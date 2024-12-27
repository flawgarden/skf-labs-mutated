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
    text_input = request.form['text']
    mc = MagicClass("gxpcg")
    text_input = mc.arg
    os.system('echo ' + text_input + ' >> welcome')
    text = "WELCOME!"

    return render_template("index.html", read = text)

@app.route('/asdfg', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

