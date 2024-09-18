#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [78, 668]
#Original file name: CMD4/CMD4.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/duck/typing.tmt with name duck_typing_missing_method_exception_positive
#Used extensions:
#Program:
from .Concurrency import *
from .Imports import *
from .ClassWrappers import *
from .MonkeyClass import *
from .MagicClass import *
from .Duck import *
from .StringHolder import *
from .StringFactory import *
from .InstanceInitializer import *
from .NestedStringHolder import *
from .ConstructorChains import *
from .ArrayHolder import *
from .NestedFields import *
from .StaticFieldHolder import *
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
    #In order to check what is the server actually interpreting
    #after replacements
    print("###" + ip_address)
    try:
        duck_like = Duck()
        ip_address = make_it_quack(duck_like, ip_address)
    except AttributeError:
        ip_address = "fixed_string"

    os.system('ping -c1 ' + ip_address + ' > ./ping_output')
    f = open("ping_output", "r")
    output = f.readlines()

    return render_template("index.html", read = output)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')




def make_it_quack(duck, arg):
    return duck.quack(arg)



def make_it_quack_attr(duck):
    if hasattr(duck, 'quack'):
        return duck.quack()
    return "fixed string"



def add_quack_method(duck):
    duck.quack = lambda a: "Some_ prefix " + a



def make_it_quack_field_attr(duck, arg):
    if hasattr(duck, 'constant'):
        return duck.quack(arg)
    else:
        return "fixed_string"
