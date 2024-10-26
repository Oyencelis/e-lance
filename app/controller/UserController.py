from flask import render_template, session
from helpers.QueryHelpers import executeGet

def seller():
    active_menu = ['users', 'seller']
    return render_template('views/users/seller.html', menu = active_menu)