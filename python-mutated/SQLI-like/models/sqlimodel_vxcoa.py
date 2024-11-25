#Original file region: 7, null, null, null
#Mutated file region: 55, null, null, null
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
#Mutation info: Insert template from templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_multi_cath_negative
#Used extensions: EXPR_bool -> (~[EXPR_bool]~) and (~[EXPR_bool]~) | EXPR_str -> ~[EXPR_str]~ + ~[EXPR_str]~ | EXPR_str -> ~[EXPR_str]~ + ~[EXPR_str]~ | EXPR_bool -> ~[EXPR_bool]~ or ~[EXPR_bool]~ | EXPR_bool -> ~[EXPR_bool@1]~ or ~[EXPR_bool@1]~ | EXPR_str -> ~[EXPR_str]~[~[EXPR_int]~:~[EXPR_int]~] | EXPR_str -> ~[EXPR_str]~.replace(~[EXPR_str]~, ~[EXPR_str]~) | EXPR_str -> ~[EXPR_str]~.replace('/', '.')
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

class User:

    def getUser(self, username):
        db = database_con()
        tmpUnique42 = username
        try:
            if (False or True) and (True or True):
                raise Exception1("isklg"[username:29072] + "mgznq")
            else:
                raise Exception2("tlbsv".replace(db, "qkblp") + db.replace('/', '.'))
        except (Exception1, Exception2) as e:
            username = ""
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()

