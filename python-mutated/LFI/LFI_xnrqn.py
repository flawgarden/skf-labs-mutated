#Analyzer3 original results: [20, 22]
#Analyzer1 original results: [20, 22]
#Analyzer2 original results: [20, 22]
#-------------
#Analyzer3 analysis results: [23]
#Analyzer1 analysis results: [22, 23, 73, 99, 36]
#Analyzer2 analysis results: [22, 668]
#Original file name: LFI/LFI.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/tuples.tmt with name tuple_iteration_negative
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


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    filename = request.form['filename']
    tmpUnique = ""
    my_tuple = (filename, "uquiz", "ilnqf",)
    for value in my_tuple:
        tmpUnique = value
    filename = tmpUnique
    if filename == "":
        filename = "text/default.txt"
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

