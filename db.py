import pymysql
import json

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"

def get_conn():
    conn = pymysql.connect(
        db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
    )
    return conn


# DONACIONES
def insert_into_donacion(comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO donacion (comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',(comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular) )
    conn.commit()

def get_five_donacion(page):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion ORDER BY id DESC LIMIT %s,5',(page,))
    pedidos = cursor.fetchall()
    return pedidos

def get_donacion_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, comuna_id, calle_numero, tipo, cantidad, fecha_disponibilidad, descripcion, condiciones_retirar, nombre, email, celular FROM donacion WHERE id=%s', (id,))
    donacion = cursor.fetchone()
    return donacion

# PEDIDOS
def insert_into_pedido(comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pedido (comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) VALUES (%s, %s, %s, %s, %s, %s, %s);',(comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante) )
    conn.commit()

def get_five_pedido(page):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido ORDER BY id DESC LIMIT %s,5',(page*5,))
    pedidos = cursor.fetchall()
    return pedidos

def get_pedido_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, comuna_id, tipo, descripcion, cantidad, nombre_solicitante, email_solicitante, celular_solicitante FROM pedido WHERE id=%s',(id,))
    pedido = cursor.fetchone()
    return pedido

# FOTOS

def insert_into_foto(ruta_archivo, nombre_archivo, donacion_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO foto (ruta_archivo, nombre_archivo, donacion_id) VALUES (%s, %s, %s);', (ruta_archivo, nombre_archivo, donacion_id))
    conn.commit()

def get_foto_by_donacion_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, ruta_archivo, nombre_archivo, donacion_id FROM foto WHERE donacion_id=%s',(id,))
    foto = cursor.fetchall()
    return foto

def get_foto_by_id(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('SELECT id, ruta_archivo, nombre_archivo, donacion_id FROM foto WHERE id=%s',(id,))
    foto = cursor.fetchone()
    return foto