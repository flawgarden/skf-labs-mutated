#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#Analyzer4 original results: [89, 20]
#Analyzer3 original results: []
#Analyzer5 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer5 analysis results: []
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Analyzer4 analysis results: [89]
#Original file name: SQLI/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_cath_finally_negative
#Used extensions: EXPR_str -> ~[EXPR_str]~.strip() | EXPR_str -> ~[EXPR_str]~.replace(~[EXPR_str]~, ~[EXPR_str]~)
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
from config.sqlite import *

class Pages:

    def getPage(self, pageId):
        tmpUnique42 = pageId
        try:
            raise Exception1(pageId.replace("vcrfl", "ydzvj").strip())
        except Exception1 as e:
            pageId = tmpUnique42
        finally:
            pageId = ""
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

