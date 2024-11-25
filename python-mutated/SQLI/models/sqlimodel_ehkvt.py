#Original file region: 7, null, null, null
#Mutated file region: 51, null, null, null
#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Original file name: SQLI/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/collections/queue.tmt with name two_queues_positive
#Used extensions: EXPR_str -> ~[EXPR_str]~[~[EXPR_int]~:~[EXPR_int]~] | EXPR_str -> ~[EXPR_str]~ + ~[EXPR_str]~ | EXPR_str -> ~[EXPR_str]~[~[EXPR_int]~:~[EXPR_int]~] | EXPR_str -> ~[EXPR_str]~.replace('/', '.') | EXPR_int -> ~[EXPR_str]~.find(~[EXPR_str]~, start=~[EXPR_int]~, end=~[EXPR_int]~) | EXPR_str -> ~[EXPR_str]~.upper() | EXPR_str -> ~[EXPR_str]~ + ~[EXPR_str]~ | EXPR_str -> ""
#Program:
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
        db = database_con()
        sourceQueue = collections.deque()
        targetQueue = collections.deque()
        sourceQueue.append("mxsgq".replace('/', '.')[4920:pageId.find("keyfg", start=-23122, end=29287)])
        sourceQueue.append("dqejr".upper() + "kvsgp" + "xpqek")
        targetQueue.append(pageId)
        targetQueue.append(""[pageId:-12707])
        while len(sourceQueue) > 0:
            targetQueue.append(sourceQueue.popleft())
        pageId = targetQueue.popleft()
        cur = db.execute('SELECT pageId, title, content FROM pages WHERE pageId='+pageId)
        return cur.fetchall()

