'''
Created on 20 ene. 2018

@author: Carlos Vega Gonzalez
'''

import psycopg2
import psycopg2.extras
import sys
import pprint



def menu():
     
    print ("Selecciona una opción")
    print ("\t1 - Dar de alta un cliente")
    print ("\t2 - Añadir alumno")
    print ("\t3 - Eliminar alumno")
    print ("\t4 - Mostrar notas por alumno")
    print ("\t5 - Modificar notas por alumno")
    print ("\t6 - Salir") 

def alta():
    
    cur.execute("INSERT INTO Polideportivo (nombre, direccion, dni, telefono) VALUES (%s, %s, %s, %s)",(n, d, f, t))
  
print()
print("BIENVENIDOS A PYTHON Y A LA BASE DE DATOS POSTGRESQL")
print()
conx = None

print("Conexión a la Base de Datos Polideportivo")

try:
    # Se realiza la conexión con la base de datos postgres
    conx = psycopg2.connect("dbname=Polideportivo user=postgres password=root")
    print("Estableciendo conexión con la base de datos ...")
    #conx.cursor devuelve un objeto cursor necesario para realizar las consultas SQL
    cur = conx.cursor()
    print ("Conectado!\n")
except:
    print ("No se puede conectar con la Base de Datos")
cur.execute("DROP TABLE IF EXISTS Clientes")
print("La tabla clientes se ha eliminado")
cur.execute("DROP TABLE IF EXISTS Deportes")
print("La tabla deportes se ha eliminado")
cur.execute("CREATE TABLE Clientes (id serial PRIMARY KEY, nombre varchar, direccion varchar, dni varchar, telefono integer)")
cur.execute("CREATE TABLE Deportes (id serial PRIMARY KEY, deporte varchar, precio_hora varchar)")

while True:
    menu()
    alta()
    
    opcionMenu = input("Seleccione una opción: ")
 
    if opcionMenu == "1":
        
        input("Pulse enter para continuar.")
        n = input("Introduzca su nombre: ")
        d = input("Introduzca su dni: ")
        f = input("Introduzca fecha de nacimiento: ")
        t = input("Introduzca su numero de teléfono: ")

    elif opcionMenu == "2":
        input("Pulse enter para continuar.")
        
    elif opcionMenu == "3":
        input("Pulse enter para continuar.")