import collections
from .Record import *
from .Exceptions import *
from .GenericClass import *
from .GenericClassVariance import *
from .GenericTwoClass import *
from .UnaryOpInterface import *
from .BinaryOpInterface import *
from .BinaryOpInterfaceDefault import *
from .DerivedBinaryOpClass import *
from .BaseBinaryOpClass import *
from .UnaryOpClass import *
from .ImplBinaryOpInterfaceClass import *
from .SuperInterface import *
from .SuperClass import *
from .SealedSuper import *
from .StringHolder import *
from .StringFactory import *
from .InstanceInitializer import *
from .NestedStringHolder import *
from .ConstructorChains import *
from .ArrayHolder import *
from .StaticFieldHolder import *
from .UnaryOpMutationInterface import *
from config.sqlite import *

class Pages:

    def getPage(self, pageId):
        queue787231 = collections.deque()
        queue787231.append(pageId)
        value7843 = queue787231.popleft() if len(queue787231) > 0 else "rinmz"
        pageId = value7843
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

