#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Original file name: SQLI-like/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/field/nested.tmt with name nested_field_depth_2_array_negative
#Used extensions:
#Program:
from .Concurrency import *
from .Imports import *
from .ClassWrappers import *
from .MonkeyClass import *
from .MagicClass import *
from .Duck import *
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
        arr4124 = ["cefon"]
        nested7231 = NestedFields2(initialValues=arr4124)
        username = nested7231.nested1.nested1.values[0]
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()

