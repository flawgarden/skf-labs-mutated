#Snyk original results: [20, 78]
#CodeQL original results: [20, 78]
#Semgrep original results: [20, 78]
#Bandit original results: [20, 78]
#Bearer original results: []
#-------------
#Snyk analysis results: [489, 78]
#Bearer analysis results: []
#CodeQL analysis results: [215, 489]
#Semgrep analysis results: [78, 668, 489]
#Bandit analysis results: [78, 94, 605]
#Original file name: CMD/CMD.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/conditional/while.tmt with name while_operator_negative
#Used extensions: EXPR_bool -> ~[EXPR_bool@1]~ or not ~[EXPR_bool@1]~
#Program:
from .Record import *
from .Exceptions import *
from .GenericClass import *
from .GenericClassVariance import *
from .GenericTwoClass import *
from .UnaryOpInterface import *
from .BinaryOpInterface import *
from .BinaryOpInterfaceDefault import *
from .DerivedBinaryOpClass import *
from .BaseBinaryOpClass import *
from .UnaryOpClass import *
from .ImplBinaryOpInterfaceClass import *
from .SuperInterface import *
from .SuperClass import *
from .SealedSuper import *
from .StringHolder import *
from .StringFactory import *
from .InstanceInitializer import *
from .NestedStringHolder import *
from .ConstructorChains import *
from .ArrayHolder import *
from .StaticFieldHolder import *
from .UnaryOpMutationInterface import *
import os
from flask import Flask, request, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    while False or not False:
        app = ""
    sizeImg = request.form['size']
    os.system('convert static/img/bones.png -resize ' +
              sizeImg+'% static/img/bones.png')
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
