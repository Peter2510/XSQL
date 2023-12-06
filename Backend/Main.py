from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/saludo',methods=["GET"])
def saludo():
    return {'mensaje':'Hola mundssso'}

@app.route('/compilar',methods=["POST","GET"])
def compilar():
    if request.method == "POST":
        data = request.get_json
        print(data)
        return {'mensaje':'compiladosss'}
    else:
        return {'mensaje':'Error compilar'}
    
if __name__ == "__main__":
    app.run(debug=True,port=3000)