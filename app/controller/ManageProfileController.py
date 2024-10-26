from flask import render_template, session, request, g
from flask_login import current_user
from helpers.HelperFunction import responseData
from helpers.QueryHelpers import executePost, executeGet

def manageProfile():
    active_menu = ['manage']
    return render_template('views/manage-profile/manageProfile.html', menu = active_menu)

def sellerRequest():
    user_id = session.get('user_id')
    print(f"User ID: {user_id}")  # Debugging
    query = "SELECT user_id FROM seller_details WHERE user_id = %s"
    
    # Execute the query to check if the user already has a seller request
    result = executeGet(query, (user_id,))
    
    # If user already has a seller request, you might want to inform them
    if result:  # Assuming `result` returns a list of records
        return render_template('views/become-seller.html', message="You already have a seller request under review.")

    return render_template('views/become-seller.html')

def sellerRequestSubmit():
    store_name = request.form.get('storeName')
    business_description = request.form.get('businessDescription')

    if not store_name:
        return responseData("error", "Store name is required", "", 200)
    if not business_description:
        return responseData("error", "Description is required", "", 200)
    
    insert_query = "INSERT INTO seller_details (user_id, store_name, description) VALUES (%s, %s, %s)"
    
    # Execute the insertion and check if it was successful
    if executePost(insert_query, (g.authenticated['user_id'], store_name, business_description)):
        return responseData("success", "Your request to become a seller has been submitted, please wait for approval.", "", 200)
    else:
        return responseData("error", "Failed to insert your request into the database.", "", 200)

    