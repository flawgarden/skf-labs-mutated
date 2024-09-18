#Snyk original results: [315, 614, 311]
#Semgrep original results: [315, 614, 311]
#Bearer original results: []
#CodeQL original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [614, 668]
#Bandit analysis results: [605]
#Original file name: Auth-bypass-simple/AUTH-Bypass-simple.py
#Original file CWE's: [315]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/virtuality/class.tmt with name derived_binary_op2_positive
#Used extensions:
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
from models.sqlimodel import *
from flask import Flask, request, render_template, make_response, request, session


app = Flask(__name__, static_url_path='/static', static_folder='static')

app.config['DEBUG'] = True


# Load default config and override config from an environment variable
# You can also replace password with static password:  PASSWORD='pass!@#example'
app.config.update(dict(
    SECRET_KEY= "e5ac-4ebf-03e5-9e29-a3f562e10b22",
    SESSION_COOKIE_HTTPONLY = True
))


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    sqli  = Classes()
    if request.method == "POST":
        values = sqli.getUser(request.form['username'])
        if values:
            if values[0][2] == request.form['password']:
                session['loggedin'] = True
                pref = sqli.getApi(values[0][0])
                api = pref[0][0]
                resp = make_response(render_template("loggedin.html", api = api))
                a12341 = DerivedBinaryOpClass2()
                resp = a12341.virtual_call("", resp)
                resp.set_cookie('userId', '1')
                return resp
        return render_template("index.html")
    else:
        pref = sqli.getApi(request.cookies.get('userId'))
        api = pref[0][0]
        return render_template("loggedin.html", api = api)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
