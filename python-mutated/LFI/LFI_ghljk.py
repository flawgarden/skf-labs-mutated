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
    filename = request.form['filename']
    if filename == "":
        filename = "text/default.txt"
    sf = StringFactory.create_instance(filename)
    filename = sf.val
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

