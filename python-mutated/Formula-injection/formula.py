from models.sqlimodel import *
from models.sqlimodel_zztfc import *
from models.sqlimodel_hfpzp import *
from models.sqlimodel_vxjhu import *
from models.sqlimodel_bydpq import *
from models.sqlimodel_wscqs import *
from models.sqlimodel_tfdaa import *
from models.sqlimodel_afpya import *
from models.sqlimodel_vmynv import *
from models.sqlimodel_qgcvb import *
from models.sqlimodel_gneeb import *
from models.sqlimodel_acpgi import *
from models.sqlimodel_orfju import *
from models.sqlimodel_selvl import *
from models.sqlimodel_jtnqz import *
from models.sqlimodel_pjmkp import *
from models.sqlimodel_ncdho import *
from models.sqlimodel_jwfce import *
from models.sqlimodel_muizf import *
from models.sqlimodel_cjpni import *
from models.sqlimodel_bybxi import *
from models.sqlimodel_mlazk import *
from models.sqlimodel_llqjc import *
from models.sqlimodel_reekn import *
from models.sqlimodel_mtlvo import *
from models.sqlimodel_vgxme import *
from models.sqlimodel_zzmda import *
from models.sqlimodel_tnlop import *
from models.sqlimodel_tsily import *
from models.sqlimodel_zgmgk import *
from models.sqlimodel_sjzwp import *
from models.sqlimodel_fcscx import *
from models.sqlimodel_gsydq import *
from models.sqlimodel_xihnu import *
from models.sqlimodel_nlfmk import *
from models.sqlimodel_kklkz import *
from models.sqlimodel_ydjpm import *
from models.sqlimodel_tlych import *
from models.sqlimodel_goett import *
from models.sqlimodel_ejoai import *
from models.sqlimodel_vhfzl import *
from models.sqlimodel_xoubq import *
from models.sqlimodel_tatww import *
from models.sqlimodel_tjidb import *
from models.sqlimodel_kadfi import *
from models.sqlimodel_zkhya import *
from models.sqlimodel_zgkej import *
from models.sqlimodel_asyyc import *
from models.sqlimodel_hmlyu import *
from models.sqlimodel_ucsgv import *
from models.sqlimodel_idrrh import *
from models.sqlimodel_gsqax import *
from models.sqlimodel_otmxs import *
from models.sqlimodel_ysdsj import *
from models.sqlimodel_ldehj import *
from models.sqlimodel_bhrcm import *
from models.sqlimodel_faopv import *
from models.sqlimodel_havzu import *
from models.sqlimodel_wbokl import *
from models.sqlimodel_wfdhx import *
from models.sqlimodel_enxpa import *
from models.sqlimodel_fzrpy import *
from models.sqlimodel_isrdb import *
from models.sqlimodel_ileql import *
from models.sqlimodel_etanm import *
from models.sqlimodel_lfmqc import *
from models.sqlimodel_mnojp import *
from models.sqlimodel_frxfs import *
from models.sqlimodel_wwzdp import *
from models.sqlimodel_ubyhw import *
from models.sqlimodel_zqlbx import *
from models.sqlimodel_zqvxp import *
from models.sqlimodel_lkmor import *
from models.sqlimodel_pbczh import *
from models.sqlimodel_yecyq import *
from models.sqlimodel_bluwv import *
from models.sqlimodel_blnrh import *
from models.sqlimodel_ttlkx import *
from models.sqlimodel_twceg import *
from models.sqlimodel_brwav import *
from models.sqlimodel_kxywh import *
from models.sqlimodel_svntj import *
from models.sqlimodel_ojkbt import *
from models.sqlimodel_yecjq import *
from models.sqlimodel_rwoyh import *
from models.sqlimodel_txpqy import *
from models.sqlimodel_wjjrm import *
from models.sqlimodel_fqwqi import *
from models.sqlimodel_ewzsw import *
from models.sqlimodel_ilpmk import *
from models.sqlimodel_vuvbp import *
from models.sqlimodel_ujfok import *
from models.sqlimodel_ptfwd import *
from models.sqlimodel_jutxf import *
from models.sqlimodel_qglkm import *
from models.sqlimodel_twjnl import *
from flask import Flask, request, render_template
import flask_excel as excel


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

excel.init_excel(app)


@app.route("/", methods=['GET'])
def home():
    p = Pages()
    menu = p.getAllPages()
    return render_template("index.html", menu=menu)


@app.route("/home/<pageId>", methods=['GET'])
def inject(pageId):
    if pageId == 0:
        pageId = 1
    p  = Pages()
    values = p.getPage(pageId)
    id      = values[0][0]
    title   = values[0][1]
    content = values[0][2]

    menu = p.getAllPages()

    return render_template("index.html",title = title, content = content, id = id, menu = menu)

@app.route("/pages/add", methods=['POST'])
def add():
    p = Pages()
    msg = p.addPage(request.form.get('title'),request.form.get('content'))
    menu = p.getAllPages()
    return render_template("index.html", menu=menu, msg = msg)

@app.route("/pages/export", methods=['GET'])
def export():
    p = Pages()
    menu = p.getAllPages()
    pagesArray = []
    pagesArray.append(["Page ID","Title","Content"])
    for page in menu:
        pagesArray.append([page[0],page[1],page[2]])

    return excel.make_response_from_array(pagesArray,"xls",file_name="export_pages")

@app.route("/pages/clear", methods=['GET'])
def clear():
    p = Pages()
    msg = p.clearPages()
    menu = p.getAllPages()
    return render_template("index.html", menu=menu, msg = msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
	