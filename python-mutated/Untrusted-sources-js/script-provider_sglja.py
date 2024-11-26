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
from flask import Flask, send_file

app = Flask(__name__)
app.config['DEBUG'] = True
a12341 = StringHolder(app)
def lmd(s: StringHolder) -> None:
    inner234234 = s.value
    def innerLmd(p: StringHolder) -> None:
        p.value = inner234234;
    innerLambda = UnaryOpMutation(innerLmd)
    innerLambda.mutate(s)
    s.value = ""
lambda1231 = UnaryOpMutation(lmd)
lambda1231.mutate(a12341)
app = a12341.value


@app.route('/<path:path>')
def static_file(path):
    return send_file(path)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8081)

