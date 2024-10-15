from flask import render_template, session, g, request
from helpers.QueryHelpers import executeGet, executePost, changeStatus
from helpers.HelperFunction import responseData, allowed_image_file, generate_random_filename
import os
from werkzeug.utils import secure_filename
import uuid

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'images', 'uploads')

def products():
    active_menu = ['product', 'products']
    if g.authenticated.get('role_id') == 1:
        products = getProducts("")
        categories = getCategories("")
    else:
        products = getProducts("WHERE c.user_id = %s AND p.status = 1")
        categories = getCategories("WHERE c.user_id = %s AND c.status = 1")
    return render_template('views/products/index.html', menu=active_menu, cat_data=categories, prod_data=products)


def getProducts(prod):
    query = f"SELECT p.product_id, p.category_id, p.product_name, c.category_name, p.description, p.price, p.qty, p.created_at, p.status FROM products p LEFT JOIN categories c ON p.category_id = c.category_id {prod}"
    if prod:
        results = executeGet(query, (g.authenticated.get('user_id'),))
    else:
        results = executeGet(query)
    
     # Format the price for each product
    for product in results:
        product['price'] = "{:,.2f}".format(product['price'])
        product['qty'] = "{:,.2f}".format(product['qty'])  

    return results



def addProduct():
    product_name = request.form.get('productName')
    category_id = request.form.get('category_menu')
    description = request.form.get('description')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    images = request.files.getlist('productImages[]')
    image_names = []

    if product_name is None or product_name == "":
        return responseData("error", "Product name is required", "", 200)
    if category_id is None or category_id == "":
        return responseData("error", "Please select a category", "", 200)
    if description is None or description.strip() == "" or description.strip() == "<p><br></p>":
        # Check for empty or default Quill editor content
        return responseData("error", "Please provide a description", "", 200)
    if price is None or price == "":
        return responseData("error", "Enter the price", "", 200)
    if quantity is None or quantity == "":
        return responseData("error", "Enter the quantity", "", 200)
    if not images or images[0].filename == '':
        return responseData("error", "Please select image", "", 200)

    #insert attacthment
    for image in images:
        if image and allowed_image_file(image.filename):  # Check if it's a valid file type
            file_extension = os.path.splitext(secure_filename(image.filename))[1]  # Get the file extension
            random_filename = generate_random_filename(file_extension)  # Generate random filename with extension
            image.save(os.path.join(UPLOAD_FOLDER, random_filename))  # Save the file
            image_names.append(random_filename)  # Store the random filename
            print(f"gooodsss {image_names}")
        else:
            print(f"heellooo {image_names}")
            return responseData("error", "Invalid file type", "", 200)   
        
        
    
        
    #Insert product
    
    insert_query = "INSERT INTO products (category_id, product_name, description, price, qty) VALUES (%s, %s, %s, %s, %s)"
    result = executePost(insert_query, (category_id, product_name, description, price, quantity))
        
    if "last_inserted_id" in result: 
        # Loop through the image_names array and insert each filename into the database
        for name in image_names:
            attachment_query = "INSERT INTO product_attachments (product_id, attachment) VALUES (%s, %s)"
            try:
                executePost(attachment_query, (result['last_inserted_id'], name))  # Insert product_id and filename
            except Exception as e:
                print(f"Error inserting {name} into database: {str(e)}") 

        return responseData("success", "New product added", "", 200)
    else:
        return responseData("error", "Something went wrong!.", "", 200)
    


def productCategories():
    active_menu = ['product', 'categories']
    if g.authenticated.get('role_id') == 1:
        categories = getCategories("")
    else:
        categories = getCategories("WHERE c.user_id = %s AND c.status = 1")
    return render_template('views/products/categories.html', menu=active_menu, cat_data=categories)

def changeProductStatus():
    product_id = request.args.get('prod_id')
    status_to = request.args.get('status_to')
    res = changeStatus("products","product_id", product_id, status_to)
    if res:
        return responseData("success", "Product has been deleted.", product_id, 200)





def getCategories(condition):
    query = f"SELECT c.user_id, c.category_id, c.category_name, c.created_at, c.updated_at, c.status, u.firstname, u.lastname FROM categories c LEFT JOIN users u ON c.user_id = u.user_id {condition} ORDER BY created_at DESC"
    if condition:
        results = executeGet(query, (g.authenticated.get('user_id'),))
    else:
        results = executeGet(query)
    return results


def getCategoriesByField(field, condition):
    query = f"SELECT {field} FROM categories {condition}"
    results = executeGet(query)
    return results

def getProductsByField(field, condition):
    query = f"SELECT {field} FROM product {condition}"
    results = executeGet(query)
    return results


def addCategories():
    user_id = g.authenticated.get('user_id')
    category_name = request.form.get('catname')

    if category_name is None or category_name == "":
        return responseData("error", "Category field is required", "", 200)

    categories = getCategoriesByField("category_name",
                                      f"WHERE category_name = '{category_name}' AND user_id = {g.authenticated.get('user_id')}")

    if categories:
        return responseData("error", "Category name is already exist", "", 200)
    else:
        insert_query = "INSERT INTO categories (user_id, category_name) VALUES (%s, %s)"
        executePost(insert_query, (user_id, category_name))
        return responseData("success", "New category has been added.", "", 200)



def changeCategoryStatus():
    category_id = request.args.get('cat_id')
    status_to = request.args.get('status_to')
    res = changeStatus("categories","category_id", category_id, status_to)
    if res:
        return responseData("success", "Category has been deleted.", category_id, 200)




def updateCategories():
    category_name = request.form.get('catname')
    category_id = request.form.get('category_id')

    if category_name is None or category_name == "":
        return responseData("error", "Category field is required", "", 200)

    categories = getCategoriesByField("category_name",
                                      f"WHERE category_name = '{category_name}' AND user_id = {g.authenticated.get('user_id')}")

    if categories:
        return responseData("error", "Category name is already exist", "", 200)
    else:
        query = "UPDATE categories SET category_name = %s WHERE category_id = %s"
        executePost(query, (category_name, category_id))
        return responseData("success", "Category has been updated.", "", 200)
    

def updateProducts():
    product_name = request.form.get('prodname')
    category_id = request.form.get('category_id')
    description =  request.form.get('description')
    price =  request.form.get('price')
    quantity =  request.form.get('quantity')

    
    if product_name is None or product_name == "":
        return responseData("error", "Product field is required", "", 200)
    
    if price is None or price == "":
        return responseData("error", "Price field is required", "", 200)
    
    if quantity is None or quantity == "":
        return responseData("error", "Quantity field is required", "", 200)
    
    



