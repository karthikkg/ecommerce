import json
import os
import sys
import requests
from ast import literal_eval
from flask import Blueprint, jsonify
from flask import  render_template, url_for, request, redirect, flash, make_response, abort,session
from logging import DEBUG
from src import app
from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, FileField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, email, EqualTo
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['jpg','jpeg','png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#UPLOAD_FOLDER = 'C:\\Users\\Karthik\\hello-python-flask\\microservices\\app\\src\\static\\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



PRODUCTION_ENV = os.environ.get("PRODUCTION")
CLUSTER_NAME = os.environ.get("CLUSTER_NAME")
if CLUSTER_NAME is None:
    print("""
    Set the name of your cluster as an environment variable and start again:

    $ export CLUSTER_NAME=<cluster-name>

    """)

if PRODUCTION_ENV == "true":
    # set dataUrl as internal url if PRODUCTION_ENV is true
    # note that internal url has admin permissions
    dataUrl = "https://data." + "banner20" + ".hasura-app.io/v1/query"
else:
    # for local development, contact the cluster via external url
    dataUrl = "https://data." + "banner20" + ".hasura-app.io/v1/query"

hasura_examples = Blueprint('hasura_examples', __name__)

app.config['SECRET_KEY'] = b'\xb7\xd8\xa0\x8b\x82\r\xa4W\xb00\x13s\x00\x1e\xd6hT\xc3F@3\xff<\x1e'
app.config['DEBUG'] = True

toolbar = DebugToolbarExtension(app)
@hasura_examples.route('/getinfo')
def getinfo():
    if '_flashes' in session:

    # This is the url to which the query is made
        url = "https://auth.banner20.hasura-app.io/v1/user/info"

        # This is the json payload for the query
        # Setting headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": 'Bearer ' +str(session['_flashes'][0][1]['auth_token'])
        }

        # Make the query and store response in resp
        resp = requests.request("GET", url, headers=headers)

        # resp.content contains the json response.
        return resp.content
    else:
        return 'you are not logged in'


@hasura_examples.route("/get_users")
def get_users():
    query = {
        "type": "select",
        "args": {
            "table": "user",
            "columns": [
                "*"
            ]
        }
    }
    print(dataUrl)
    print(json.dumps(query))
    response = requests.post(
        dataUrl, data=json.dumps(query)
    )
    data = response.json()
    print(json.dumps(data))
    return jsonify(data=data)
# Task 7: A text box which sends data as POST to any endpoint and log the received to stdout.
class InputForm(Form):
    """docstring for InputForm"""
    first_name = StringField('first_name', validators = [DataRequired()])
    last_name = StringField('last_name', validators = [DataRequired()])
    email = EmailField('email', validators = [DataRequired(), email()]) 
    phone_number = StringField('phone_number', validators = [DataRequired()]) 
    password = PasswordField('password',validators=[DataRequired()])
    #confirm = PasswordField('password2',validators=[DataRequired()])

@hasura_examples.route('/input',methods=['GET','POST'])
def inputf():
    form = InputForm()
    if form.validate_on_submit(): #if request.method == "POST":
        print("\n\n\nprint \n entered form correctly\n \n")
        first_name = form.first_name.data #request.form['first_name']
        last_name = form.last_name.data #request.form['last_name']
        email = form.email.data #request.form['email']
        phone_number = form.phone_number.data #request.form['phone_number']
        password = form.password.data #request.form['password']
        print(first_name,last_name,email,phone_number,password)
        app.logger.debug('Submitted Successfully :-)\nName: '+first_name +'\nEmail : '+ email)

        # This is the json payload for the query
        requestPayload = {
            "type": "insert",
            "args": {
                "table": "user",
                "objects": [{"user_first_name": first_name,
            "user_last_name": last_name,
            "user_email_address": email,
            "phone_number": phone_number,
            "password": password}]
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)
        data=resp.json()

        # resp.content contains the json response.
        print(resp.content)
        #logging the input to stdout
        #app.logger.debug('Submitted Successfully :-)\nName: '+name +'\nEmail : '+ email)
        #print('Submitted Successfully :-)\nName: '+name +'\nEmail : '+ email)
        #flash('Submitted Successfully :-) Name: '+name +' | Email : '+ email)
        return jsonify(data=data)
    return render_template('input.html',form = form)

class signupForm(Form):
    """docstring for InputForm"""
    first_name = StringField('first_name', validators = [DataRequired()])
    last_name = StringField('last_name', validators = [DataRequired()])
    email = EmailField('email', validators = [DataRequired(), email()]) 
    phone_number = StringField('phone_number', validators = [DataRequired()]) 
    password = PasswordField('password',validators=[DataRequired(),EqualTo('password2','Passwords must match')])
    password2 = PasswordField('password2',validators=[DataRequired()])

@hasura_examples.route('/signup',methods=['GET','POST'])
def signup():
    form = signupForm()
    if form.validate_on_submit(): #if request.method == "POST":
        print("\n\n\nprint \n entered form correctly\n \n")
        first_name = form.first_name.data #request.form['first_name']
        last_name = form.last_name.data #request.form['last_name']
        email = form.email.data #request.form['email']
        phone_number = form.phone_number.data #request.form['phone_number']
        password = form.password.data #request.form['password']
        print(first_name,last_name,email,phone_number,password)
        app.logger.debug('Submitted Successfully :-)\nName: '+first_name +'\nEmail : '+ email)

        # This is the json payload for the query
        requestPayload = {
            "type": "select",
            "args": {
                "table": "user",
                "columns": [
                    "user_email_address"
                ],
                "where": {
                    "user_email_address": {
                        "$eq": email
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)


        # resp.content contains the json response.
        if resp.json():
            return render_template("signup.html",form=form)
        else:
            authurl = "https://auth.banner20.hasura-app.io/v1/signup"

            # This is the json payload for the query
            requestPayload = {
                            "provider": "username",
                            "data": {
                                "username": email,
                                "password": password
                            }
                        }

            # Setting headers
            headers = {
                "Content-Type": "application/json"
            }

            # Make the query and store response in resp
            resp = requests.request("POST", authurl, data=json.dumps(requestPayload), headers=headers)

            # resp.content contains the json response.
            print('\n\n')
            print(resp.json())
            print('\n\n')
            hasura_user_id= resp.json()['hasura_id']
            print('\n\nhasura_id: '+str(hasura_user_id)+'\n')

            requestPayload = {
                                "type": "insert",
                                "args": {
                                    "table": "user",
                                    "objects": [{"user_first_name": first_name,
                                                "user_last_name": last_name,
                                                "user_email_address": email,
                                                "phone_number": phone_number,
                                                "password": password, "hasura_id": hasura_user_id}
                                    ]
                                }
                            }

            # Setting headers
            headers = {
                "Content-Type": "application/json"
            }

            # Make the query and store response in resp
            resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

            # resp.content contains the json response.
            print(resp.content)
    return render_template('signup.html',form = form)

class seller_signupForm(Form):
    """docstring for InputForm"""
    first_name = StringField('first_name', validators = [DataRequired()])
    last_name = StringField('last_name', validators = [DataRequired()])
    email = EmailField('email', validators = [DataRequired(), email()]) 
    phone_number = StringField('phone_number', validators = [DataRequired()]) 
    password = PasswordField('password',validators=[DataRequired(),EqualTo('password2','Passwords must match')])
    password2 = PasswordField('password2',validators=[DataRequired()])

@hasura_examples.route('/seller_signup',methods=['GET','POST'])
def seller_signup():
    form = seller_signupForm()
    if form.validate_on_submit():
        print("\n\n\nprint \n entered form correctly\n \n")
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        password = form.password.data
        print(first_name,last_name,email,phone_number,password)
        app.logger.debug('Submitted Successfully :-)\nName: '+first_name +'\nEmail : '+ email)

        # This is the json payload for the query
        requestPayload = {
            "type": "select",
            "args": {
                "table": "seller",
                "columns": [
                    "email_address"
                ],
                "where": {
                    "email_address": {
                        "$eq": email
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)


        # resp.content contains the json response.
        if resp.json():
            print('\n'+str(resp.json())+'username/email already registerd'+'\n')
            return render_template('seller_signup.html',form=form)
        else:
            print('\n'+str(resp.json())+'username/email not yet registerd'+'\n')
            authurl = "https://auth.banner20.hasura-app.io/v1/signup"

            # This is the json payload for the query
            requestPayload = {
                            "provider": "username",
                            "data": {
                                "username": email,
                                "password": password
                            }
                        }

            # Setting headers
            headers = {
                "Content-Type": "application/json"
            }

            # Make the query and store response in resp
            resp = requests.request("POST", authurl, data=json.dumps(requestPayload), headers=headers)

            # resp.content contains the json response.
            print('\n\n')
            print(resp.json())
            print('\n\n')
            hasura_user_id= resp.json()['hasura_id']
            print('\n\nhasura_id: '+str(hasura_user_id)+'\n')

            requestPayload = {
                                "type": "insert",
                                "args": {
                                    "table": "seller",
                                    "objects": [{"first_name": first_name,
                                                "last_name": last_name,
                                                "email_address": email,
                                                "phone_number": phone_number,
                                                "password": password, "hasura_id": hasura_user_id}
                                    ]
                                }
                            }

            # Setting headers
            headers = {
                "Content-Type": "application/json"
            }

            # Make the query and store response in resp
            resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

            # resp.content contains the json response.
            print(resp.content)
    return render_template('seller_signup.html',form=form)

class seller_loginForm(Form):
    """docstring for InputForm"""
    email = EmailField('email', validators = [DataRequired(), email()]) 
    password = PasswordField('password',validators=[DataRequired()])
@hasura_examples.route('/seller_login',methods=['GET','POST'])
def seller_login():
    form = seller_loginForm()
    if form.validate_on_submit():
        print("\n\n\nprint \n entered form correctly\n \n")
        email = form.email.data
        password = form.password.data
        app.logger.debug('Submitted Successfully :-)\n '+'\nEmail : '+ email)


        # This is the json payload for the query
        requestPayload = {
            "type": "select",
            "args": {
                "table": "seller",
                "columns": [
                    "first_name",
                    "last_name",
                    "email_address",
                    "password"
                ],
                "where": {
                    "$and": [
                        {
                            "email_address": {
                                "$eq": email
                            }
                        },
                        {
                            "password": {
                                "$eq": password
                            }
                        }
                    ]
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        print(resp.content)

         # resp.content contains the json response.
        if resp.json():
            flash('Welcome ',email)
            return render_template('index.html',form=form,customer = resp.json())
        else:
            flash('Invalid username or password')
            return render_template('seller_login.html',form=form)
    return render_template('seller_login.html',form=form)

@hasura_examples.route('/login',methods=['GET','POST'])
def login():
    form = seller_loginForm()
    if form.validate_on_submit():
        print("\n\n\nprint \n entered form correctly\n \n")
        email = form.email.data
        password = form.password.data
        app.logger.debug('Submitted Successfully :-)\n '+'\nEmail : '+ email)

        import requests
        # This is the url to which the query is made
        url = "https://auth.banner20.hasura-app.io/v1/login"

        # This is the json payload for the query
        requestPayload = {
            "provider": "username",
            "data": {
                "username": email,
                "password": password
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
        response = make_response(render_template('index.html'))
       

        # resp.content contains the json response.
        print(resp.content)
        flash(resp.json())
        return response
    return render_template('login.html',form=form)


@hasura_examples.route('/logout', methods=['GET','POST'])
def logout():
    # This is the url to which the query is made
    url = "https://auth.banner20.hasura-app.io/v1/user/logout"

    # This is the json payload for the query
    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, headers=headers)

    # resp.content contains the json response.
    print(resp.content)
    return render_template('index.html')

class add_productForm(Form):
    """docstring for InputForm"""
    product_name = StringField('product name', validators = [DataRequired()])
    category = StringField('category', validators = [DataRequired()])
    price = StringField('price', validators = [DataRequired()]) 
    description = StringField('description', validators = [DataRequired()]) 
    specifications = StringField('specifications',validators=[DataRequired(),EqualTo('password2','Passwords must match')])
    image_0 = FileField('image_0')
    image_1 = FileField('image_1')
    image_2 = FileField('image_2')
    image_3 = FileField('image_3')
    image_4 = FileField('image_4')

@hasura_examples.route('/add_product',methods=['GET','POST'])
def add_product():
    form = add_productForm()
    if form.validate_on_submit():
        print("\n\n\nprint \n entered form correctly\n \n")
        product_name = form.product_name.data
        category = form.category.data
        price = form.price.data
        description = form.description.data
        specifications = form.specifications.data
        image_0 = form.image_0.data
        image_1 = form.image_1.data
        image_2 = form.image_2.data
        image_3 = form.image_3.data
        image_4 = form.image_4.data
        hasura_id = getinfo()

        # This is the url to which the query is made
        imagesList = [image_0, image_1, image_2, image_3, image_4]
        

        # This is the json payload for the query
        requestPayload = {
            "type": "select",
            "args": {
                "table": "seller",
                "columns": [
                    "id"
                ],
                "where": {
                    "hasura_id": {
                        "$eq": hasura_id
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        seller_id=resp.json()['id']


    
        # This is the url to which the query is made
        # This is the json payload for the query
        requestPayload = {
            "type": "select",
            "args": {
                "table": "category",
                "columns": [
                    "id"
                ],
                "where": {
                    "name": {
                        "$eq": ""
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        category_id = resp.json()['id']

        # This is the json payload for the query
        requestPayload = {
            "type": "insert",
            "args": {
                "table": "product",
                "objects": [{"product_name": product_name,
                                                "price": price,
                                                "category_id": category_id,
                                                "description": description,
                                                "specifications": specifications, "seller_id": seller_id,
                                                "product_url": url_for('/',filename='product/'+product_name)}]
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

        for image in imagesList:
            if image:
                import requests

                # This is the url to which the query is made
                fileurl = "https://filestore.banner20.hasura-app.io/v1/file"

                # Setting headers
                headers = {}

                # Open the file and make the query
                with open('test.png', 'rb') as file_image:
                    resp = requests.post(fileurl, data=file_image.read(), headers=headers)

                # resp.content contains the json response.
                print(resp.content)

        # resp.content contains the json response.
        print(resp.content)

class addphotoForm(Form):
    """docstring for InputForm"""
    image_0 = FileField('image_0')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# Display product info by product id
# url example : https://app.banner20.hasura-app.io/product?product_id=2
@hasura_examples.route("/product")
def product_info():
        
        product_id = request.args.get("product_id")
        requestPayload = {
            "type": "select",
            "args": {
                "table": "complete_product_info",
                "columns": [
                    "*"
                ],
                "where": {
                    "product_id": {
                        "$eq": product_id
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        return resp.content

# Display products by sub category id
# url example : https://app.banner20.hasura-app.io/displaybysubcategory?sub_category_id=1
@hasura_examples.route("/displaybysubcategory")
def displaybysubcategory():
        
        subcategory_id = request.args.get("sub_category_id")
        requestPayload = {
            "type": "select",
            "args": {
                "table": "complete_product_info",
                "columns": [
                    "*"
                ],
                "where": {
                    "seller_id": {
                        "$eq": subcategory_id
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        return resp.content
        

@hasura_examples.route('/add_photo',methods=['GET','POST'])
def addPhoto():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            image=filename
            # This is the url to which the query is made
            url = "https://filestore.banner20.hasura-app.io/v1/file"
            
            # Open the file and make the query
            with open(filename, 'rb') as file_image:
                resp = requests.post(url, data=file_image.read(), headers=headers)

            # resp.content contains the json response.
            print(resp.content)
            return str(resp.json())
    return render_template('addphoto.html')
@hasura_examples.route('/')
def home():
    # This is the json payload for the query
    requestPayload = {
        "type": "select",
        "args": {
            "table": "category_and_sub",
            "columns": [
                "*"
            ]
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json",
    }


    # Make the query and store response in resp
    resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.
    category_and_sub_category = resp.content.decode('utf-8')

    requestPayload = {
        "type": "select",
        "args": {
            "table": "complete_product_info",
            "columns": [
                "*"
            ]
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json"
    }

    # Make the query and store response in resp
    resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

    # resp.content contains the json response.
    all_product_info= resp.content.decode('utf-8')
    if '_flashes' in session:
        user_id= session['_flashes'][0][1]['hasura_id']
        # This is the json payload for the query
        requestPayload = {
                        "type": "select",
                        "args": {
                            "table": "user",
                            "columns": [
                                "user_first_name"
                            ],
                            "where": {
                                "hasura_id": {
                                    "$eq": user_id
                                }
                            }
                        }
                    }

        # Setting headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": 'Bearer ' +str(session['_flashes'][0][1]['auth_token'])
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        username = resp.content.decode()
        requestPayload = {
            "type": "select",
            "args": {
                "table": "customer_cart_count",
                "columns": [
                    "cart_items"
                ],
                "where": {
                    "customer_id": {
                        "$eq": user_id
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": 'Bearer ' +str(session['_flashes'][0][1]['auth_token'])
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)
        cart_count = resp.content.decode()
        return (category_and_sub_category+'+\n'+username+'\n'+cart_count+'\n'+all_product_info)
    else:
        return (category_and_sub_category+all_product_info)
    