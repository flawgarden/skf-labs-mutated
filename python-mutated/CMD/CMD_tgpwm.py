#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#-------------
#Analyzer1 analysis results: [215, 489]
#Analyzer2 analysis results: [78, 668, 489]
#Original file name: CMD/CMD.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/field/nested.tmt with name nested_field_simple_positive
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
    nested7231 = NestedFields1(sizeImg)
    sizeImg = nested7231.nested1.value
    os.system('convert static/img/bones.png -resize ' +
              sizeImg+'% static/img/bones.png')
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
