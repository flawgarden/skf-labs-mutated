#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#Analyzer3 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer1 analysis results: [563]
#Analyzer2 analysis results: []
#Original file name: SQLI-like/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/tuples.tmt with name nested_tuples_positive
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
        tuple1 = (username,)
        tuple2 = ("lypbl",)
        nested_tuple = ((tuple1,), (tuple2,))
        username = nested_tuple[0][0]
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()

