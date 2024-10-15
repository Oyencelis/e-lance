from functools import wraps
from flask import Flask, session, redirect, url_for, g
#Middleware
from middleware.auth import login_required
#Helpers
from helpers.Session import sessionRemove
# Controllers
from controller.HomeController import home
from controller.LoginController import login, LoginSubmit, signup, signupSubmit
# Authenticate controllers
from controller.DashboardController import dashboardIndex
from controller.ProductController import productCategories, addCategories, changeCategoryStatus, updateCategories, products, addProduct, changeProductStatus, updateProducts





def setup_routes(app: Flask):

    @app.before_request
    def load_user():
        g.authenticated = session.get('authenticated', None)

    #HomeController
    @app.route('/')
    def home_page():
        return home() 
    
    #Login Controller
    @app.route('/login')
    def login_page():
        # Check if the user is already logged in
        if g.authenticated:
            return redirect(url_for('home_page'))  # Redirect to home if logged in
        return login() 
    
    @app.route('/login', methods=['POST'])
    def login_submit():
        return LoginSubmit() 
    
    #Sign Up Controller
    @app.route('/signup')
    def signup_page():
        # Check if the user is already logged in
        if g.authenticated:
            return redirect(url_for('home_page'))  # Redirect to home if logged in
        return signup()
    
    @app.route('/signup', methods=['POST'])
    def signup_submit():
        return signupSubmit()
    

    

    @app.route('/logout')
    @login_required 
    def logout():
        sessionRemove('authenticated') # Clear session data
        return redirect(url_for('login_page'))

    @app.route('/dashboard')
    @login_required 
    def dashboard_page():
        return dashboardIndex()
    

    @app.route('/product/categories')
    @login_required 
    def product_categories():
        return productCategories()
    

    @app.route('/add-category', methods=['POST'])
    def add_categories():
        return addCategories()
    
    @app.route('/change-category-status', methods=['GET', 'POST'])
    def change_category_status():
        return changeCategoryStatus()

    @app.route('/update-category', methods=['POST'])
    def update_categories():
        return updateCategories()
    
    @app.route('/product')
    @login_required
    def product_page():
        return products()
    
    @app.route('/add-product', methods=['POST'])
    def add_product():
        return addProduct()
    
    @app.route('/change-product-status', methods=['GET', 'POST'])
    def change_product_status():
        return changeProductStatus()
    
    @app.route('/')
    @login_required
    def update_products():
        return updateProducts()