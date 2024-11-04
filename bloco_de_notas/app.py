from flask import Flask, request, jsonify
from database import create_connection

app = Flask(__name__)

@app.route('/notas', methods=['POST'])
def create_nota():
    data = request.get_json()
    titulo = data['titulo']
    conteudo = data['conteudo']

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Notas (titulo, conteudo) VALUES (:titulo, :conteudo)", (titulo, conteudo))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Nota criada com sucesso!'}), 201

@app.route('/notas', methods=['GET'])
def get_notas():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notas")
    notas = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(notas), 200

@app.route('/notas/<int:id>', methods=['PUT'])
def update_nota(id):
    data = request.get_json()
    titulo = data['titulo']
    conteudo = data['conteudo']

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Notas SET titulo = :titulo, conteudo = :conteudo WHERE id = :id", (titulo, conteudo, id))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Nota atualizada com sucesso!'}), 200

@app.route('/notas/<int:id>', methods=['DELETE'])
def delete_nota(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Notas WHERE id = :id", (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Nota deletada com sucesso!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
