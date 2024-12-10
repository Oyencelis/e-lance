from flask import render_template, request, jsonify, session, redirect, url_for
from helpers.HelperFunction import responseData, hashing
from helpers.QueryHelpers import executeGet, executePost
from helpers.Session import setSession, sessionRemove
# from controller.SessionController import login_user, logout_user, is_logged_in


def login():
    if 'user_id' in session:
        user_role = session.get('role_id')

        if user_role == 1:
            return redirect('/dashboard')
        else:
            return redirect('/') 
    return render_template('views/login.html')

def LoginSubmit():
    email = request.form.get('email')
    password = request.form.get('password')
    hashedValue = hashing(password)
    print(hashedValue)
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    user = executeGet(query, (email, hashedValue))
    
    if user:
        user = user[0]
        
        if user['status'] == 1:
            user_detail = {
                'user_id': user['user_id'],
                'role_id': user['role_id'],
                'firstname': user['firstname'],
                'lastname': user['lastname'],
            }

            setSession('authenticated', user_detail)
            return responseData("success", "Login Successfully", user, 200)
        else:
            return responseData("error", "Your account is banned. Please contact support.", None, 200)
    else:
        return responseData("error", "Invalid username or password", None, 200)


def signup():
    return render_template('views/signup.html')


def signupSubmit():
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirmPassword')

    # Validate all fields
    if fname is None or fname == "":
        return responseData("error", "First name is required", "", 200)
    if lname is None or lname == "":
        return responseData("error", "Last name is required", "", 200)
    if email is None or email == "":
        return responseData("error", "Email is required", "", 200)
    if phone is None or phone == "":
        return responseData("error", "Phone is required", "", 200)
    if password is None or password == "":
        return responseData("error", "Password is required", "", 200)
    if confirmPassword is None or confirmPassword == "":
        return responseData("error", "confirmPassword is required", "", 200)
    
    select_query = "SELECT email FROM users WHERE email = %s"
    check_email = executeGet(select_query, (email,))
    if check_email:
        return responseData("error", "Email already exist", "", 200)
    else:
        hashed_password = hashing(password)

        insert_query = "INSERT INTO users (firstname, lastname, email, password, phone) VALUES (%s, %s, %s, %s, %s)"
        executePost(insert_query, (fname, lname, email, hashed_password, phone))
        return responseData("success", "User registered successfully", "", 200)
    


def dashboard():
    return render_template('views/dashboard.html')

def logout():
    return redirect(url_for('home_page'))  # Redirect to home or login page