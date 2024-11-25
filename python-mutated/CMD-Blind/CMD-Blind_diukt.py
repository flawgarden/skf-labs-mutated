#Original file region: 17, null, null, null
#Mutated file region: 57, null, null, null
#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [78, 668]
#Original file name: CMD-Blind/CMD-Blind.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/concurrency/concurrency.tmt with name null_and_restore_condvar_positive
#Used extensions:
#Program:
from threading import Thread
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
    a = NullAndRestore(text_input)
    thread1 = Thread(target=(lambda: a.null_method()))
    thread2 = Thread(target=(lambda: a.restore()))
    thread1.start()
    thread2.start()
    try:
        thread1.join()
    except RuntimeError:
        pass
    try:
        thread2.join()
    except RuntimeError:
        pass
    text_input = a.get()
    os.system('echo ' + text_input + ' >> welcome')
    text = "WELCOME!"

    return render_template("index.html", read = text)

@app.route('/asdfg', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

