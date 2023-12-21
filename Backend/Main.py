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
from src.manejadorXml import  Estructura 



app = Flask(__name__)
CORS(app)

@app.route('/saludo',methods=["GET"])
def saludo():
    Estructura.load();
    return Estructura.Databases

@app.route('/ejecutar',methods=["POST","GET"])

def compilar():
    if request.method == "POST":

        env = Environment(None)
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        entrada = comprobarTexto(entrada)
        pars = parse(entrada)
        iniciarEjecucion = Ejec(pars.statements)
        _res = iniciarEjecucion.execute(env)
        if len(env.errors) > 0:
            for e in errores:
                print("a",e)
        else:
            print("Compilación exitosa")
        #     return {'mensaje':"Compilación exitosa"}
        
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
        
def comprobarTexto(entrada):
    result = ""
    enComillas = False

    for char in entrada:
        if char == '"':
            enComillas = not enComillas
        result += char.lower() if not enComillas else char

    return result
    
           
           
if __name__ == "__main__":
    app.run(debug=True,port=3000)