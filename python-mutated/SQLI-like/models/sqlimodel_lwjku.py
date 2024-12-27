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
        tmpList = [username, "vwtjh", "moaam"]
        compList = ["raxlv" + x for x in tmpList]
        username = compList[1]
        db = database_con()
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()

