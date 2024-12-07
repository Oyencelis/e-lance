from flask import render_template, session, g, request
from helpers.QueryHelpers import executeGet, executePost, changeStatus
from helpers.HelperFunction import responseData, allowed_image_file, generate_random_filename
import os
from werkzeug.utils import secure_filename
import uuid
from controller.HomeController import getCategoriesInHome

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'images', 'uploads')

def products():
    active_menu = ['product', 'products']
    categories = getCategories("")
    if g.authenticated.get('role_id') == 1:
        products = getProducts("")
        
    else:
        products = getProducts("AND p.user_id = %s")
    return render_template('views/products/index.html', menu=active_menu, cat_data=categories, prod_data=products)


def getProducts(condition):
    # query = f"SELECT p.product_id, p.category_id, p.product_name, c.category_name, p.description, p.price, p.qty, p.created_at, p.status FROM products p LEFT JOIN categories c ON p.category_id = c.category_id  {prod}"
    query = f"SELECT p.product_id, p.category_id, p.product_name, c.category_name, p.description, p.price, p.qty, p.created_at, p.status, u.user_id, u.firstname, u.lastname FROM products p LEFT JOIN categories c ON p.category_id = c.category_id LEFT JOIN users u ON p.user_id = u.user_id WHERE p.status = 1 AND c.status != 2 {condition}"
    if condition:
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
    user_id = g.authenticated.get('user_id')
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
    
    insert_query = "INSERT INTO products (category_id, user_id, product_name, description, price, qty) VALUES (%s, %s, %s, %s, %s, %s)"
    result = executePost(insert_query, (category_id, user_id, product_name, description, price, quantity))
        
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
    # if g.authenticated.get('role_id') == 1:
    #     categories = getCategories("")
    # else:
    categories = getCategories("")
    return render_template('views/products/categories.html', menu=active_menu, cat_data=categories)

def changeProductStatus():
    product_id = request.args.get('prod_id')
    status_to = request.args.get('status_to')
    res = changeStatus("products","product_id", product_id, status_to)
    if res:
        return responseData("success", "Product has been deleted.", product_id, 200)
    
def viewProduct(product_id):
    categories = getCategoriesInHome("WHERE status = 1")
    try:
        # Sanitize the product_id input
        product_id = int(product_id)
        
        # Get product details using direct SQL query for debugging
        query = "SELECT p.product_id, p.product_name, p.description, p.price, p.qty, COALESCE (pa.attachment, 'no-image.jpg') as attachment FROM products p LEFT JOIN product_attachments pa ON p.product_id = pa.product_id WHERE p.product_id = %s AND p.status = 1"
        
        product = executeGet(query, (product_id,))
        
        # Check if the product list is empty
        if not product:
            print(f"No product found with ID: {product_id}")
            return render_template('views/404.html'), 404
            
        product = product[0]  # Get the first result
        
        # Prepare image URL
        image_path = product['attachment']
        if image_path and image_path != 'no-image.jpg':
            product_image_url = '/static/images/uploads/' + image_path
        else:
            product_image_url = '/static/images/no-image.jpg'
        
        return render_template('views/Products/view-products.html',
                             product_name=product['product_name'],
                             product_description=product['description'],
                             product_price=product['price'],
                             product_image_url=product_image_url,
                             product_qty=product['qty'],
                             product_id=product_id,
                             cat_data=categories)
                             
    except Exception as e:
        print(f"Error in viewProduct: {str(e)}")
        return render_template('views/404.html'), 404





def getCategories(condition):
    # query = f"SELECT c.user_id, c.category_id, c.category_name, c.created_at, c.updated_at, c.status, u.firstname, u.lastname FROM categories c LEFT JOIN users u ON c.user_id = u.user_id {condition} ORDER BY created_at DESC"
    query = f"SELECT * FROM categories WHERE status = 1"
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
    query = f"SELECT {field} FROM products {condition}"
    results = executeGet(query)
    return results


def addCategories():
    # user_id = g.authenticated.get('user_id')
    category_name = request.form.get('catname')

    if category_name is None or category_name == "":
        return responseData("error", "Category field is required", "", 200)

    categories = getCategoriesByField("category_name",
                                      f"WHERE category_name = '{category_name}'")

    if categories:
        return responseData("error", "Category name is already exist", "", 200)
    else:
        insert_query = "INSERT INTO categories (category_name) VALUES (%s)"
        executePost(insert_query, (category_name,))
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
                                      f"WHERE category_name = '{category_name}'")

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
    product_id = request.form.get('product_id')

    
    if product_name is None or product_name == "":
        return responseData("error", "Product name is required", "", 200)
    
    if category_id is None or category_id == "":
        return responseData("error", "Category is required", "", 200)
    
    if description is None or description == "":
        return responseData("error", "Description is required", "", 200)
    
    if price is None or price == "":
        return responseData("error", "Price is required", "", 200)
    
    if quantity is None or quantity == "":
        return responseData("error", "Quantity is required", "", 200)
    
    products = getProductsByField("product_name", f"WHERE product_name = '{product_name}' AND category_id = {category_id}")
    if products:
        return responseData("error", "Product name already exists in this category", "", 200)
    
    # Perform the update query
    query = "UPDATE products SET product_name = %s, category_id = %s, description = %s, price = %s, quantity = %s WHERE product_id = %s"
    executePost(query, (product_name, category_id, description, price, quantity, product_id))
    
    return responseData("success", "Product has been updated.", "", 200)

def buyProduct(product_id):
    if request.method == 'POST':
        # Process the form data
        full_name = request.form.get('full_name')
        mobile_number = request.form.get('mobile_number')
        floor_unit = request.form.get('floor_unit')
        province = request.form.get('province')
        district = request.form.get('district')
        ward = request.form.get('ward')
        other_notes = request.form.get('other_notes')
        payment_method = request.form.get('payment_method')

        # Validate the input data
        if not full_name or not mobile_number or not payment_method:
            return responseData("error", "Please fill in all required fields.", "", 400)

        # Payment processing logic
        try:
            # Call payment gateway API here
            # e.g., charge the user
            pass
        except Exception as e:
            return responseData("error", "Payment processing failed: " + str(e), "", 400)

        return responseData("success", "Order placed successfully!", "", 200)

    return render_template('views/Products/buy-products.html', product_id=product_id,)