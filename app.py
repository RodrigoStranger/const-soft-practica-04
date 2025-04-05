from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.autores_blueprint import autor_blueprint
from backend.blueprints.libros_blueprint import libro_blueprint

app = Flask(__name__)

app.register_blueprint(autor_blueprint, url_prefix='/home')
app.register_blueprint(libro_blueprint, url_prefix='/home')

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)