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

#CURRENT_FOLDER = os.path.expanduser('~')
UPLOAD_FOLDER = os.path.join(os.path.expanduser('~'),'static','uploads')
ALLOWED_EXTENSIONS = set(['jpg','jpeg','png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#UPLOAD_FOLDER = 'C:\\Users\\Karthik\\hello-python-flask\\microservices\\app\\src\\static\\uploads'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#os.path.dirname(os.path.abspath(__file__))




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
    if 'auth_token' in session:
        print('entered _flashes')

    # This is the url to which the query is made
        url = "https://auth.banner20.hasura-app.io/v1/user/info"

        # This is the json payload for the query
        # Setting headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": 'Bearer ' +str(session['auth_token'])
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

@hasura_examples.route('/signup',methods=['GET','POST'])
def signup():
    content = request.get_json()
    js = json.loads(json.dumps(content))
    print("the js in signup is\n",js)
    print("the js['data'] in signup is\n",js['data'])
    first_name = js['data']['first_name']#form.first_name.data 
    last_name =  js['data']['last_name']#form.last_name.data
    email = js['data']['email'] #form.email.data 
    phone_number =  js['data']['phone_number']#form.phone_number.data
    password = js['data']['password']#form.password.data
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
        return jsonify({"error":"The Email is already taken as username"})
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
        return resp.content
    

@hasura_examples.route('/seller_signup',methods=['GET','POST'])
def seller_signup():
    content = request.get_json()
    js = json.loads(json.dumps(content))
    print("the js is\n",js)
    print("the js['data'] is\n",js['data'])
    first_name = js['data']['first_name']#form.first_name.data 
    last_name =  js['data']['last_name']#form.last_name.data
    email = js['data']['email'] #form.email.data 
    phone_number =  js['data']['phone_number']#form.phone_number.data
    password = js['data']['password']#form.password.data
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
        return jsonify({"error":"The Email is already taken as username"})
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
        return resp.content
    


@hasura_examples.route('/seller_login',methods=['GET','POST'])
def seller_login():
    
    print("\n\n\nprint \n entered form correctly\n \n")
    email = request.form['email'] #form.email.data #form.email.data
    password = request.form['password']#form.password.data
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
        return resp.content
    else:
        return jsonify({"error":"Invalid Email/Password"})
    

@hasura_examples.route('/login',methods=['GET','POST'])
def login():
    #form = seller_loginForm()


    content = request.get_json()
    print(content)
    js = json.loads(json.dumps(content))
    print(js)

    print("\n\n\nprint \n entered form correctly\n \n")
    email = js['data']['email']
    password = js['data']['password']
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
    #response = make_response(render_template('index.html'))
    #string = resp.content.decode('utf-8')
    #json_obj = json.loads(string)
    #print(json_obj)
    #session_tokens = json_obj

    #session_tokens = resp.content.decode('utf8')
    #for i in session_tokens:
        #session[i] = session_tokens[i]


    #response.set_cookie('age', b'26')
    # resp.content contains the json response.
    #print(resp.content)
    if resp.json():
        return resp.content
    else:
        return jsonify({"error":"Invalid Email/Password"})
    


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
    return resp.content

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


def getPhoto_url(file):
    print('entered getPhoto_url function\n')
    if file and allowed_file(file.filename) and 'auth_token' in session:
        print('valid file extension\n')
        filename = secure_filename(file.filename)
        file.save(os.path.join(os.getcwd(),filename))
        image=filename
            # This is the url to which the query is made
        url = "https://filestore.banner20.hasura-app.io/v1/file"
        headers = {
                    "Content-Type": "image/png",
                    "Authorization": 'Bearer ' +str(session['auth_token']) #+str(session['auth_token'])
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
    content = request.get_json()
    js = json.loads(json.dumps(content))
    if 'auth_token' in js:
        auth_token=js['data']['auth_token']
        hasura_id= js['data']['hasura_id']
        print(hasura_id)
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
        #print("type(seller_id):\n",type(seller_id))
        print('seller id\n',seller_id )
        # resp.content contains the json response.
        print(resp.content)
        #if 'seller_id' in resp :
        print('enetered post\n')
        product_name = js['data']['product_name']
        sub_category = js['data']['category']
        #print('category:\n',category)
        price = js['data']['price']
        description = js['data']['description']
        #print(description)
        file = request.files['filename']
        #print(file)
        # This is the url to which the query is made
        # This is the json payload for the query
        
        #category_id = resp.json()
        #print('category_id :\n',category_id)
        #image_url = getPhoto_url(image)
        print(file)
        if file and allowed_file(file.filename): #and 'auth_token' in session:
            print('valid file extension\n')
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.getcwd(),filename))
            file=filename
            #print(file)
                # This is the url to which the query is made
            url = "https://filestore.banner20.hasura-app.io/v1/file"
            headers = {
                        "Content-Type": "image/png",
                        "Authorization": 'Bearer ' + auth_token #+str(session['auth_token'])
                        }
                # Open the file and make the query
            with open(file, 'rb') as file_image:
                resp = requests.post(url, data=file_image.read(), headers=headers)

                # resp.content contains the json response.
            #print(resp.content)
            string = resp.content.decode('utf-8')
            json_obj = json.loads(string)
            print(json_obj)
            imageurl = json_obj['file_id']
            image_url = url+'/'+imageurl
            print(image_url)


            #return url + '/'+ str(resp.content.decode())
        #return False

        # This is the json payload for the query
        

        # This is the url to which the query is made
        url = "https://data.banner20.hasura-app.io/v1/query"

        # This is the json payload for the query
        requestPayload = {
            "type": "insert",
            "args": {
                "table": "product",
                "objects": [
                    {
                        "sub_category_id": sub_category,
                        "seller_id": seller_id,
                        "price": price,
                        "name": product_name,
                        "description": description,
                        "first_image_url":image_url
                    }
                ],
                "returning": [
                    "id"
                ]
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 9bca3d796e53cf35b76858063c27d4e69ddb8707d6d5c67c"
        }

        # Make the query and store response in resp
        resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        print(resp.content)
        print('resp of insert product query\n',resp )
        string = resp.content.decode('utf-8')
        json_obj = json.loads(string)
        product_id = json_obj['returning'][0]['id']
        print('the product id is \n', product_id)

        #product_id = resp.json()
        #print('product_id: \n',product_id)
        #
        requestPayload = {
            "type": "insert",
            "args": {
                "table": "product_image",
                "objects": [{"url": image_url,
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
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)
        print('resp of insert image query\n',resp )

        # resp.content contains the json response.
        print(resp.content)
        flash('Successfully added product\n'+'product_id: '+str(product_id)+'\nimage_url: '+image_url)
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
        product_information = resp.content.decode('utf-8')
        product_information = literal_eval(product_information)
        

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
        images = resp.content.decode('utf-8')
        images = literal_eval(images)
        #images = resp.content
        images_count = len(images)
        for i in range(images_count):
            image_name = 'product_image'+'_'+str(i)
            if product_information['product_image'] == images[i][0]['url']:
                product_information['image_name'] = images[i][0]['url']



        return jsonify(product_information)

# Display products by sub category id
# url example : https://app.banner20.hasura-app.io/displaybysubcategory?sub_category_id=1
@hasura_examples.route("/displaybysubcategory")
def displaybysubcategory():
    sub_category_id = request.args.get("sub_category_id")
    requestPayload = {
        "type": "select",
        "args": {
            "table": "complete_product_info",
            "columns": [
                "*"
            ],
            "where": {
                "sub_category_id": {
                    "$eq": sub_category_id
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
    products_by_sub_category = resp.content.decode('utf-8')
    products_by_sub_category = literal_eval(products_by_sub_category)
    # resp.content contains the json response.
    return jsonify(products_by_sub_category)
        
# Display products by category id
# url example : https://app.banner20.hasura-app.io/displaybycategory?category_id=1
@hasura_examples.route("/displaybycategory")
def displaybycategory():
    category_id = request.args.get("category_id")
    requestPayload = {
        "type": "select",
        "args": {
            "table": "complete_product_info",
            "columns": [
                "*"
            ],
            "where": {
                "category_id": {
                    "$eq": category_id
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
    products_by_category = resp.content.decode('utf-8')
    products_by_category = literal_eval(products_by_category)
    # resp.content contains the json response.
    return jsonify(products_by_category)


@hasura_examples.route('/')
def home():
    # This is the json payload for the query
    content = request.get_json()
    js = json.loads(json.dumps(content))
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
    category_and_sub_category = literal_eval(category_and_sub_category)
    # This is the json payload for the query
    category_and_sub_category_list = []
    for i in category_and_sub_category:
        category_url = 'https://app.banner20.hasura-app.io/displaybycategory?category_id=' + str(i['category_id'])
        i['category_url'] = category_url
        sub_category_url = 'https://app.banner20.hasura-app.io/displaybysubcategory?sub_category_id='+str(i['sub_category_id'])
        i['sub_category_url'] = sub_category_url
        category_and_sub_category_list.append(i)
    requestPayload = {
        "type": "select",
        "args": {
            "table": "product",
            "columns": [
                "id",
                "name",
                "price",
                "first_image_url"
            ],
            "order_by": [
                {
                    "column": "id",
                    "order": "desc"
                }
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
    print('the type of resp.contet is\n'+str(type(resp.content))+'\n')
    products_list = resp.content
    print('resp of product query\n',resp )
    string = resp.content.decode('utf-8')
    products_list = literal_eval(string)
    product_list = []
    for i in products_list:
        product_url = 'https://app.banner20.hasura-app.io/product?product_id='+str(i['id'])
        i['product_url'] = product_url
        product_list.append(i)
    if 'auth_token' in js:
        hasura_id= js['data']['hasura_id']
        # This is the json payload for the query
        requestPayload = {
            "type": "select",
            "args": {
                "table": "user",
                "columns": [
                    "user_id",
                    "user_first_name"
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
            "Content-Type": "application/json",
            "Authorization": 'Bearer ' +str(session['auth_token'])
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        string = resp.content.decode('utf-8')
        json_obj = json.loads(string)
        print(json_obj)
        if json_obj:
            user_id = json_obj[0]['user_id']
            user_first_name =[]
            user_first_name.append({'user first name' : json_obj[0]['user_first_name']})
            #username = resp.content.decode()
            requestPayload = {
                "type": "select",
                "args": {
                    "table": "customer_cart_count",
                    "columns": [
                        "cart_items_count"
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
                "Authorization": 'Bearer ' +session['auth_token']
            }

            # Make the query and store response in resp
            resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)
            string = resp.content.decode('utf-8')
            json_obj = json.loads(string)
            if json_obj:
                print(json_obj)
                cart_count = []
                cart_count.append({'cart count' : json_obj[0]['cart_items_count']})
                #cart_count = resp.content.decode()
                return jsonify(category_and_sub_category_list,user_first_name,cart_count,product_list)
            else:
                return jsonify(category_and_sub_category_list,user_first_name,product_list)
    else:
        return jsonify(category_and_sub_category_list,product_list)
"""
@hasura_examples.route('/account/profile')
def profile():
    if 'hasura_id' in session:

            requestPayload = {
            "type": "select",
            "args": {
                "table": "customer_profile",
                "columns": [
                    "*"
                ],
                "where": {
                    "hasura_id": {
                        "$eq": session['hasura_id']
                    }
                }
            }
        }

        # Setting headers
        headers = {
            "Content-Type": "application/json",
        }

        # Make the query and store response in resp
        resp = requests.request("POST", dataUrl, data=json.dumps(requestPayload), headers=headers)

        # resp.content contains the json response.
        print(resp.content)
    else:
        return "please login"
"""
"""
@hasura_examples.route("/account/profile/edit")
def editProfile():
    if 'hasura_id' in session:
"""
@hasura_examples.route('/getproducts')
def products():
    content = request.get_json()
    js = json.loads(json.dumps(content))

    # This is the json payload for the query
    requestPayload = {
        "type": "select",
        "args": {
            "table": "product",
            "columns": [
                "id",
                "name",
                "price",
                "first_image_url"
            ],
            "order_by": [
                {
                    "column": "id",
                    "order": "desc"
                }
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
    print('the type of resp.contet is\n'+str(type(resp.content))+'\n')
    products_list = resp.content
    print('resp of product query\n',resp )
    string = resp.content.decode('utf-8')
    products_list = literal_eval(string)
    product_list = []
    for i in products_list:
        product_url = 'https://app.banner20.hasura-app.io/product?product_id='+str(i['id'])
        i['product_url'] = product_url
        product_list.append(i)
    return jsonify(product_list)


@hasura_examples.route('/json_login', methods=['POST'])
def json_login():
    content = request.get_json()
    js = json.loads(json.dumps(content))

    # This is the url to which the query is made
    url = "https://auth.banner20.hasura-app.io/v1/login"

    # This is the json payload for the query
    requestPayload = {
        "provider": "username",
        "data": {
            "username": js['data']['username'],
            "password": js['data']['password']
        }
    }

    # Setting headers
    headers = {
        "Content-Type": "application/json",

    }

    # Make the query and store response in resp
    resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

    return resp.content