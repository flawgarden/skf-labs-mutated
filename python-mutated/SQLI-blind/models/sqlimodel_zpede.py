#CodeQL original results: [89, 20]
#Semgrep original results: [89, 20]
#Snyk original results: []
#-------------
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: []
#Original file name: SQLI-blind/models/sqlimodel.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/interpolation.tmt with name format_method_interpolation_positive 
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
        try:
            db = database_con()
            tmpStr = pageId
            interpolatedStr = "Some_prefix, {}".format(tmpStr)
            pageId = interpolatedStr
            cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
            return cur.fetchone()
        except Exception as e:
            print(e)
            return None
