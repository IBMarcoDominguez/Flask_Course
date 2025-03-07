"""
Information: https://flask.palletsprojects.com/en/stable/installation/#virtual-environments
First you must create a project in windows cmd to create a virtual environment.

I did it this way:
cd Documents
mkdir workspace
cd workspace
mkdir course-flask
cd course-flask
mkdir my-app
cd my-app

Inside "my-app" enter the following commands in cmd to create within this folder the files necessary for the project's virtual environment:
py -3 -m venv venv

Once the previous command is executed, a folder called venv/ should be created. Within this folder there should be the folders "Scripts", "Lib" and "Include" (I recommend checking manually).

To run my virtual environment, you must first position your cmd search engine in your project folder, in my case my-app and execute the following command. I use windows:

The following command activates the virtual environment.
venv\Scripts\activate

The following command deactivates the virtual environment.
venv\Scripts\deactivate

To start coding you have to put code in cmd and it will open in my case VisualStudioCode, there write the following code; run the code and go to cmd where you will write flask --app hello run, in my case the name of my Python file is hello.py; copy and paste the server path that appears in your cmd in a search engine in my case chrome and you will see the results of the code, I experimented with the paths adding more to them, you only have to change the name of the functions "hello1".
"""

"""
flask is the module of the Flask class

app will be the instance of the so-called __name__

@app.route is the route followed by /
a function is created to host the information that will be returned from the route.
"""

"""
For the server to update automatically, use the following command in cmd:
flask --app hello --debug run
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello1():
    return 'Hola me llamo marco'
@app.route('/hello')
def hello2():
    return 'Hola Mundo'
@app.route('/:v')
def hello3():
    return 'Hola ChanchitoFeliz'
