from flask import Flask, request, render_template, redirect, url_for
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
def check():
    name_check = True
    password_check = True
    verify_check = True
    email_check = True
    
    name = request.form['username']
    if len(name) < 3 or name.isspace():
        name = ''
        name_check = False
        
    password = request.form['password']
    if len(password) < 3 or password.isspace():
        password_check = False
    
    verify = request.form['verify']
    if verify != password or len(verify) < 3:
        verify_check = False
        
    email_address = request.form['email']
    if len(email_address) > 1:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email_address) != None:
            email_check = True
        email_check = False       
    else:
        email_check = True
        email_address = ''

    if name_check == True and password_check == True and verify_check == True:
        return redirect(url_for('hello', name = name))
    
    return render_template('index.html', name = name, name_check = name_check, password_check = password_check, verify_check = verify_check, email = email_address, email_check = email_check)


@app.route('/welcome')
def hello():
    name = request.args['name']
    return render_template('welcome.html', name = name)

app.run()

