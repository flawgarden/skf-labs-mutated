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
#Original file name: SQLI-like/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/queue.tmt with name simple_poll_positive
#Used extensions: MACRO_Create_Queue -> queue787231 = collections.deque() | MACRO_Add_Fixed_VAR_ToQueue -> queue787231.append(~[VAR_~[TYPE@1]~@1]~)
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

class User:

    def getUser(self, username):
        queue787231 = collections.deque()
        queue787231.append(username)
        username = queue787231.popleft()
        db = database_con()
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()

