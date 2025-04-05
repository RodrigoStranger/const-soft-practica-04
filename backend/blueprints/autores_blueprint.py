from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from backend.models.mysql_autores_model import AutorModel

model = AutorModel()
autor_blueprint = Blueprint('autor_blueprint', __name__)

@autor_blueprint.route('/crearautor', methods=['POST'])
@cross_origin()
def create_autor():
    data = model.create_autor(request.json['nombre'], request.json.get('nacionalidad'))
    return jsonify(data)

@autor_blueprint.route('/actualizarautor', methods=['PUT'])
@cross_origin()
def update_autor():
    data = model.update_autor(
        request.json['id'],
        request.json['nombre'],
        request.json.get('nacionalidad')
    )
    return jsonify(data)

@autor_blueprint.route('/eliminarautor', methods=['DELETE'])
@cross_origin()
def delete_autor():
    return jsonify(model.delete_autor(int(request.json['id'])))

@autor_blueprint.route('/obtenerautor', methods=['GET'])
@cross_origin()
def get_autor():
    return jsonify(model.get_autor(int(request.json['id'])))

@autor_blueprint.route('/obtenerautores', methods=['GET'])
@cross_origin()
def get_autores():
    return jsonify(model.get_autores())
