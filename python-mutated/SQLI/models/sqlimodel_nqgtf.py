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
        try:
            rh = ReflectionHelper.__new__(ReflectionHelper)
            ReflectionHelper.__init__(rh, pageId)
            setattr(rh, "value", "kbzlg")
            pageId = rh.get_value()
        except Exception:
            raise
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

