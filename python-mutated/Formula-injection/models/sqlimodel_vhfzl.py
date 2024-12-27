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
        pageId = example_function_memo_negative(pageId, "mefyu")
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


def wrapperExample(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper



def wrapperExample2(func):
    def wrapper(*args, **kwargs):
        args = ("fixed_string",) + args[1:]
        result = func(*args, **kwargs)
        return result
    return wrapper



def wrapperExampleMemoization(func):
    cache = ["result"]
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        cache.append(result)
        return cache[-1]
    return wrapper



def wrapperExampleMemoizationNegative(func):
    cache = ["result"]
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        cache.append(result)
        return cache[0]
    return wrapper



@wrapperExample
def example_function(x, y):
    return x + y



@wrapperExampleMemoization
def example_function_memo_positive(x, y):
    return x + y



@wrapperExampleMemoizationNegative
def example_function_memo_negative(x, y):
    return x + y



@wrapperExample2
def example_function_2(x, y):
    return x + y



@ClassWrapper
def example_function_with_class_wr(x, y):
    return x + y



@ClassWrapperEmpty
def example_function_with_empty_class_wr(x, y):
    return x + y
