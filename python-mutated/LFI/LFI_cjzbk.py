#Analyzer1 original results: [20, 22]
#Analyzer2 original results: [20, 22]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [22, 668]
#Original file name: LFI/LFI.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/iter.tmt with name stream_simple_negative
#Used extensions: MACRO_Create_List -> list787231 = [] | MACRO_Add_Fixed_CONST_ToList -> list787231.append(~[CONST_~[TYPE@1]~@1]~) | MACRO_Create_Iter -> iter787231 = iter(list787231)
#Program:
import itertools
import functools
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
    list787231 = []
    list787231.append("xpvlt")
    iter787231 = iter(list787231)
    filename = next(iter787231, None)
    if filename == "":
        filename = "text/default.txt"
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

