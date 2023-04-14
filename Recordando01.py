# la etapa 01 consta en repasar todo lo que tenga que ver con python

#### Clase 01:

### Primero: el print.

print ("Es una función que ejecuta en la consola una impresión")

## Con print también se puede imprimir resultados de operaciones matemáticas

print (5 + 8)
print (3 * 8)
print (27 - 8)
print (12 / 8)

## La identación es un factor a tomar en cuenta a la hora de programar en python, es el hacer un espacio en el inicio de línea

### Segundo: los comentarios que se representan con un #, nos permiten hacer líneas de código que no se tomarán en cuenta a la hora de correr el prográma, es una buena práctica.

"""
Para escribir un comentario de varías línea se pueden escribir entre tres doblesd comillas o tres comillas sencillas
a
b
c
d
"""
#### Clase 02: 

### Primero: Las variables, cajas etiquetables a las que designas ciertos objetos.

My_name = "José Diego"

print (My_name)

My_age = 12

print (My_age)

## Las variables también se pueden actualizar

My_age = 19

print (My_age)

### Segundo: Podemos pedirle datos a los usuarios y almacenar los datos en una variable

Your_name = input("What is your name? ")
print ("Yo soy", Your_name)

#### Clase 03:

## Comprovaremos los distintos tipos de datos con la función "type"
## Hay distintos tipos de variables: Strings (son cadenas de texto, str); int (valores enteros); booleans (Solo hay dos: Verdadero o Falso. bool)
## Los inputs solo recogen los datos como str.

#### Clase 04:

## Los stings se pueden unir con una operación llamada concatenación.

### Primero: Concatenación

name = input("¿Cuál es tu nombre? ")
print (name)
last_name = input("¿Cuál es tu apellido? ")
print (last_name)

full_name = name + " " + last_name
print (full_name)

### Segundo: El formato

## Una opción es la siguiente: se concatenan strings con las variables, sobrando un espacio al final de cada string.

template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print ("Versión 01 " + template)

## La segunda forma es con unas llaves que reprecental un epacio donde va un valor, todo combinado con la función "format"

template = "Hola, mi nombre es {} y mi apellido es {}". format(name, last_name)
print ("versión 02 " + template)

## La tercera es más censilla

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print ("versión 03 " + template)


