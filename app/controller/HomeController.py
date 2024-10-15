from flask import render_template, session

def home():
    user_role = session.get('role_id')
    firstname = session.get('firstname')
    lastname = session.get('lastname')

   
    return render_template('views/home.html', user_role = user_role, firstname = firstname, lastname = lastname)