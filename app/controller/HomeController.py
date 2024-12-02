from flask import render_template, request, session, g, url_for
from helpers.QueryHelpers import executeGet, executePost, changeStatus
from helpers.HelperFunction import responseData, allowed_image_file, generate_random_filename

import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def home():
    page = request.args.get('page', 1, type=int)
    categories = getCategoriesInHome("WHERE status = 1")
    products = getProductsInHome("WHERE p.status = 1", page=page)
    return render_template('views/home.html', cat_data=categories, prod_data=products, page=page, per_page=10)

def getCategoriesInHome(condition=""):
    query = f"SELECT * FROM `categories` {condition}"
    results = executeGet(query)
    return results

def getProductsInHome(condition="", page=1, per_page=10):
    offset = (page - 1) * per_page
    query = f"SELECT p.product_id, p.category_id, p.product_name, c.category_name, pa.attachment, p.description, p.price, p.qty, p.created_at, p.status FROM products p LEFT JOIN categories c ON p.category_id = c.category_id left JOIN product_attachments pa ON p.product_id = pa.product_id {condition} AND c.status != 2 GROUP BY p.product_id, p.category_id, p.product_name, c.category_name, p.price, p.qty, p.created_at, p.status LIMIT {offset}, {per_page}"
    results = executeGet(query)
    
    if not results:  # Check if results is empty
        return []  # Return an empty list or handle as needed

    for product in results:
        product['formatted_price'] = locale.format_string("%0.2f", product['price'], grouping=True)
        if product['attachment'] is not None:
            product['attachment'] = url_for('static', filename='images/uploads/' + product['attachment'])
        else:
            product['attachment'] = None
    return results

def loadMoreProducts():
    page = request.args.get('page', 1, type=int)
    products = getProductsInHome("WHERE p.status = 1", page=page)
    
    if products is None or products == "":
        return responseData("error", "No more products found.", [], 200)

    return responseData("success", "Products loaded successfully.", products, 200)

def categoryPage(category_id):
    products = getProductsInCategory(category_id)
    categories = getCategoriesInHome("WHERE status = 1")

    # Check if products list is empty
    if not products:
        return render_template('/views/categories.html', data=[], cat_data=categories)  # Pass an empty list

    return render_template('/views/categories.html', data=products, cat_data=categories)

def getProductsInCategory(category_id):
    query = f"SELECT p.product_id, p.user_id, p.product_name, p.price, p.status AS product_status, pa.product_attachment_id, pa.product_id AS attachment_product_id, pa.attachment, pa.status AS attachment_status, c.category_id, c.category_name, c.status AS category_status FROM products p LEFT JOIN product_attachments pa ON p.product_id = pa.product_id LEFT JOIN categories c ON p.category_id = c.category_id WHERE c.category_id = {category_id} AND c.status = 1;"
    results = executeGet(query)
    
    if not results:  # Check if results is empty
        return []  # Return an empty list or handle as needed

    for product in results:
        product['formatted_price'] = locale.format_string("%0.2f", product['price'], grouping=True)
        if 'attachment' in product and product['attachment'] is not None:
            product['attachment'] = url_for('static', filename='images/uploads/' + product['attachment'])
            print(f"Image URL for {product['product_name']}: {product['attachment']}")
        else:
            product['attachment'] = None
            print(f"No image for {product['product_name']}")
    return results