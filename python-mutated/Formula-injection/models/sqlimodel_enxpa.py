#Original file region: 7, null, null, null
#Mutated file region: 45, null, null, null
#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#Analyzer3 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer1 analysis results: [396, 89, 584]
#Analyzer2 analysis results: [89]
#Original file name: Formula-injection/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/exceptions/causeThrows.tmt with name null_pointer_exception_negative
#Used extensions:
#Program:
from typing import Any

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
        def get_none() -> Any:
            return None
        try:
            a = get_none()
            a = a + a
        except TypeError as e:
            pageId = ""
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

    def getLastPageId(self):
        db = database_con()
        cur = db.execute('SELECT pageId FROM pages ORDER BY pageId DESC LIMIT 1')
        return cur.fetchone()[0]

    def getAllPages(self):
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages')
        return cur.fetchall()

    def clearPages(self):
        db = database_con()
        try:
            db.execute('DELETE FROM pages WHERE pageId > 3')
            db.commit()
            msg = "Pages cleared sucessfully"
        except:
            db.rollback()
            msg = "Error on clearing the pages"
        finally:
            return msg

    def addPage(self,title,content):
        db = database_con()
        pageId = self.getLastPageId() + 1
        try:
            db.execute('INSERT INTO pages VALUES (?,?,?)',(pageId,title,content))
            db.commit()
            msg = "Page added successfully"
        except:
            db.rollback()
            msg = "Error on adding the page"
        finally:
            db.close()
            return msg    