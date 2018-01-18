'''
Created on 18 ene. 2018

@author: Carlos Vega Gonzalez
'''


'''
----------Apartado de notas----------
Cambiar a UTF-8 al crear un proyecto
'''


'''
#Secuencia de numeros
a = 0;
while a < 15:
     a = a + 1;
     print (a)
'''

'''
#Mostrar una secuencia de valores
año = 2001;
while año <= 2012:
    print ("Informes del Año", str(año));
    año +=1;
'''

'''    
#Pide un nombre al usuario. Al introducirlo se sale del while
while True:
    nombre = input ("Indique su nombre: ")
    print (nombre);
    if nombre:
        break 
'''

'''
#Sumar números introducidos por consola
a = 1;
suma = 0;
print ("Se introducirán números para añadirlos a una suma");
print ("Pulsa el número 0 para salir");
while a != 0:
     print ('El valor de la suma en este momento es: ', suma);
     a = float(input('Introduce un número: '));
     suma = suma + a;
print ('La suma total de los números introducidos es: ', suma);
'''

'''   
#Salir del While pulsando la letra s
#Pulsa diferentes letras cada vez para mantenerte dentro del while
#Pulsa la letra s para acabar
fin_prog = ""
while fin_prog != "s":
    print ("Estás dentro del while");
    fin_prog = input("pulsa la letra s para salir" )
'''

'''
#Acción según el valor de una cadena. IF lleva tabulaciones también
semaforo = "verde";
sem = input("Introduzca el estado del semaforo: ")
if sem == semaforo:
     print ("Cruzar la calle");
else:
     print ("Esperar");
'''

'''    
#Valor absoluto de un número introducido por consola
n = int(input("Introduce un número positivo o negativo: "));
if n < 0:
    print ('El valor absoluto de ', n, 'es ', -n);
else:
    print ('El valor absoluto de ', n, 'es ', n);
'''
    
'''
#Operador == del if dentro de un print
print ( 10 == 10); #Compara 10 con 8. Devolverá False en este ejemplo
 #Por ejemplo, si se comparara 10 con 10 devolvería True
x = 10;
y = 8;
print ( x == y); #Compara el valor de x con el de y. Devolverá False             
'''

'''
#Buscando elementos en una lista
lista = ['Geranio', 'Rosa', 'Clavel', 'Tulipán', 'Amapola', 'Lirio', 'Jazmín']
nombre = input("Compruebe si el elemento se encuentra en la lista: ")
nm = "Lavanda a sido aladido"
if nombre in lista:
    print('El elemento SÍ existe en la lista')
else:
    print('El elemento NO existe en la lista')
segundo = input("Escriba el nombre Lavanda: ")
if segundo not in lista:
    lista.append('Lavanda')
    print( str(nm))
'''


