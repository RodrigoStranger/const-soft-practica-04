from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from backend.models.mysql_libros_model import LibroModel

model = LibroModel()
libro_blueprint = Blueprint('libro_blueprint', __name__)

@libro_blueprint.route('/crearlibro', methods=['POST'])
@cross_origin()
def create_libro():
    data = model.create_libro(
        request.json['titulo'],
        request.json['año_publicacion'],
        request.json['id_autor']
    )
    return jsonify(data)

@libro_blueprint.route('/actualizarlibro', methods=['PUT'])
@cross_origin()
def update_libro():
    data = model.update_libro(
        request.json['id'],
        request.json['titulo'],
        request.json['año_publicacion'],
        request.json['id_autor']
    )
    return jsonify(data)

@libro_blueprint.route('/eliminarlibro', methods=['DELETE'])
@cross_origin()
def delete_libro():
    return jsonify(model.delete_libro(int(request.json['id'])))

@libro_blueprint.route('/obtenerlibro/<int:id>', methods=['GET'])
@cross_origin()
def get_libro():
    return jsonify(model.get_libro(id))

@libro_blueprint.route('/obtenerlibros', methods=['GET'])
@cross_origin()
def get_libros():
    return jsonify(model.get_libros())
