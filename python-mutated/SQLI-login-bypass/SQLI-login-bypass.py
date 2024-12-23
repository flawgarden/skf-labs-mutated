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
# Description:
#   This application is vulnerable to SQL injection attacks that causes
#   to access admin panel, without credentials.
#
# Author:
#   Alex Romero (@NtAlexio2)
#
# Reference:
#   https://portswigger.net/web-security/sql-injection/lab-login-bypass
#

from models.sqlimodel import *
from models.sqlimodel_kjixf import *
from models.sqlimodel_ioqha import *
from models.sqlimodel_rckzw import *
from models.sqlimodel_znleq import *
from models.sqlimodel_iiqmj import *
from models.sqlimodel_jnalv import *
from models.sqlimodel_ffuuy import *
from models.sqlimodel_bxzpy import *
from models.sqlimodel_hphap import *
from models.sqlimodel_xxcga import *
from models.sqlimodel_iwfil import *
from models.sqlimodel_xdymi import *
from models.sqlimodel_ktmtj import *
from models.sqlimodel_amjtf import *
from models.sqlimodel_pfhzm import *
from models.sqlimodel_xrkyt import *
from models.sqlimodel_jcpjj import *
from models.sqlimodel_njjao import *
from models.sqlimodel_ejuef import *
from models.sqlimodel_ngcxg import *
from models.sqlimodel_fjzie import *
from models.sqlimodel_vethi import *
from models.sqlimodel_whhvs import *
from models.sqlimodel_uyhxd import *
from models.sqlimodel_ivhux import *
from models.sqlimodel_wewdy import *
from models.sqlimodel_vpzlk import *
from models.sqlimodel_irgdj import *
from models.sqlimodel_odrga import *
from models.sqlimodel_szvof import *
from models.sqlimodel_aaifg import *
from models.sqlimodel_tlmsk import *
from models.sqlimodel_gjviu import *
from models.sqlimodel_tfvhl import *
from models.sqlimodel_smbtc import *
from models.sqlimodel_pjiig import *
from models.sqlimodel_uamwg import *
from models.sqlimodel_hwhix import *
from models.sqlimodel_kklev import *
from models.sqlimodel_hbjth import *
from models.sqlimodel_oxurs import *
from models.sqlimodel_ygtmu import *
from models.sqlimodel_qumaa import *
from models.sqlimodel_ughzz import *
from models.sqlimodel_zqrti import *
from models.sqlimodel_vzfic import *
from models.sqlimodel_kioxb import *
from models.sqlimodel_xcwqp import *
from models.sqlimodel_hfxvw import *
from flask import Flask, request, render_template, make_response, request
import hashlib


app = Flask(__name__, static_url_path='/static', static_folder='static')

app.config['DEBUG'] = False


@app.route("/")
def start():
    '''
    Application main page.
    '''
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Login page for users to create new session.
    '''
    sqli = dbaccess()
    keys = request.form.keys()
    if 'username' in keys and 'password' in keys:
        try:
            username = request.form['username']
            password = request.form['password']
            values   = sqli.validateUser(username, password) # Unsafe Function!
            if values:
                response = make_response(render_template("loggedin.html", username=values[0][0], msg="Congratulations!"))
                response.set_cookie("sessionid", hashlib.sha1(username.encode('utf-8')).hexdigest())
                return response
        except Exception as e:
            return render_template("500.html", error=str(e))
    return render_template("index.html")


@app.route("/loggedin", methods=['POST', 'GET'])
def loggedin():
    '''
    User dashboard.
    '''
    if not isloggedin():
        return render_template("index.html", msg='You have to login first')

    hash     = request.cookies.get('sessionid')
    sqli     = dbaccess()
    values   = sqli.getHash(hash.lower())
    username = values[0][0].lower()
    return render_template("loggedin.html", username=username, msg="Congratulations!")


@app.route("/logout", methods=['GET'])
def logout():
    '''
    Terminate user session.
    '''
    text = ''
    if request.method == "GET":
        text     = 'You successfully logged out'
        response = make_response(render_template('index.html',msg=text))
        response.set_cookie('sessionid', '', expires=0)
        return response
    text = "You are not logged out"
    return render_template('index.html', msg=text)


def isloggedin():
    if 'sessionid' in request.cookies:
        hash = request.cookies.get('sessionid')
        sqli = dbaccess()
        values = sqli.getHash(hash.lower())
        if values:
            return True
    return False


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

