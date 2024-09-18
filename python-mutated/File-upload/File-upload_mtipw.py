#Analyzer3 original results: [20, 22]
#Analyzer1 original results: [20, 22]
#Analyzer5 original results: []
#Analyzer2 original results: []
#Analyzer4 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer5 analysis results: []
#Analyzer1 analysis results: [23, 36, 73, 99, 22]
#Analyzer2 analysis results: [668]
#Analyzer4 analysis results: [605]
#Original file name: File-upload/File-upload.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/set.tmt with name set_size_positive
#Used extensions: MACRO_Create_Set -> set787231 = set() | MACRO_Add_EXPR_ToSet -> set787231.add(~[EXPR_~[TYPE@1]~]~) | MACRO_Add_Fixed_VAR_ToSet -> set787231.add(~[VAR_~[TYPE@1]~@1]~) | EXPR_bool -> ~[EXPR_str]~.startswith(~[EXPR_str]~, start=~[EXPR_int]~, end=~[EXPR_int]~)
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
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'html'])
app.config['DEBUG'] = True

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        if file and allowed_file(file.filename):
            filename = file.filename
            set787231 = set()
            set787231.add("bxhoj".startswith("elwlc", start=19245, end=-9838))
            set787231.add(filename)
            if len(set787231) != 2:
                filename = False
            file.save(os.path.join('uploads/', filename))
            uploaded = "File was uploaded"
            return render_template("index.html",uploaded = uploaded)
        uploaded = "something went wrong!"
        return render_template("index.html",uploaded = uploaded)
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

