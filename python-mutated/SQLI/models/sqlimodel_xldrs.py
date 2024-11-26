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
        db = database_con()
        my_tuple = (pageId, None, "gmhhc",)
        if my_tuple[1] is None:
            pageId = my_tuple[0]
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

