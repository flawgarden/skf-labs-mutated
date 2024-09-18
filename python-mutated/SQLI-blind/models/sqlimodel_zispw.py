#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Original file name: SQLI-blind/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/magic/magic.tmt with name magic_method_iter_positive
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

class Pages:

    def getPage(self, pageId):
        mc = MagicClass(pageId)
        pageId = mc["tmp_string"]
        try:
            db = database_con()
            cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
            return cur.fetchone()
        except Exception as e:
            print(e)
            return None
