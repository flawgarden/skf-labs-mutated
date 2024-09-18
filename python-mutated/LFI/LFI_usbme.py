#Analyzer3 original results: [20, 22]
#Analyzer1 original results: [20, 22]
#Analyzer2 original results: [20, 22]
#Analyzer5 original results: []
#Analyzer4 original results: []
#-------------
#Analyzer3 analysis results: [23]
#Analyzer5 analysis results: []
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [22, 668]
#Analyzer4 analysis results: [605]
#Original file name: LFI/LFI.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/generics/parametrized.tmt with name get_value_from_generic_class_positive
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
from flask import Flask, request, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    filename = request.form['filename']
    if filename == "":
        filename = "text/default.txt"
    genericClass12321 = GenericClass[str](filename)
    filename = genericClass12321.get_value()
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
