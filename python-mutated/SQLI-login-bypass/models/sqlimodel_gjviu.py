#
#
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
from .MonkeyClass import *
from .Exceptions import *
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
        tmpUnique42 = username
        try:
            raise Exception1("AA")
        except Exception1 as e:
            username = ""
        finally:
            username = tmpUnique42
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
