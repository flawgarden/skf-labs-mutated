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
        db = database_con()
        username = example_function_memo_positive(username, "eiulg")
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()




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
