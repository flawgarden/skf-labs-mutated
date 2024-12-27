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

class User:

    def getUser(self, username):
        dynamic_duck = DynamicDuck()
        add_quack_method(dynamic_duck)
        try:
            username = make_it_quack(dynamic_duck, "wmsjs")
        except AttributeError:
            pass
        db = database_con()
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()




def make_it_quack(duck, arg):
    return duck.quack(arg)



def make_it_quack_attr(duck, arg):
    if hasattr(duck, 'quack'):
        return duck.quack(arg)
    return "fixed string"



def add_quack_method(duck):
    duck.quack = lambda a: "Some_ prefix " + a



def make_it_quack_field_attr(duck, arg):
    if hasattr(duck, 'constant'):
        return duck.quack(arg)
    else:
        return "fixed_string"
