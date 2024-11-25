#Original file region: 7, null, null, null
#Mutated file region: 37, null, null, null
#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#Analyzer3 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer1 analysis results: [89]
#Analyzer2 analysis results: [89]
#Original file name: SQLI-like/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/conditional/recursion.tmt with name recursion_mutual_negative
#Used extensions:
#Program:
from .Exceptions import *
from .Concurrency import *
from .Imports import *
from .ClassWrappers import *
from .MonkeyClass import *
from .MagicClass import *
from .Duck import *
from .ReflectionHelper import *
from .StringHolder import *
from .StringFactory import *
from .InstanceInitializer import *
from .NestedStringHolder import *
from .ConstructorChains import *
from .ArrayHolder import *
from .NestedFields import *
from .StaticFieldHolder import *
from config.sqlite import *

class User:

    def getUser(self, username):
        username = param_or_empty_mutual2(len(username), username)
        db = database_con()
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()




def param_or_empty(value: int, param: str) -> str:
    if len(param) == value:
        return param
    elif value > len(param):
        return param_or_empty(value - 1, param)
    else:
        return ""



def param_or_empty_mutual1(value: int, param: str) -> str:
    if len(param) == value:
        return param
    elif value > len(param):
        return param_or_empty_mutual2(value - 1, param)
    else:
        return ""



def param_or_empty_mutual2(value: int, param: str) -> str:
    return param_or_empty_mutual1(value - 1, param)
