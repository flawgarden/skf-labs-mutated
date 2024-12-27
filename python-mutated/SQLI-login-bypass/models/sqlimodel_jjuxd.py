from .GenericTwoClass import *
from .GenericClassVariance import *
from .GenericClass import *
from .SealedSuper import *
from .SuperClass import *
from .SuperInterface import *
from .SpecialOperatorsStringHolder import *
from .BinaryOpInterface import *
from .UnaryOpClass import *
from .UnaryOpInterface import *
from .ImplBinaryOpInterfaceClass import *
from .BaseBinaryOpClass import *
from .DerivedBinaryOpClass import *
from .BinaryOpInterfaceDefault import *
from .ImplementsEnterExit import *
from .ArrayHolder import *
from .StaticFieldHolder import *
from .StringFactory import *
from .NestedFields import *
from .StringHolder import *
from .NestedStringHolder import *
from .InstanceInitializer import *
from .ConstructorChains import *
from .Imports import *
from .ReflectionHelper import *
from .MagicClass import *
from .Record import *
from .UnaryOpMutationInterface import *
from .MonkeyClass import *
from .Exceptions import *
from .Point import *
from .ClassWrappers import *
from .Concurrency import *
from .Duck import *

#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
# SKF Labs - Security Knowledge Framework (SKF)
# Copyright (C) 2022, OWASP Foundation, Inc.
#
# This software is provided under a slightly modified version
# of The GNU Affero General Public License. See the accompanying LICENSE 
# file for more information.
#
# Author:
#   Alex Romero (@NtAlexio2)
# 

from config.sqlite import *

class dbaccess:

    def validateUser(self, username, password):
        query = 'SELECT Username, Password FROM users WHERE Username=\'{}\' AND Password=\'{}\''.format(username, password)
        map787234 = dict()
        map787234["imuak"] = query
        if "imuak" in map787234:
            query = map787234.pop("imuak")
        db = database_con()
        cur = db.execute(query)
        return cur.fetchall()

    def getUser(self, username):
        db = database_con()
        cur = db.execute('SELECT Username, Password FROM users WHERE Username= ?',
        [username])
        return cur.fetchall()

    def getHash(self, Hash):
        db = database_con()
        cur = db.execute('SELECT Username, Password FROM users WHERE Hash= ?', [Hash])
        return cur.fetchall()