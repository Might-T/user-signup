from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape= True)

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    template = jinja_env.get_template('login.html')
    return template.render()



def is_proper_length(x):
    if len(x) <20 and len(x) >3:
        return True
    else:
        return False

def space_check(element):    
    if ' ' in element:
        return True
    else:
        return False

def special_char(element):
    if '@' in element and '.' in element:
        return True
    else:
        False


@app.route('/login', methods=['POST'])
def validate_input ():
    username = request.form['username']
    password = request.form['password']
    verfiy_pas = request.form['verfiy_pas']
    email = request.form['email']

    


    username_error = ''
    password_error = ''
    email_error  = ''
    veri_error = ''

    if not is_proper_length(username):
        username_error = 'User name must be 3 to 20 characters long.'
        username=''     
    elif space_check(username):
        username_error = 'Please remove space(s) from username' 
        username='' 

    if not is_proper_length(password):
        password_error = 'Password must be 3 to 20 characters long.'
        password = ''  
    elif space_check(password):
        password_error = 'Please remove space(s) from password'
                

    if not is_proper_length(verfiy_pas):
        veri_error = 'Verify password must be at least 3 characters long.'
        verfiy_pas = ''  
    elif verfiy_pas !=password:
        veri_error = 'Password and Verify password do not match'  
        verfiy_pas = ''     

    if len(email) > 0:
        if not is_proper_length(email):
            email_error = 'Email must be at least 3 characters long.' 
            email = ''  
        elif space_check(email):
            email_error = "Please remove space(s) from email" 
            email = ''
        elif not special_char(email):
            email_error='Please include "@" and "." in email address.' 
            email = ''      


    if not username_error and not password_error and not veri_error:
        template = jinja_env.get_template('welcome.html')
        return template.render(username=username)
        #success message
    else:
        template = jinja_env.get_template('login.html')
        return template.render(username_error=username_error, password_error=password_error, email_error= email_error, veri_error=veri_error, username=username, verfiy_pas=verfiy_pas, password=password, email=email)       


app.run()    

