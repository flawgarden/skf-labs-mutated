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
from flask import Flask, send_file

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/<path:path>')
def static_file(path):
    path = get_value_two_args(app, "1")
    return send_file(path)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8081)




def get_value(value=None):
    if value is None:
        value = "fixed_string"
    return value



def get_value_two_args(arg1, arg2=None):
    if arg2 is None:
        arg1 = "fixed_string"
    return arg1
