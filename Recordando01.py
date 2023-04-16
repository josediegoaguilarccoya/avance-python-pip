# La etapa 01 consta en repasar todo lo que tenga que ver con python
# ******************************************************************

#### Clase 01: Tu primer programa

print ("***********************************************************")
print ("Clase 01")
print ("***********************************************************")

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
#### Clase 02: Variables

print ("***********************************************************")
print ("Clase 02")
print ("***********************************************************")

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

#### Clase 03: Tipoes de datos

print ("***********************************************************")
print ("Clase 03")
print ("***********************************************************")

## Comprobaremos los distintos tipos de datos con la función "type"
## Hay distintos tipos de variables: Strings (son cadenas de texto, str); int (valores enteros); booleans (Solo hay dos: Verdadero o Falso. bool)
## Los inputs solo recogen los datos como str.

#### Clase 04: Strings

print ("***********************************************************")
print ("Clase 04")
print ("***********************************************************")

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

## La tercera es más sencilla

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print ("versión 03 " + template)

#### Clase 05: Numbers

print ("***********************************************************")
print ("Clase 05")
print ("***********************************************************")

### Primero; los str o números enteros.

## Los números no se declaran entre comillas, si no se vuelven strings

vidas = "123"
print (vidas)
print (type(vidas))

vidas = 123
print (vidas)
print (type(vidas))

### Segundo; los números con una precisión decimal o float

temperatura = 12.56 
print (temperatura)
print(type(temperatura))

### Tercero; las variables que contengan un valor numérico se pueden actualizar operandolas con el valor previo de la variable.

Age = 3 
print (Age)

Age = Age + 5 
print (Age)

### Cuarto; Una sintaxis especial.

Age = Age - 2
print (Age)

Age -= 2
print (Age)

## Las dos expresiones escritas previamente son equivalentes

### Quinto; Cuando tenemos un número muy grande o muy pequeño python lo expresa en notación científica.

number = 5400000000000000000.234 
print (number)

number = 0.000000000000001232131
print (number)

### Sexto; Es buena práctica escribir el nombre de las variables teniendo en cuenta lo que representan o guardan como valor. De esa manera sabremos que guarda la variable con tan solo leer el nombre.

#### Clase 06: Booleans 

print ("***********************************************************")
print ("Clase 06")
print ("***********************************************************")

### Primero; los booleans 

## Los valores booleanos solo tienen dos valores: verdadero o falso. Se escriben iniciando en mayuscula e ingles. 

Trabajaste = True 
print (Trabajaste)
print (type(Trabajaste))

Trabajaste = False 
print (Trabajaste)
print (type(Trabajaste))

### Segundo; podemos invertir el valor de un booleano con el operador "not".

print (not Trabajaste)

Trabajaste = not Trabajaste 
print (Trabajaste)

#### Clase 07: Transformación de tipos

print ("***********************************************************")
print ("Clase 07")
print ("***********************************************************")

### Primero; se puede cambiar el tipo de dato de manera dinámica, es una ventaja de la flexibilidad de Python

name = "José"
print(type(name))
name = 12
print(type(name))
name = True 
print(type(name))

### Segundo; dependiendo del tipo de dato toma de distintas formas los operadores matemáticos. Por ejemplo: el operador (+) concatena strings y suma enteros y datos numéricos. Esto hace que no podamos operar con el signo de la adición un string y un entero.

print ("come" + "manzanas")
print (12 + 32)
#print ("name" + 32)

## el ejemplo anterior no podría ser corrido en la terminal.

### Tercero; podemos combertir de la siguiente manera un entero a un string 

age = 13 
print ("Mi edad es " + str(age))

## Otro modo de transformar es con la función format

print (f"Mi edad es {age}")

## Ahora podemos hacer un programa sencillo. Con una intención opuesta, ya no queremos combertir un entero en un string, ahora queremos que un string se vuelva un entero.

age = input("Escribe tu edad ==>  ")
print(type(age))
age = int(age)
age += 10
print(f"Tu edad en 10 años será {age}")













