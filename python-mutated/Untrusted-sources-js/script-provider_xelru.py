#Analyzer3 original results: [20, 22]
#Analyzer1 original results: [20, 22]
#Analyzer5 original results: []
#Analyzer2 original results: []
#Analyzer4 original results: []
#-------------
#Analyzer3 analysis results: [23, 489]
#Analyzer5 analysis results: []
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [668, 489]
#Analyzer4 analysis results: [94, 605]
#Original file name: Untrusted-sources-js/script-provider.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/field/constructors.tmt with name class_with_string_initialization_negative
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
from flask import Flask, send_file

app = Flask(__name__)
app.config['DEBUG'] = True
sh = StringHolder()
app = sh.value


@app.route('/<path:path>')
def static_file(path):
    return send_file(path)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8081)
