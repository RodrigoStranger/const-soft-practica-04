from backend.models.mysql_connection_pool import MySQLPool

class AutorModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_autor(self, autor_id):
        params = {'id': autor_id}
        rv = self.mysql_pool.execute("SELECT * FROM autores WHERE id = %(id)s", params)
        data = []
        for result in rv:
            data.append({'id': result[0], 'nombre': result[1], 'nacionalidad': result[2]})
        return data

    def get_autores(self):
        rv = self.mysql_pool.execute("SELECT * FROM autores")
        data = [{'id': r[0], 'nombre': r[1], 'nacionalidad': r[2]} for r in rv]
        return data

    def create_autor(self, nombre, nacionalidad):
        data = {'nombre': nombre, 'nacionalidad': nacionalidad}
        query = "INSERT INTO autores (nombre, nacionalidad) VALUES (%(nombre)s, %(nacionalidad)s)"
        cursor = self.mysql_pool.execute(query, data, commit=True)
        data['id'] = cursor.lastrowid
        return data

    def update_autor(self, autor_id, nombre, nacionalidad):
        data = {'id': autor_id, 'nombre': nombre, 'nacionalidad': nacionalidad}
        query = "UPDATE autores SET nombre = %(nombre)s, nacionalidad = %(nacionalidad)s WHERE id = %(id)s"
        self.mysql_pool.execute(query, data, commit=True)
        return {'result': 1}

    def delete_autor(self, autor_id):
        params = {'id': autor_id}
        query = "DELETE FROM autores WHERE id = %(id)s"
        self.mysql_pool.execute(query, params, commit=True)
        return {'result': 1}