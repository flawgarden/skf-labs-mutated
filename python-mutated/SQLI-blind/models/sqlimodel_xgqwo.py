#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Original file name: SQLI-blind/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/field/constructors.tmt with name class_with_instance_initializer_negative
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
        try:
            db = database_con()
            ii = InstanceInitializer(db)
            db = ii.list[0]
            cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
            return cur.fetchone()
        except Exception as e:
            print(e)
            return None
