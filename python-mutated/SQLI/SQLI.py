from models.sqlimodel import *
from models.sqlimodel_weluo import *
from models.sqlimodel_xlisn import *
from models.sqlimodel_ixabo import *
from models.sqlimodel_xldrs import *
from models.sqlimodel_qsujc import *
from models.sqlimodel_nohzy import *
from models.sqlimodel_juoxe import *
from models.sqlimodel_pbrvw import *
from models.sqlimodel_sdjvg import *
from models.sqlimodel_pjoim import *
from models.sqlimodel_vdylu import *
from models.sqlimodel_vuwer import *
from models.sqlimodel_kpekx import *
from models.sqlimodel_jbasw import *
from models.sqlimodel_djyrj import *
from models.sqlimodel_ljxkt import *
from models.sqlimodel_swcqc import *
from models.sqlimodel_xblbu import *
from models.sqlimodel_mbqpv import *
from models.sqlimodel_ehkvt import *
from models.sqlimodel_ljaip import *
from models.sqlimodel_qvkri import *
from models.sqlimodel_ctbkj import *
from models.sqlimodel_vwcaf import *
from models.sqlimodel_ztrcz import *
from models.sqlimodel_hauuc import *
from models.sqlimodel_vwhix import *
from models.sqlimodel_yepfj import *
from models.sqlimodel_othcc import *
from models.sqlimodel_ccefg import *
from models.sqlimodel_zuwth import *
from models.sqlimodel_hurdj import *
from models.sqlimodel_xcndf import *
from models.sqlimodel_wpjci import *
from models.sqlimodel_msrgv import *
from models.sqlimodel_dnstc import *
from models.sqlimodel_hkwlq import *
from models.sqlimodel_xgspt import *
from models.sqlimodel_xfcks import *
from models.sqlimodel_whfea import *
from models.sqlimodel_bdyci import *
from models.sqlimodel_bljbd import *
from models.sqlimodel_ymlmq import *
from models.sqlimodel_raqdv import *
from models.sqlimodel_vsggv import *
from models.sqlimodel_xgnkx import *
from models.sqlimodel_ggxcb import *
from models.sqlimodel_lrcmb import *
from models.sqlimodel_fttso import *
from models.sqlimodel_rmrge import *
from models.sqlimodel_nycqk import *
from models.sqlimodel_pottz import *
from models.sqlimodel_pedce import *
from models.sqlimodel_pckwo import *
from models.sqlimodel_nqgtf import *
from models.sqlimodel_uccgj import *
from models.sqlimodel_mtkkk import *
from models.sqlimodel_xdzpk import *
from models.sqlimodel_vpypg import *
from models.sqlimodel_szsjp import *
from models.sqlimodel_rdpdk import *
from models.sqlimodel_dfkht import *
from models.sqlimodel_fohef import *
from models.sqlimodel_dbgwa import *
from models.sqlimodel_nieas import *
from models.sqlimodel_dpppn import *
from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/home/<pageId>", methods=['GET'])
def inject(pageId):
    if pageId == 0:
        pageId = 1
    sqli  = Pages()
    values = sqli.getPage(pageId)
    id      = values[0][0]
    title   = values[0][1]
    content = values[0][2]
    return render_template("index.html",title = title, content = content, id = id)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
