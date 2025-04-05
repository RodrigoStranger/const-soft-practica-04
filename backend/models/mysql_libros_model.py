from backend.models.mysql_connection_pool import MySQLPool

class LibroModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def get_libro(self, libro_id):
        params = {'id': libro_id}
        rv = self.mysql_pool.execute("""
            SELECT L.id, L.titulo, L.año_publicacion, A.nombre 
            FROM libros L 
            INNER JOIN autores A ON L.id_autor = A.id 
            WHERE L.id = %(id)s
        """, params)
        data = [{'id': r[0], 'titulo': r[1], 'año_publicacion': r[2], 'autor': r[3]} for r in rv]
        return data

    def get_libros(self):
        rv = self.mysql_pool.execute("""
            SELECT L.id, L.titulo, L.año_publicacion, A.nombre 
            FROM libros L 
            INNER JOIN autores A ON L.id_autor = A.id
        """)
        data = [{'id': r[0], 'titulo': r[1], 'año_publicacion': r[2], 'autor': r[3]} for r in rv]
        return data

    def create_libro(self, titulo, año_publicacion, id_autor):
        autor_exists_query = "SELECT COUNT(*) FROM autores WHERE id = %(id_autor)s"
        params = {'id_autor': id_autor}
        autor_exists = self.mysql_pool.execute(autor_exists_query, params)
        if autor_exists[0][0] == 0:
            return {'error': 'El autor con el ID proporcionado no existe en la base de datos.'}
        data = {'titulo': titulo, 'año_publicacion': año_publicacion, 'id_autor': id_autor}
        query = "INSERT INTO libros (titulo, año_publicacion, id_autor) VALUES (%(titulo)s, %(año_publicacion)s, %(id_autor)s)"
        cursor = self.mysql_pool.execute(query, data, commit=True)
        data['id'] = cursor.lastrowid
        return {'message': f"Libro '{titulo}' creado correctamente.", 'libro': data}

    def delete_libro(self, libro_id):
        params = {'id': libro_id}
        query = "DELETE FROM libros WHERE id = %(id)s"
        self.mysql_pool.execute(query, params, commit=True)
        return {'result': f'Libro con id {libro_id} eliminado correctamente'}
    
    def update_libro(self, libro_id, titulo, año_publicacion, id_autor):
        data = {
            'id': libro_id,
            'titulo': titulo,
            'año_publicacion': año_publicacion,
            'id_autor': id_autor
        }
        query = """
        UPDATE libros
        SET titulo = %(titulo)s, año_publicacion = %(año_publicacion)s, id_autor = %(id_autor)s
        WHERE id = %(id)s
        """
        self.mysql_pool.execute(query, data, commit=True)
        return {'result': f'Libro "{titulo}" actualizado correctamente'}