from flask import Flask, jsonify, request
# por defecto para crear una instancia de aplicación
def create_app():
    app = Flask(__name__)
    return app
app = create_app()
# metodo de respuesta GET para concoer el estado del servicio, devuelve un json
# para llamarlo poner SU_IP:8081/status
@app.route("/status")
def status():
    return {
        "estado": "1",
        "texto": "OK" 
    }
# API REST que recibe un JSON lo imprime por consola y responde un json 
@app.route("/events", methods=(['POST']))
def create_event():
    event = request.json
    print(event)
    response = {'token': '123456789'}
    return jsonify(response)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
