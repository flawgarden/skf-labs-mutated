#Original file region: 7, null, null, null
#Mutated file region: 52, null, null, null
#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: [396, 584]
#Analyzer2 analysis results: [89]
#Original file name: Formula-injection/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/lambdas/mutation.tmt with name nested_unary_lambda_mutation_positive
#Used extensions:
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
        db = database_con()
        s23423 = pageId
        a12341 = StringHolder()
        def lmd(s: StringHolder) -> None:
            def innerLmd(p: StringHolder) -> None:
                p.value = "";
            innerLambda = UnaryOpMutation(innerLmd)
            innerLambda.mutate(s)
            s.value = s23423
        lambda1231 = UnaryOpMutation(lmd)
        lambda1231.mutate(a12341)
        pageId = a12341.value
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