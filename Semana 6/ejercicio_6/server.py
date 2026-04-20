from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada en memoria
notas = [
    {"id": 1, "contenido": "Comprar pan"},
    {"id": 2, "contenido": "Estudiar Flask"}
]

# RUTA: Obtener todas las notas (LECTURA)
@app.route('/notas', methods=['GET'])
def obtener_notas():
    return jsonify(notas)

# RUTA: Agregar una nueva nota (CREACIÓN)
@app.route('/notas', methods=['POST'])
def agregar_nota():
    nueva_nota = {
        "id": len(notas) + 1,
        "contenido": request.json.get('contenido')
    }
    notas.append(nueva_nota)
    return jsonify(nueva_nota), 201

# RUTA: Eliminar una nota (ELIMINACIÓN)
@app.route('/notas/<int:nota_id>', methods=['DELETE'])
def eliminar_nota(nota_id):
    global notas
    notas = [n for n in notas if n['id'] != nota_id]
    return jsonify({"mensaje": "Nota eliminada"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)