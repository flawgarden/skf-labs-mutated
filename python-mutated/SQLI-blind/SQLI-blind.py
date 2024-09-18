from models.sqlimodel import *
from models.sqlimodel_tdair import *
from models.sqlimodel_ubldg import *
from models.sqlimodel_hybmg import *
from models.sqlimodel_sjczg import *
from models.sqlimodel_xykfa import *
from models.sqlimodel_ncnuy import *
from models.sqlimodel_rafzl import *
from models.sqlimodel_xgqwo import *
from models.sqlimodel_nsxac import *
from models.sqlimodel_zpede import *
from models.sqlimodel_speem import *
from models.sqlimodel_zispw import *
from models.sqlimodel_yxnsv import *
from models.sqlimodel_kggtk import *
from models.sqlimodel_jpjbt import *
from flask import Flask, render_template


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/home/<pageId>", methods=['GET'])
def inject(pageId):
    sqli = Pages()
    values = sqli.getPage(pageId)
    print(values)
    print(pageId)
    if values:
        if pageId == '1':
            return render_template("index.html",title = "The welcome page", content = "Some text about the welcome page is inserted here", id = 1)
        if pageId == '2':
            return render_template("index.html",title = "About", content = "Some text about the about page!", id = 2)
        if pageId == '3':
            return render_template("index.html",title = "Contact", content = "Some contact information is found here", id = 3)
        return render_template("index.html")
    else:
        return render_template("404.html")

@app.route('/asdfg', defaults={'path': ''})
@app.route('/<path:path>')
def default(path):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')


