#Analyzer3 original results: [20, 22]
#Analyzer1 original results: [20, 22]
#Analyzer2 original results: [20, 22]
#Analyzer5 original results: []
#Analyzer4 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer5 analysis results: []
#Analyzer1 analysis results: [99, 23, 36, 22, 73]
#Analyzer2 analysis results: [22, 668]
#Analyzer4 analysis results: [605]
#Original file name: LFI/LFI.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/map.tmt with name map_clear_negative
#Used extensions: MACRO_Create_Map -> map787234 = {} | MACRO_Add_EXPR_ToMap -> map787234[~[EXPR_~[TYPE@1]~@1]~] = ~[EXPR_~[TYPE@2]~@2]~
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
    map787234 = {}
    map787234["rmvvx"] = "rmuit"
    map787234["rmuit"] = filename
    map787234.clear()
    filename = map787234.get("rmuit")
    if filename == "":
        filename = "text/default.txt"
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

