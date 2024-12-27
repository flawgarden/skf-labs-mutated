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
        s23423 = pageId
        a12341 = StringHolder()
        def lmd(s: StringHolder) -> None:
            def innerLmd(p: StringHolder) -> None:
                p.value = "";
            innerLambda = UnaryOpMutation(innerLmd)
            innerLambda.mutate(s)
            s.value = s23423
        lambda1231 = UnaryOpMutation(lmd)
        lambda1231.mutate(a12341)
        pageId = a12341.value
        db = database_con()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

