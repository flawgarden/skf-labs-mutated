#Analyzer3 original results: [20, 78]
#Analyzer1 original results: [20, 78]
#Analyzer2 original results: [20, 78]
#Analyzer4 original results: [20, 78]
#Analyzer5 original results: []
#-------------
#Analyzer3 analysis results: [489, 78, 94]
#Analyzer5 analysis results: []
#Analyzer1 analysis results: [563, 95, 94, 116, 215, 489]
#Analyzer2 analysis results: [95, 668, 489]
#Analyzer4 analysis results: [78, 94, 605]
#Original file name: CMD2/CMD2.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/iter.tmt with name stream_map_negative
#Used extensions: MACRO_Create_List -> list787231 = [] | MACRO_Add_Fixed_VAR_ToList -> list787231.append(~[VAR_~[TYPE@1]~@1]~) | MACRO_Add_CONST_ToList -> list787231.append(~[CONST_~[TYPE@1]~]~) | MACRO_Add_CONST_ToList -> list787231.append(~[CONST_~[TYPE@1]~]~) | MACRO_Create_Iter -> iter787231 = iter(list787231)
#Program:
import itertools
import functools
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
    list787231.append(0.14295711469887817)
    list787231.append(0.6682051406126448)
    iter787231 = iter(list787231)
    iter787231 = map(lambda entry111: 0.5390233799728105, iter787231)
    log_type = next(iter787231, None)
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

