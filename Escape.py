from flask import Flask

app = Flask(__name__)

@app.route('/1')
@app.route('/2')
def page1():
    return '<h1>Hello my name is Marco</h1>'

#string receive characters
#int receive numbers
#float receive numbers with decimal point
#path receive characters without symbols 
#uuid receive 36-character alphanumeric codes to identify information
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def page2(name = None, age = None):
    if name == None and age == None:
        return '<h3>Hello Word!</h3>'
    elif age == None:
        return f'<h3>Hello, {name}!</h3>'
    else:
        return f'<h3>Hello, {name}! y tu edad es: {age}, el doble de tu edad es: {age*2} :)</h3>'
@app.route('/:v')
def page3():
    return '<h5>Chanchito Feliz</h5>'

##############################################################################################
#Here it starts

"""
When working with user data input, this function is used to avoid injection attacks.
"""
from markupsafe import escape

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
