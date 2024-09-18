#CodeQL original results: [89, 20]
#Semgrep original results: [89, 20]
#Bandit original results: [89, 20]
#Snyk original results: []
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [89]
#Bandit analysis results: [89]
#Original file name: SQLI/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/list.tmt with name list_get_negative
#Used extensions: MACRO_Create_List -> list787231 = [] | MACRO_Add_CONST_ToList -> list787231.append(~[CONST_~[TYPE@1]~@1]~)
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
        db = database_con()
        list787231 = []
        list787231.append("dnbcf")
        pageId = list787231[0]
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()
    
