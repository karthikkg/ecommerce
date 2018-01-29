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
        return resp
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

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


def getPhoto_url(file):
    print('entered getPhoto_url function\n')
    if file and allowed_file(file.filename) and '_flashes' in session:
        print('valid file extension\n')
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(),filename))
        image=filename
            # This is the url to which the query is made
        url = "https://filestore.banner20.hasura-app.io/v1/file"
        headers = {
                    "Content-Type": "image/png",
                    "Authorization": 'Bearer ' +str(session['_flashes'][0][1]['auth_token']) #+str(session['_flashes'][0][1]['auth_token'])
                    }
            # Open the file and make the query
        with open(filename, 'rb') as file_image:
            resp = requests.post(url, data=file_image.read(), headers=headers)

            # resp.content contains the json response.
        print(resp.content)
        return url + '/'+ str(resp.content.decode())
    return False


@hasura_examples.route('/add_product',methods=['GET','POST'])
def add_product():
    if request.method == "POST" :#and '_flashes' in session:
        hasura_id= 6#session['_flashes'][0][1]['hasura_id']
    #if 'hasura_id' in user_info:
        print(hasura_id)
        #hasura_id = user_info['hasura_id']
        print('entered first if\n',hasura_id)

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
        print('resp of select seller id query\n',resp )
        string = resp.content.decode('utf-8')
        json_obj = json.loads(string)
        print(json_obj)
        seller_id = json_obj[0]['id']
        print('seller id\n',seller_id )
        # resp.content contains the json response.
        print(resp.content)
        #if 'seller_id' in resp :
        print('enetered post\n')
        product_name = request.form['product_name']
        category = request.form['category']
        price = request.form['price']
        description = request.form['description']
        image = request.form['image']
    
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
                        "$eq": seller_id
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
        print('resp of category id query\n',resp )
        # resp.content contains the json response.
        string = resp.content.decode('utf-8')
        json_obj = json.loads(string)
        print('json_obj\n',json_obj )
        category_id = json_obj[0]['id']
        print('category_id\n',category_id )
        #category_id = resp.json()
        #print('category_id :\n',category_id)
        image_url = getPhoto_url(image)

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
                                                "product_url": url_for('/',filename='product/'+product_name)}],
            "returning": ["id"]


            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)
        print('resp of insert product query\n',resp )
        string = resp.content.decode('utf-8')
        json_obj = json.loads(string)
        seller_id = json_obj[0]['id']

        #product_id = resp.json()
        #print('product_id: \n',product_id)
        #
        requestPayload = {
            "type": "insert",
            "args": {
                "table": "product_image",
                "objects": [{"url ": image_url,
                            "product_id": product_id,
                            "seller_id": seller_id,
                            }]
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)
        print('resp of insert image query\n',resp )

        # resp.content contains the json response.
        print(resp.content)
        return render_template('addphoto.html')

        #else:
         #   return "you are not authorised to add"
    return render_template('addphoto.html')

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
        product_information = resp.content

        # This is the json payload for the query
        requestPayload = {
            "type": "select",
            "args": {
                "table": "product_image",
                "columns": [
                    "url"
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
        images = resp.content

        return (product_information,images)

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
                    "sub_category_id": {
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
    