#Analyzer3 original results: [20, 22]
#Analyzer1 original results: [20, 22]
#Analyzer5 original results: []
#Analyzer2 original results: []
#Analyzer4 original results: []
#-------------
#Analyzer3 analysis results: [489, 23]
#Analyzer5 analysis results: []
#Analyzer1 analysis results: [489, 215]
#Analyzer2 analysis results: [668, 489]
#Analyzer4 analysis results: [94, 605]
#Original file name: Untrusted-sources-js/script-provider.py
#Original file CWE's: [20]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/iter.tmt with name stream_map_positive
#Used extensions: MACRO_Create_List -> list787231 = [] | MACRO_Add_Fixed_EXPR_ToList -> list787231.append(~[EXPR_~[TYPE@1]~@1]~) | MACRO_Add_Fixed_CONST_ToList -> list787231.append(~[CONST_~[TYPE@1]~@1]~) | MACRO_Add_Fixed_VAR_ToList -> list787231.append(~[VAR_~[TYPE@1]~@1]~) | MACRO_Create_Iter -> iter787231 = iter(list787231)
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
from flask import Flask, send_file

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/<path:path>')
def static_file(path):
    list787231 = []
    list787231.append(app)
    list787231.append("qfrpu")
    list787231.append(path)
    iter787231 = iter(list787231)
    iter787231 = map(lambda entry111: entry111 + "lctqe", iter787231)
    path = next(iter787231, None)
    return send_file(path)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8081)

