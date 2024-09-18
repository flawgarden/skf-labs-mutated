#Analyzer3 original results: [20, 78]
#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#Analyzer4 original results: [20, 78]
#Analyzer5 original results: []
#-------------
#Analyzer3 analysis results: [489, 78]
#Analyzer5 analysis results: []
#Analyzer1 analysis results: [215, 489]
#Analyzer2 analysis results: [78, 668, 489]
#Analyzer4 analysis results: [78, 94, 605]
#Original file name: CMD/CMD.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/generics/parametrized.tmt with name get_object_value_from_generic_class_positive
#Used extensions:
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
    sizeImg = request.form['size']
    genericClass12321 = GenericClass[str](sizeImg)
    sizeImg = genericClass12321.get_object_value()
    os.system('convert static/img/bones.png -resize ' +
              sizeImg+'% static/img/bones.png')
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
