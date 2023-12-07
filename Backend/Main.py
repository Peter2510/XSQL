from flask import Flask, request
import json
from flask_cors import CORS, cross_origin
from flask.helpers import url_for
from werkzeug.utils import redirect




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
        print(entrada)
        global tmp_val
        tmp_val = entrada["code"]
        return redirect(url_for("compilar"))
        print(entrada)
        return {'mensaje':'A COMPILAR'}
    else:
        return {'mensaje':'Error al compilar'}
    
@app.route('/compilar')
def compilar():
    global tmp_val
    
    global Tabla
    
    
        
    
if __name__ == "__main__":
    app.run(debug=True,port=3000)