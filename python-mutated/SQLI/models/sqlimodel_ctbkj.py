#Original file region: 7, null, null, null
#Mutated file region: 47, null, null, null
#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Original file name: SQLI/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/queue.tmt with name queue_poll_negative
#Used extensions: MACRO_Create_Queue -> queue787231 = collections.deque() | MACRO_Add_CONST_ToQueue -> queue787231.append(~[CONST_~[TYPE@1]~]~) | MACRO_Add_CONST_ToQueue -> queue787231.append(~[CONST_~[TYPE@1]~]~) | MACRO_Add_Fixed_VAR_ToQueue -> queue787231.append(~[VAR_~[TYPE@1]~@1]~)
#Program:
import collections
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
        queue787231 = collections.deque()
        queue787231.append("oomek")
        queue787231.append("vpjvw")
        queue787231.append(pageId)
        pageId = queue787231.popleft()
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

