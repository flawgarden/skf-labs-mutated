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
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/map.tmt with name map_merge_1_positive
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
from config.sqlite import * 

class Pages:
    
    def getPage(self, pageId):
        db = database_con()
        map111 = {}
        map222 = {}
        map111[-21822] = pageId
        map222[-10279] = db
        map111.update(map222)
        db = map111[-10279]
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()
    
