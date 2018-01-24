'''
Created on 20 ene. 2018

@author: Carlos Vega Gonzalez
'''

import psycopg2
import psycopg2.extras
import sys
import pprint
#Para la conexión a la base de datos en Postgresql
print()
print("BIENVENIDOS A PYTHON Y A LA BASE DE DATOS POSTGRESQL")
print()
conx = None #Para destruir cualquier conexión conx existente
print("Conexión a la Base de Datos Polideportivo")
#Se usa try para poder capturar las excepciones producidas durante la conexión
try:
    # Se realiza la conexión con la base de datos postgres
    conx = psycopg2.connect("dbname=pruebas user=postgres password=root")
    print("Estableciendo conexión con la base de datos ...")
    #conx.cursor devuelve un objeto cursor necesario para realizar las consultas SQL
    cur = conx.cursor()
    print ("Conectado!\n")
except:
    print ("No se puede conectar con la Base de Datos")
cur.execute("DROP TABLE IF EXISTS alumnos")
print("La tabla alumnos se ha eliminado")
cur.execute("DROP TABLE IF EXISTS deportes")
print("La tabla deportes se ha eliminado")
cur.execute("CREATE TABLE alumnos (id_a serial PRIMARY KEY, nombre varchar, direccion varchar, DNI varchar, telefono integer)")
print("La tabla alumnos se ha creado")
cur.execute("CREATE TABLE deportes (id_d serial PRIMARY KEY, nombre varchar, localizacion text, precio money)")
print("La tabla deportes se ha creado")
#Se insertan algunas tuplas en la tabla alumnos
cur.execute("INSERT INTO alumnos (nombre, direccion, DNI, telefono) VALUES (%s, %s, %s, %s)",("Iván Moreno", "C/ Laguna 5, Móstoles", "40222444H", 656348821))
cur.execute("INSERT INTO alumnos (nombre, direccion, DNI, telefono) VALUES (%s, %s, %s, %s)",("Sara García", "C/ Olmos 16, Alcorcón", "21334655P", 647459932))
cur.execute("INSERT INTO alumnos (nombre, direccion, DNI, telefono) VALUES (%s, %s, %s, %s)",("Luis Sendra", "C/ Pinares 9, Leganés", "09113544S", 648560043))
cur.execute("INSERT INTO alumnos (nombre, direccion, DNI, telefono) VALUES (%s, %s, %s, %s)",("Ana Cortés", "C/ Robles 4, Móstoles", "10224655T", 629671154))
cur.execute("INSERT INTO alumnos (nombre, direccion, DNI, telefono) VALUES (%s, %s, %s, %s)",("Javier Uceda", "C/ Abetos 12, Alcorcón", "21335766V", 710782265))
#Se insertan algunas tuplas en la tabla deportes
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Natación", "piscina mediana", 30))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Natación", "piscina olímpica", 40))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Tenis", "pista 1", 25))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Tenis", "pista 2", 25))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Tenis", "pista 3", 25))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Tenis", "pista 4", 25))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Atletismo", "pista cubierta", 40))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Atletismo", "pista exterior", 35))
cur.execute("INSERT INTO deportes (nombre, localizacion, precio) VALUES (%s, %s, %s)",("Baloncesto", "pabellón A", 30))
#Se modifica la tabla Alumnos con un campo nuevo llamado deporte
cur.execute("ALTER TABLE alumnos ADD COLUMN deporte integer")
#Se dan valores al campo deporte
cur.execute("UPDATE alumnos SET deporte = 5 WHERE id_a = 1")
cur.execute("UPDATE alumnos SET deporte = 2 WHERE id_a = 2")
cur.execute("UPDATE alumnos SET deporte = 7 WHERE id_a = 3")
cur.execute("UPDATE alumnos SET deporte = 3 WHERE id_a = 4")
cur.execute("UPDATE alumnos SET deporte = 9 WHERE id_a = 5")
#Se relacionan las tablas alumnos y deportes
cur.execute("ALTER TABLE alumnos ADD CONSTRAINT depfk FOREIGN KEY (deporte) REFERENCES deportes (id_d) MATCH FULL")
#Se realiza una consulta
cur.execute("SELECT alumnos.nombre, deportes.nombre, deportes.localizacion FROM alumnos, deportes WHERE alumnos.deporte = deportes.id_d")
tuplas=cur.fetchall()
print()
print("Se muestran todos los alumnos y sus deportes usando pprint")
pprint.pprint(tuplas)