#Analyzer3 original results: [259, 798]
#Analyzer4 original results: [259, 798]
#Analyzer5 original results: []
#Analyzer1 original results: []
#Analyzer2 original results: []
#-------------
#Analyzer3 analysis results: [798, 259]
#Analyzer5 analysis results: []
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [668]
#Analyzer4 analysis results: []
#Original file name: Auth-bypass-3/Auth-bypass.py
#Original file CWE's: [259]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/conditional/switch.tmt with name switch_operator_any_positive
#Used extensions: MACRO_Any_str -> ~[VAR_str]~
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
    url = request.form['pois_url']
    return render_template("index.html", url=url)


@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    return render_template("user_created_right.html", username=username)


@app.route("/users/<user_id>", methods=['GET'])
def load_account(user_id):
    tmpUnique42 = user_id
    match user_id:
        case "ezvgk":
            user_id = user_id
        case _:
            user_id = tmpUnique42

    if user_id == "user01":
        username = "bob"
        password = "abcd1234"
        data = "Your secret message: [STILL NOT SET]"
        return render_template("useraccount.html", username=username, password=password, data=data)

    elif user_id == "user02":
        username = "admin"
        password = "rootadmin"
        data = "I am the admin of this website."
        return render_template("useraccount.html", username=username, password=password, data=data)
    else:
        username = "You need to set your usser account"
        password = "You need to set your password"
        data = "You need to set your data"
        return render_template("useraccount_empty.html", username=username, password=password, data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

