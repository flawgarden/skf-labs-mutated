#CodeQL original results: [89, 20]
#Semgrep original results: [89, 20]
#Snyk original results: []
#-------------
#Snyk analysis results: []
#CodeQL analysis results: [89]
#Semgrep analysis results: [89]
#Original file name: SQLI/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/tuples.tmt with name swap_values_with_tuple_negative
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

class Pages:

    def getPage(self, pageId):
        tuple1 = (pageId,)
        tuple2 = (16114,)
        a, b = tuple1, tuple2
        a, b = b, a
        pageId = a[0]
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

