from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>', methods=['GET'])
def calcular_factorial(num):
    factorial = math.factorial(num)

    etiqueta = "par" if num % 2 == 0 else "impar"

    respuesta = {
        "numero_recibido": num,
        "factorial": factorial,
        "etiqueta": etiqueta
    }
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
