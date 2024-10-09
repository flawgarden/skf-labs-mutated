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
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/tuples.tmt with name tuple_unpacking_positive 
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
        db = database_con()
        my_tuple = (username, "rpznq", "fetrb")
        a, b, c = my_tuple
        username = a
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()
    
