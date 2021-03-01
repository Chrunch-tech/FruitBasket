""" Defining all the routes and apps used in this website """
from flask import render_template, session, redirect, url_for, flash
from .model import Products, Users, FeedBacks, Orders
from .form import SearchFrom, RegistrationForm, LoginForm, Feedback, UpdateAccount, AddToCartForm, ShippingForm
from . import app, bcrypt, db
import random
import secrets
import os
from PIL import Image


@app.route('/', methods=['GET', 'POST'])
def home():  # Home page of the website
    """
    Defining the home page
    :return: All the needs in the home page
    """
    search_form = SearchFrom()
    products = []
    for i in range(len(Products.query.all())):
        if len(products) <= 5:
            products.append(Products.query.all()[i])
        else:
            break
    if search_form.validate_on_submit():
        session['searchBar_data'] = search_form.searchBar.data
        return redirect(url_for('search_result'))
    return render_template('home.html', search_form=search_form, products=products)


@app.route('/registration', methods=['GET', 'POST'])
def register():  # Registration page of the website
    """
    Defining the registration page
    :return: All the things from which users can make there account
    """
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        hash_id = bcrypt.generate_password_hash(str(random.randint(400, 800))).decode('utf-8')
        password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        a = random.randint(1, 10)
        b = random.randint(1, 1000)
        user = Users(
            userId=random.randint(a, b),
            hash_id=hash_id,
            username=register_form.username.data,
            email=register_form.email.data,
            profile_img=url_for('static', filename='default.jpg'),
            password=password)
        if register_form.password.data != register_form.conform_password.data:
            flash('Password dose\'nt match')
        else:
            print("Working")
            db.session.add(user)
            db.session.commit()
            flash('Your account is successfully created! Now you\'ll able to login')
            return redirect(url_for('login'))
    return render_template('register.html', register_form=register_form)


def save_image(form_picture):
    """
    :raises:
    Saving the user profile image to the database
    :return: path to store the profile image
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    image = random_hex + f_ext
    image_path = os.path.join(app.root_path, 'static', 'profile_pic', image)
    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(image_path)
    return image


@app.route('/login', methods=['GET', 'POST'])
def login():  # Login page of the website
    login_form = LoginForm()
    if login_form.validate_on_submit():
        check_user = Users.query.filter_by(username=login_form.username.data).first()
        checkPassword = bcrypt.check_password_hash(pw_hash=check_user.password, password=login_form.password.data)
        if login_form.username.data == check_user.username and checkPassword:
            session['username'] = login_form.username.data
            flash(f'Welcome! {session["username"]}')
            return redirect(url_for('profile'))
        else:
            flash("Maybe the password or username is not valid!")
    return render_template('login.html', login_form=login_form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():  # Users profile page
    """
    Defining users profile page ;)
    :return: Page with the users profile pic along with there account controls
    """
    if "username" in session:
        feedback = Feedback()
        updateAccount = UpdateAccount()
        latestProducts = []
        my_orders = []
        user = Users.query.filter_by(username=session['username']).first()
        order = Orders.query.filter_by(customerEmail=user.email).all()
        for i in range(len(order)):
            my_orders.append(order[i])
        username = user.username
        email = user.email
        profile_img = user.profile_img
        for i in range(len(Products.query.all())):  # Getting the latest product data.
            if len(latestProducts) <= 6:
                latestProducts.append(Products.query.all()[i])
            else:
                break
        if feedback.validate_on_submit():
            feedback_message = feedback.message_bar.data
            feedback_data = FeedBacks(costumerId=user.userId,
                                      costumerName=user.username,
                                      email=user.email,
                                      message=feedback_message)
            db.session.add(feedback_data)
            db.session.commit()
            return redirect(url_for('profile'))
        if updateAccount.validate_on_submit():
            if updateAccount.profile_img.data:
                print(updateAccount.profile_img.data)
                update_image = save_image(updateAccount.profile_img.data)
                user.profile_img = 'static/profile_pic/' + update_image
            update_name = updateAccount.name.data
            user.username = update_name
            update_email = updateAccount.email.data
            user.email = update_email
            db.session.add(user)
            db.session.commit()
            session['username'] = updateAccount.name.data
            flash('Your account is successfully updated!')
            return redirect(url_for('profile'))
    else:
        flash('You\'ll first need to login and if you don\'t have a account then register a account')
        return redirect(url_for('login'))
    return render_template('profile.html', latestProducts=latestProducts, feedback=feedback,
                           username=username, email=email, profile_img=profile_img, updateAccount=updateAccount,
                           my_orders=my_orders)


def valid_input(value):
    """
    Making valid user input
    :param value: User input
    :return: valid user input
    """
    char_table = {'a': 'A',
                  'b': 'B',
                  'c': 'C',
                  'd': 'D',
                  'e': 'E',
                  'f': 'F',
                  'g': 'G',
                  'h': 'H',
                  'i': 'I',
                  'j': 'J',
                  'k': 'K',
                  'l': 'L',
                  'm': 'M',
                  'n': 'N',
                  'o': 'O',
                  'p': 'P',
                  'q': 'Q',
                  'r': 'R',
                  's': 'S',
                  't': 'T',
                  'u': 'U',
                  'v': 'V',
                  'w': 'W',
                  'x': 'X',
                  'y': 'Y',
                  'z': 'Z'
                  }
    if value[0] not in char_table.values():
        for i in char_table.keys():
            check = value[0] == i
            if check:
                result = value.replace(value[0], char_table[i])
                return result
    else:
        return value


def results(input_data):
    """
    Defining how to process the search data
    :param input_data: Taking search data as a input for this fuction
    :return: The list of product name based on the search
    """
    output = []
    names = []
    result = valid_input(input_data)
    for i in range(len(Products.query.all())):
        names.append(Products.query.all()[i].productName)
    for name in names:
        if result in name:
            product_data = Products.query.filter_by(productName=name).first()
            output.append(product_data)
    return output


@app.route('/products', methods=['GET', 'POST'])
def search_result():
    """
    Finally defining the search results
    :returns: The page with the with the list of products
    """
    searchForm = SearchFrom()
    if searchForm.validate_on_submit():
        value = searchForm.searchBar.data
        products = results(value)
        return render_template('search_result.html', searchForm=searchForm, value=value, products=products)
    else:
        if "searchBar_data" in session:
            value = session['searchBar_data']
            products = results(value)
        else:
            return redirect(url_for('home'))
    return render_template('search_result.html', searchForm=searchForm, value=value, products=products)


@app.route('/<int:product_id>', methods=['GET', 'POST'])
def product_info(product_id):
    add_to_cart = AddToCartForm()
    customer = Users.query.filter_by(username=session["username"]).first()
    product = Products.query.get_or_404(product_id)
    if add_to_cart.validate_on_submit():
        order = Orders(productId=product_id, productName=product.productName, productPrice=product.price,
                       image_url=product.image_url,
                       quantity=add_to_cart.amount.data, customerName=customer.username, customerEmail=customer.email)
        db.session.add(order)
        db.session.commit()
        flash('Product is successfully added')
        return redirect(url_for('search_result'))
    return render_template('productInfo.html', product=product, shippingForm=add_to_cart)


@app.route('/shipping', methods=['GET', 'POST'])
def shipping():
    shippingForm = ShippingForm()
    if "username" in session:
        selected_products = []
        user = Users.query.filter_by(username=session["username"]).first()
        order = Orders.query.filter_by(customerEmail=user.email).all()
        for i in range(len(order)):
            selected_products.append(order[i])
        if shippingForm.validate_on_submit():
            return redirect(url_for('gritting'))
    else:
        return redirect(url_for('home'))
    return render_template('shipping.html', shippingForm=shippingForm, selected_products=selected_products, user=user)


@app.route('/gritting')
def gritting():
    """
    Final gritting to the user
    :return: The gritting page
    """
    return render_template('gritting.html')


@app.errorhandler(404)
def error(e):  # An 404 error page
    """
    Defining the error page
    :param e: type to error
    :return: error page
    """
    return render_template('error.html'), e

# And Done ;).
