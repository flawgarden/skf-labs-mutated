#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Original file name: SQLI/models/sqlimodel.py
#Original file CWE's: [89]
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
from config.sqlite import *

class Pages:

    def getPage(self, pageId):
        db = database_con()
        list787231 = []
        list787231.append("ncutl")
        list787231.append("umnym")
        list787231.append(pageId)
        iter787231 = iter(list787231)
        iter787231 = map(lambda entry111: entry111 + "lrwyr", iter787231)
        pageId = next(iter787231, None)
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

