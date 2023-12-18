from flask import Flask, request
from src.ast.symTable import SymTable
from src.ejecucion.Ejecutar import Ejec
from src.ejecucion.environment import Environment
from Parser import *
import json
from flask_cors import CORS, cross_origin
from flask.helpers import url_for
from werkzeug.utils import redirect
from Lexer import tokens, lexer, errores, find_column
from src.visitor import ExpressionsVisitor
from src.manejadorXml import  Estructura
from src.visitor.symbolTableVisitor import SymbolTableVisitor
from src.visitor.usarvisitor import UsarVisitor 


app = Flask(__name__)
CORS(app)

@app.route('/saludo',methods=["GET"])
def saludo():
    Estructura.load();
    return Estructura.Databases

@app.route('/ejecutar',methods=["POST","GET"])
def compilar():
    if request.method == "POST":

        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        pars = parse(entrada.lower())
        env = Environment(None)
        visitorExpressions = ExpressionsVisitor(env)
        
        visitorUsar = UsarVisitor(env)
        pars.accept(visitorUsar,env)
        
        # Validaciones
        pars.accept(visitorExpressions, env)
        
        #visitor declaracion de una funcion
        pars.accept(SymbolTableVisitor(env),env)
        for er in env.errors:
            print(er.toString())
        #
        iniciarEjecucion = Ejec(pars.statements)
        _res = iniciarEjecucion.execute(env)
        print(_res,"---------------------------- FINNNNNNNNNNN -------------")
        sb = SymTable("padre")
        sb.symbolFuncs['pedro' ] = '45'
        print(sb.symbolFuncs)
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