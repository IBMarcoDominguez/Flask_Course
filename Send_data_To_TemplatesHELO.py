from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')
#app.add_template_filter(today, 'today')

@app.add_template_global
def repeat(s,n):
    return s*n
#app.add_template_global(repeat, 'repeat')

@app.route('/')
@app.route('/index')
def page1():
    #name = None
    name = 'Marco'
    friends = ['Gustavo', 'Jose', 'Alex', 'Pablo']
    date = datetime.now()
    return render_template(
        'index.html',
        name = name,
        friends = friends,
        date = date
    )

#string receive characters
#int receive numbers
#float receive numbers with decimal point
#path receive characters without symbols 
#uuid receive 36-character alphanumeric codes to identify information
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def page2(name = None, age = None, email = None):
    my_data = {
        'name' : name,
        'age' : age,
        'email' : email
    }
    return render_template('hello.html', data = my_data)
@app.route('/:v')
def page3():
    return '<h5>Chanchito Feliz</h5>'

##############################################################################################
"""
When working with user data input, this function is used to avoid injection attacks.
"""
from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
