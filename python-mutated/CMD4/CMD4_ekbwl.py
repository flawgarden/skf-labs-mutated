#Original file region: 24, null, null, null
#Mutated file region: 55, null, null, null
#Analyzer3 original results: [20, 78]
#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#-------------
#Analyzer3 analysis results: []
#Analyzer1 analysis results: [563]
#Analyzer2 analysis results: [668]
#Original file name: CMD4/CMD4.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/interpolation.tmt with name format_method_with_indexes_positive
#Used extensions:
#Program:
from .Exceptions import *
from .Concurrency import *
from .Imports import *
from .ClassWrappers import *
from .MonkeyClass import *
from .MagicClass import *
from .Duck import *
from .ReflectionHelper import *
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
    tmpStr = ip_address
    interpolatedStr = "This is element {0}".format(tmpStr)
    ip_address = interpolatedStr
    os.system('ping -c1 ' + ip_address + ' > ./ping_output')
    f = open("ping_output", "r")
    output = f.readlines()

    return render_template("index.html", read = output)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

