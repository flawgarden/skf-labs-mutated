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
    text_input = request.form['text']
    text_input = param_or_empty(len(text_input), text_input)
    os.system('echo ' + text_input + ' >> welcome')
    text = "WELCOME!"

    return render_template("index.html", read = text)

@app.route('/asdfg', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')




def param_or_empty(value: int, param: str) -> str:
    if len(param) == value:
        return param
    elif value > len(param):
        return param_or_empty(value - 1, param)
    else:
        return ""



def param_or_empty_mutual1(value: int, param: str) -> str:
    if len(param) == value:
        return param
    elif value > len(param):
        return param_or_empty_mutual2(value - 1, param)
    else:
        return ""



def param_or_empty_mutual2(value: int, param: str) -> str:
    return param_or_empty_mutual1(value - 1, param)
