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
        try:
            dynamic_duck = DynamicDuck()
            add_quack_method(dynamic_duck)
            try:
                pageId = make_it_quack(dynamic_duck, pageId)
            except AttributeError:
                pageId = "fixed_string"
            db = database_con()
            cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
            return cur.fetchone()
        except Exception as e:
            print(e)
            return None



def make_it_quack(duck, arg):
    return duck.quack(arg)



def make_it_quack_attr(duck):
    if hasattr(duck, 'quack'):
        return duck.quack()
    return "fixed string"



def add_quack_method(duck):
    duck.quack = lambda a: "Some_ prefix " + a



def make_it_quack_field_attr(duck, arg):
    if hasattr(duck, 'constant'):
        return duck.quack(arg)
    else:
        return "fixed_string"
