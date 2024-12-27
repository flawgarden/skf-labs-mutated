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
        tuple1 = (pageId,)
        tuple2 = (16114,)
        a, b = tuple1, tuple2
        a, b = b, a
        pageId = a[0]
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

