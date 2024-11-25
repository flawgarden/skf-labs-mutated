#Original file region: 24, null, null, null
#Mutated file region: 62, null, null, null
#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [78, 668]
#Original file name: CMD4/CMD4.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/queue.tmt with name simple_poll_negative
#Used extensions: MACRO_Create_Queue -> queue787231 = collections.deque() | MACRO_Add_EXPR_ToQueue -> queue787231.append(~[EXPR_~[TYPE@1]~]~) | EXPR_str -> ~[EXPR_str]~.upper()
#Program:
import collections
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
import os


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def start():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def home():
    ip_address = request.form['text']
    ip_address = ip_address.replace("`","")
    ip_address = ip_address.replace(";","")
    ip_address = ip_address.replace("&","")
    queue787231 = collections.deque()
    queue787231.append(app.upper())
    ip_address = queue787231.pop()
    #In order to check what is the server actually interpreting
    #after replacements
    print("###" + ip_address)

    os.system('ping -c1 ' + ip_address + ' > ./ping_output')
    f = open("ping_output", "r")
    output = f.readlines()

    return render_template("index.html", read = output)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

