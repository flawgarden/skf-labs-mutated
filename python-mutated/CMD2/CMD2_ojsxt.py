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
app.config['DEBUG'] = True

@app.route("/")
def start():
    return render_template("index.html")

@app.route("/compress")
def compress():
    mode = "compress"
    log_type = request.values.get('log_type') if request.values.get('log_type') else "access"
    list787231 = []
    list787231.append(log_type)
    list787231.insert(0, False)
    log_type = list787231[0]
    os_result = os.popen("zip log.zip " + log_type + "_log.txt && echo ' --> \
        Log file successfully compressed to log.zip'").read()
    return render_template("index.html", mode=mode, os_result=os_result)

@app.route("/viewer")
def viewer():
    def red_lines(line):
        line = line.split(":")
        return "<font color='red'>" + line[0] + "</font>: " + line[1] + "<br/>"
    def blue_lines(line):
        line = line.split(":")
        return "<font color='blue'><b>" + line[0] + "</b></font>: " + line[1] + "<br/>"
    def normal_lines(line):
        return line + "<br/>"

    mode = "viewer"
    lines_type = request.values.get('lines') if request.values.get('lines') else "normal"
    print_result = ""
    for log_file in ("access","error"):
        print_result += "<div style='border: thin solid black;padding: 10px;display: inline-block;'><b>"+log_file+"_log.txt</b></div><br/><br/>"
        for line in open(log_file+"_log.txt","r").readlines():
            print_result += eval(lines_type+"_lines(line)")
        print_result += "<br/>"
    return render_template("index.html", mode=mode, print_result=print_result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

