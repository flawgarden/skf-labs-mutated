from models.sqlimodel import *
from models.sqlimodel_lwjku import *
from models.sqlimodel_rianu import *
from models.sqlimodel_dawjz import *
from models.sqlimodel_qvxqi import *
from models.sqlimodel_dcldp import *
from models.sqlimodel_vqlsa import *
from models.sqlimodel_ausrg import *
from models.sqlimodel_ijgsy import *
from models.sqlimodel_lzktj import *
from models.sqlimodel_vxcoa import *
from models.sqlimodel_keshs import *
from models.sqlimodel_uwljk import *
from models.sqlimodel_yealu import *
from models.sqlimodel_wxtvp import *
from models.sqlimodel_vhbzh import *
from models.sqlimodel_mjqza import *
from models.sqlimodel_mndse import *
from models.sqlimodel_eqlla import *
from models.sqlimodel_hpkjj import *
from models.sqlimodel_vgdjs import *
from models.sqlimodel_cwilw import *
from models.sqlimodel_safmb import *
from models.sqlimodel_rtdgd import *
from models.sqlimodel_hruwa import *
from models.sqlimodel_gmczy import *
from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/home/<username>", methods=['GET'])
def inject(username):
    sqli  = User()
    values = sqli.getUser(username)
    username = values[0][0]
    email = values[0][1]
    return render_template("index.html", username = username, email = email)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

