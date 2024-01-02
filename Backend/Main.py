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
from src.visitor import GenerateASTVisitor, C3DVisitor
import io
from src.manejadorXml import  obtener

global env
env = None

app = Flask(__name__)
CORS(app)


# SOLO PRUEBA AQUI

@app.route('/saludo',methods=["GET"])
def saludo():
    
    Estructura.load()
    return Estructura.Databases

@app.route('/generaDump', methods = ['GET'])
def generaDump():
        nombre = request.args.get('nombre')
        Estructura.load()
        datos =[]
        datos.append( obtener.dumpXMl(nombre))
        return datos

@app.route('/generaExport', methods = ['GET'])
def generaExport():
        nombre = request.args.get('nombre')
        Estructura.load()
        datos =[]
        datos.append(obtener.exportTablaInserts(nombre))
        return datos


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
                
            if len(Estructura.tablasSimbolos) > 0:
                print("Tabla de simbolos")
                tb = json.dumps(Estructura.tablasSimbolos)
                Estructura.tablasSimbolos = []
                
                response['tablas'] = tb
            
            if len(env.funciones) > 0:
                print("Tabla de funciones")
                funciones = []
                nombres_de_funciones = list(env.funciones.keys())

                # Imprimir nombres y tipos de funciones
                for nombre in nombres_de_funciones:
                    funcion = env.funciones[nombre]

                    if isinstance(funcion.tipo, String_):
                        tipo = funcion.tipo.type.name
                    else:
                        tipo = funcion.tipo.name

                    funcion_info = {
                        'nombre': nombre,
                        'tipo': tipo,
                    }
                    funciones.append(funcion_info)
                
                tf = json.dumps(funciones)
                
                response['funciones'] = tf

            if len(_res) > 0 and len(env.errors) < 1:
                try:
                    tac_visitor = C3DVisitor(env)
                    pars.accept(tac_visitor, env)
                    response['tac'] = tac_visitor.code
                    ast_visitor = GenerateASTVisitor(env)
                    pars.accept(ast_visitor, env)
                    f = io.StringIO()
                    ast_visitor.get_graph().dot(f)
                    dot_string = f.getvalue()

                    response['dot'] = dot_string
                except Exception as e:
                    print(e)

            return response
    
        
        
def comprobarTexto(entrada):
    result = ""
    enComillas = False

    for char in entrada:
        if char == '"' or char == "'":
            enComillas = not enComillas
        result += char.lower() if not enComillas else char
    return result
           
if __name__ == "__main__":
    app.run(debug=True,port=3000)
