from bd import obtener_conexion
import pymysql

def insetar_juego(nombre, descripcion, precio):
    conexion = obtener_conexion()
    if id == '' or nombre == '' or descripcion == '' or precio == '':
        return None
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO juegos(nombre, descripcion, precio) VALUES (%s, %s, %s)", (nombre, descripcion, precio))

    conexion.commit()
    conexion.close()
    

def obtener_juego_por_id(id):
    conexion = obtener_conexion()
    juego = None
    with conexion.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos WHERE id = %s", (id,))
        juego = cursor.fetchone()  
    conexion.close()
    return juego

def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor(pymysql.cursors.DictCursor) as cursor: 
        cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos

def actualizar_juego(id, nombre, descripcion, precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE juegos
            SET nombre = %s, descripcion = %s, precio = %s
            WHERE id = %s
        """, (nombre, descripcion, precio, id))
    conexion.commit()
    conexion.close()
    
def eliminar_juego(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM juegos WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


    
