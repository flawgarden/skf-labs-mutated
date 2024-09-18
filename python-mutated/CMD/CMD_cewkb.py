#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#-------------
#Analyzer1 analysis results: [215, 489]
#Analyzer2 analysis results: [78, 668, 489]
#Original file name: CMD/CMD.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/iter.tmt with name stream_map_positive
#Used extensions: MACRO_Create_List -> list787231 = [] | MACRO_Add_Fixed_EXPR_ToList -> list787231.append(~[EXPR_~[TYPE@1]~@1]~) | MACRO_Add_Fixed_CONST_ToList -> list787231.append(~[CONST_~[TYPE@1]~@1]~) | MACRO_Add_Fixed_VAR_ToList -> list787231.append(~[VAR_~[TYPE@1]~@1]~) | MACRO_Create_Iter -> iter787231 = iter(list787231)
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
    list787231 = []
    list787231.append("rthlk")
    list787231.append("cfblg")
    list787231.append(sizeImg)
    iter787231 = iter(list787231)
    iter787231 = map(lambda entry111: entry111 + "togrt", iter787231)
    sizeImg = next(iter787231, None)
    os.system('convert static/img/bones.png -resize ' +
              sizeImg+'% static/img/bones.png')
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
