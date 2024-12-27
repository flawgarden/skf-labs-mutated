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
        gen = simple_generator(pageId, "rdstw", "cbnff")
        genToList = list(gen)
        pageId = genToList[1]
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


def simple_generator(arg1, arg2, arg3):
    yield arg1
    yield arg2
    yield arg3



def infinite_gen(arg1, arg2):
    yield arg1
    while True:
        yield arg2



def generator_from(arg1, arg2, arg3, arg4):
    yield from simple_generator(arg1, arg2, arg3)
    yield arg4
