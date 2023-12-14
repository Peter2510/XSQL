from flask import Flask, request
from src.ejecucion.Ejecutar import Ejec
from src.ejecucion.environment import Environment
from Parser import *
import json
from flask_cors import CORS, cross_origin
from flask.helpers import url_for
from werkzeug.utils import redirect
from Lexer import tokens, lexer, errores, find_column
from src.visitor import ExpressionsVisitor



app = Flask(__name__)
CORS(app)

@app.route('/saludo',methods=["GET"])
def saludo():
    return {'mensaje':'Hola mundo!'}

@app.route('/ejecutar',methods=["POST","GET"])
def compilar():
    if request.method == "POST":

        env = Environment(None)
        visitorExpressions = ExpressionsVisitor(env)
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        pars = parse(entrada.lower())
        # Validaciones
        pars.accept(visitorExpressions, env)
        #
        iniciarEjecucion = Ejec(pars.statements)
        _res = iniciarEjecucion.execute(env)
        print(_res,"---------------------------- FINNNNNNNNNNN -------------")

        # ### solo prueba de esto
        # def prueba(texto):
        #     while True:
        #         tok = lexer.token()
        #         if not tok:
        #             break
        #         print(tok)
        # lexer.input(entrada)
        # prueba(entrada)
        # ##########3
        return {'mensaje':entrada}
    else:
        return {'mensaje':'Error al compilar'}
           
if __name__ == "__main__":
    app.run(debug=True,port=3000)