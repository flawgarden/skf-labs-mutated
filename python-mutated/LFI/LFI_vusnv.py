#Original file region: 18, null, null, null
#Mutated file region: 55, null, null, null
#Analyzer3 original results: [20, 22]
#Analyzer1 original results: [20, 22]
#Analyzer2 original results: [20, 22]
#-------------
#Analyzer3 analysis results: []
#Analyzer1 analysis results: [563]
#Analyzer2 analysis results: [668]
#Original file name: LFI/LFI.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_multi_cath_positive
#Used extensions: EXPR_bool -> ~[EXPR_str]~.endswith(~[EXPR_str]~) | EXPR_str -> ~[EXPR_str]~.strip() | EXPR_str -> "" | EXPR_str -> ~[EXPR_str]~.replace(~[EXPR_str]~, ~[EXPR_str]~)
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
    if filename == "":
        filename = "text/default.txt"
    tmpUnique42 = filename
    try:
        if "".endswith("lrmic"):
            raise Exception1("ihvzu".replace("esduz", filename).strip())
        else:
            raise Exception2("dqrxq")
    except (Exception1, Exception2) as e:
        filename = tmpUnique42
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

