from flask import Flask, request
from Parser import *
import json
from flask_cors import CORS, cross_origin
from flask.helpers import url_for
from werkzeug.utils import redirect
from Lexer import tokens, lexer, errores, find_column



app = Flask(__name__)
CORS(app)

@app.route('/saludo',methods=["GET"])
def saludo():
    return {'mensaje':'Hola mundo!'}

@app.route('/ejecutar',methods=["POST","GET"])
def compilar():
    if request.method == "POST":
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        print(entrada, type(entrada))
        pars = parse(entrada)
        for instr in pars:
            instr.interpretar(None, None)



        ### solo prueba de esto
        def prueba(texto):
            while True:
                tok = lexer.token()
                if not tok:
                    break
                print(tok)
        lexer.input(entrada)
        prueba(entrada)
        ##########3
        return {'mensaje':entrada}
    else:
        return {'mensaje':'Error al compilar'}
           
if __name__ == "__main__":
    app.run(debug=True,port=3000)