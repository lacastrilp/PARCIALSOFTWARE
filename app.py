from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/factorial/<int:num>', methods=['GET'])
def calcular_factorial(num):
    # Calcular factorial
    factorial = math.factorial(num)

    # Determinar si el factorial es par o impar
    etiqueta = "par" if factorial % 2 == 0 else "impar"

    # Crear respuesta JSON
    resultado = {
        "numero_recibido": num,
        "factorial": factorial,
        "etiqueta": etiqueta
    }
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
