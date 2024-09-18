#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#Analyzer3 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer1 analysis results: [89]
#Analyzer2 analysis results: [89]
#Original file name: SQLI/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/concurrency/concurrency.tmt with name two_set_threads_in_sequence_negative
#Used extensions:
#Program:
from threading import Thread
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
        w = Wrapper(pageId)
        task1 = SettingTask(w, "")
        task2 = SettingTask(w, pageId)
        task2.start()
        try:
            task2.join()
        except RuntimeError:
            pass
        task2.start()
        try:
            task1.join()
        except RuntimeError:
            pass
        pageId = w.i
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

