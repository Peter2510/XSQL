from flask import Flask, request
from src.ejecucion.Ejecutar import Ejec
from src.ejecucion.environment import Environment
from Parser import *
import json
from flask_cors import CORS, cross_origin
from flask.helpers import url_for
from werkzeug.utils import redirect
from Lexer import tokens, lexer, errors, find_column
from src.manejadorXml import  Estructura

global env
env = None

app = Flask(__name__)
CORS(app)


@app.route('/saludo',methods=["GET"])
def saludo():
    Estructura.load()
    return Estructura.Databases

@app.route('/ejecutar',methods=["POST","GET"])

def compilar():
    if request.method == "POST":
        global env 
        if env is None:
             env = Environment(None)
        #env = Environment(None)
        
        entrada = request.data.decode("utf-8")
        entrada = json.loads(entrada)
        entrada = comprobarTexto(entrada)
        pars = parse(entrada)
        if len(errors) > 0:
            #Se convierte la lista de instancias a una lista de diccionarios
            errores_dict_list = [error.to_dict() for error in errors]

            #Se convertierte la lista de diccionarios a formato JSON
            json_string = json.dumps(errores_dict_list, indent=2)

            # Imprimir el resultado
            print(json_string)
            errors.clear()
            #cuando termine la ejecucion de un .sql 
            #se resetea el nombre de la base de datos actual
            Estructura.nombreActual = ""
            env.errors.clear()
            return {'errores':json_string}
        
        else:
            response = {'errores': '', 'resultados': []}
            iniciarEjecucion = Ejec(pars.statements)
            _res = iniciarEjecucion.execute(env)
            if len(env.errors) > 0:
                    errores_dict_list = [error.to_dict() for error in env.errors]
                    json_string = json.dumps(errores_dict_list, indent=2)
                    Estructura.nombreActual = ""
                    env.errors.clear()
                    response['errores'] = json_string
            if len(_res) > 0:
                # print("Compilación exitosa")
                print("",Estructura.nombreActual)
                Estructura.nombreActual = ""
                env.errors.clear()

                response['resultados'] = _res

            return response
    
        
        
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