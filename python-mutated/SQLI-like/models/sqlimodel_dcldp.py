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

class User:

    def getUser(self, username):
        s123 = SimpleImport()
        username = s123.func("cmxic")
        db = database_con()
        cur = db.execute("SELECT UserName, email FROM users WHERE UserName LIKE '%"+username+"%' ORDER BY UserId")
        return cur.fetchall()

