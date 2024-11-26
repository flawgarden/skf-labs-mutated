from threading import Thread
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
        w = Wrapper(pageId)
        task1 = SettingTask(w, "")
        task2 = SettingTask(w, pageId)
        task2.start()
        try:
            task2.join()
        except RuntimeError:
            pass
        task2.start()
        try:
            task1.join()
        except RuntimeError:
            pass
        pageId = w.i
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

