#Analyzer1 original results: [89, 20]
#Analyzer2 original results: [89, 20]
#-------------
#Analyzer1 analysis results: []
#Analyzer2 analysis results: [89]
#Original file name: SQLI-login-bypass/models/sqlimodel.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_multi_cath_negative
#Used extensions: EXPR_bool -> ~[EXPR_str]~.startswith(~[EXPR_str]~) | EXPR_str -> ~[EXPR_str]~.replace(~[EXPR_str]~, ~[EXPR_str]~) | EXPR_str -> ~[EXPR_str]~.replace(~[EXPR_str]~, ~[EXPR_str]~) | EXPR_str -> ~[EXPR_str]~.strip() | EXPR_str -> "" | EXPR_str -> ~[EXPR_str]~.replace(~[EXPR_str]~, ~[EXPR_str]~) | EXPR_str -> ~[EXPR_str]~.replace('/', '.') | EXPR_str -> ~[EXPR_str]~.lower()
#Program:
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
        tmpUnique42 = query
        try:
            if "simse".strip().startswith(""):
                raise Exception1("nwaxy".replace("wfkzn", "gwvox").replace(query, "ytsed"))
            else:
                raise Exception2("hvsvl".replace('/', '.').replace("yymmf", "pgmnv".lower()))
        except (Exception1, Exception2) as e:
            query = ""
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
