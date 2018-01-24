'''
Created on 23 ene. 2018

   
    elif opcionMenu == "4":
        input("Pulse enter para continuar.")
            
    elif opcionMenu == "5":
        input("Pulse enter para continuar.")
    elif opcionMenu == "6":
        break
    else:
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar") 


@author: Carlos Vega Gonzalez
'''
import collections

notas = []
alumno = []

def menu():
    
    
    
    print ("Selecciona una opción")
    print ("\t1 - Mostrar alumnos")
    print ("\t2 - Añadir alumno")
    print ("\t3 - Eliminar alumno")
    print ("\t4 - Mostrar notas por alumno")
    print ("\t5 - Modificar notas por alumno")
    print ("\t6 - Salir")

    
while True:
    
    menu()
    
   
    
    opcionMenu = input("Seleccione una opción: ")
 
    if opcionMenu == "1":
        input("Pulse enter para continuar.")
        
        for x in alumno: 
            print('Nombre:', x['Nombre'], '\tDNI:', x['DNI'])

    elif opcionMenu == "2":
        input("Pulse enter para continuar.")
        
        nombre = input("Introduzca un nombre: ")    
        dni = input("Introduzca el dni: ")
        
        nuevoestudiante = {'Nombre': nombre, 'DNI': dni}
        
        alumno.append(nuevoestudiante)
        
        print("Contacto anadido.")
        
    elif opcionMenu == "3":
        input("Pulse enter para continuar.")
        
        if nombre in alumno:
            
          
    