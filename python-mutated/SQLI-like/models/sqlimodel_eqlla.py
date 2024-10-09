#CodeQL original results: [89, 20]
#Semgrep original results: [89, 20]
#Snyk original results: []
#-------------
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: []
#Original file name: SQLI-like/models/sqlimodel.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/varargs/varargs.tmt with name varargs_get_string_with_index_negative 
#Used extensions: EXPR_str -> ""
#Program:
from typing import TypeVar
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
        db = database_con()
        username = getStringWithIndex(1, username, "")
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()
    



def getFirstString(*lines: str) -> str:
    return getStringWithIndex(0, *lines)



def getStringWithIndex(ind: int, *lines: str) -> str:
    return lines[ind]



def getFirstStringFromArray(*lines: str) -> str:
    return list(lines)[0]



TYPEVAR = TypeVar('TYPEVAR')
def varargsWithGenerics(*elements: TYPEVAR) -> TYPEVAR:
    return elements[0]



def combineStrings(*strings: str) -> str:
    return ", ".join(strings)
