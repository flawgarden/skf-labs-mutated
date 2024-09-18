#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#Analyzer4 original results: [89, 20]
#Analyzer3 original results: []
#Analyzer5 original results: []
#-------------
#Analyzer3 analysis results: []
#Analyzer5 analysis results: []
#Analyzer1 analysis results: [396, 584]
#Analyzer2 analysis results: [89]
#Analyzer4 analysis results: [89]
#Original file name: Formula-injection/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/list.tmt with name list_filter_neutral
#Used extensions: MACRO_Create_List -> list787231 = [] | MACRO_Add_VAR_ToList -> list787231.append(~[VAR_~[TYPE@1]~@1]~) | MACRO_Add_EXPR_ToList -> list787231.append(~[EXPR_~[TYPE@1]~@1]~) | MACRO_Add_CONST_ToList -> list787231.append(~[CONST_~[TYPE@1]~@1]~) | EXPR_bool -> ~[EXPR_bool@1]~ and ~[EXPR_bool@1]~
#Program:
from .Record import *
from .Exceptions import *
from .GenericClass import *
from .GenericClassVariance import *
from .GenericTwoClass import *
from .UnaryOpInterface import *
from .BinaryOpInterface import *
from .BinaryOpInterfaceDefault import *
from .DerivedBinaryOpClass import *
from .BaseBinaryOpClass import *
from .UnaryOpClass import *
from .ImplBinaryOpInterfaceClass import *
from .SuperInterface import *
from .SuperClass import *
from .SealedSuper import *
from .StringHolder import *
from .StringFactory import *
from .InstanceInitializer import *
from .NestedStringHolder import *
from .ConstructorChains import *
from .ArrayHolder import *
from .StaticFieldHolder import *
from .UnaryOpMutationInterface import *
from config.sqlite import *

class Pages:

    def getPage(self, pageId):
        list787231 = []
        list787231.append(pageId)
        list787231.append(pageId)
        list787231.append(True)
        pageId  = next(filter(lambda s: pageId and pageId, list787231))
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