from typing import TypeVar
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
        password = getFirstStringFromArray(password, username)
        username = getFirstStringFromArray(username, password)
        query = 'SELECT Username, Password FROM users WHERE Username=\'{}\' AND Password=\'{}\''.format(username, password)
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



def getFirstString(*lines: str) -> str:
    return getStringWithIndex(0, *lines)



def getStringWithIndex(ind: int, *lines: str) -> str:
    return lines[ind]



def getFirstStringFromArray(*lines: str) -> str:
    return list(lines)[0]



TYPEVAR = TypeVar('TYPEVAR')
def varargsWithGenerics(*elements: TYPEVAR) -> TYPEVAR:
    return elements[0]



def combineStrings(*strings: str) -> str:
    return ", ".join(strings)
