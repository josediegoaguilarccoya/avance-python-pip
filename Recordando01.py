# La etapa 01 consta en repasar todo lo que tenga que ver con python
# ******************************************************************

#### Clase 01: Tu primer programa

print ("*" * 30)
print ("Clase 01")
print ("*" * 30)

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

print ("*" * 30)
print ("Clase 02")
print ("*" * 30)

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

print ("*" * 30)
print ("Clase 03")
print ("*" * 30)

## Comprobaremos los distintos tipos de datos con la función "type"
## Hay distintos tipos de variables: Strings (son cadenas de texto, str); int (valores enteros); booleans (Solo hay dos: Verdadero o Falso. bool)
## Los inputs solo recogen los datos como str.

#### Clase 04: Strings

print ("*" * 30)
print ("Clase 04")
print ("*" * 30)

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

print ("*" * 30)
print ("Clase 05")
print ("*" * 30)

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

print ("*" * 30)
print ("Clase 06")
print ("*" * 30)

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

print ("*" * 30)
print ("Clase 07")
print ("*" * 30)

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

### Cuarto; cuando lo que escribimos no son dígitos, la función int no puede tarnsformarlos a un número entero y te arroja un error.

#### Clase 08: Operadores aritméticos 

print ("*" * 30)
print ("Clase 08")
print ("*" * 30)

### Primero; los operadores aritméticos básicos son:

a = int(input("primer número ==>  "))
b = int(input("segundo número ==>  "))

## Adición
print ( a + b )

## Sustracción 
print ( a - b )

## Multiplicación 
print ( a * b )

## División 
print ( a / b )

## Módulo: Esta operación te da el residuo de la división.
print ( a % b )

##  : solo captura el npumero entero de una división inexacta 
print ( a // b )

## Potencia 
print ( a ** b )

### Segundo: Las operacines aritméticas en python se resuelven según la jerarquía de operaciones.
## Primero se resuelve los signos de agrupación 
## Segundo las operaciones exponenciales
## Tercero las operaciones de multiplicación y división. 
## Cuarto las operaciones adición y resta.

#### Clase 09: Operadores de comparación 

print ("*" * 30)
print ("Clase 09")
print ("*" * 30)


## Los operadores de comparación sirven para la lógica

#### Primero; operadores de comparación, nos dan un valor booleano

a = int(input("primer número ==>  "))
b = int(input("segundo número ==>  "))

# Mayor que ">" 

print ( a > b )

# Menor que "<"

print ( a < b )

# Mayor o igual que ">="

print ( a >= b )

# Menor o igual que "<="

print ( a <= b )

# Igualdad "=="

print ( a == b )

## Compara de manera rádical las mayúsculas y minúsculas, también compara el tipo de dato, esto se refiere a que un string no será igual a un entero.

# Dieferente de "!="

print ( a != b )

#### Clase 10: Comparación de números flotantes 

print ("*" * 30)
print ("Clase 10")
print ("*" * 30)

### Primero: Constituimos una variable "x" y una variable "y"

x = 3.3 
print (x)

y = 2.2 + 1.1 
print (y)

### Segundo: si cmparamos estas dos variables tendremos un False como resultado, lo que nos podría dar errores si no conocemos de él.

print (x==y)

### Tercero: para superar el error podemos combertir a y en un str

y_str = format(y, ".2g")
print ("str ==> ", y_str)

## Para compara "x" y "y" hacemos lo siguiente.

print (y_str == str(x))

### Cuarto: el siguiente método permite la comparación, para ello usaremos una variable llamada tolerance y el valor absoluto de la diferencia entre los números que queremos comparar.

tolerance = 0.00001
print(abs(x-y) < tolerance)

#### Clase 11: Operadores lógicos: and y or 

print ("*" * 30)
print ("Clase 11")
print ("*" * 30)

### Primero: and

print("AND")

print("True and True ==> ", True and True)
print("True and False ==> ", True and False)
print("False and True ==> ", False and True)
print("Flase and False ==> ", False and False)

### Segundo: or

print("OR")

print("True or True ==> ", True or True)
print("True or False ==> ", True or False)
print("False or True ==> ", False or True)
print("Flase or False ==> ", False or False)

#### Clase 12: Operador lógico not 

print ("*" * 30)
print ("Clase 12")
print ("*" * 30)

### Primero: not 

print (not True)
print (not False)

#### Clase 13: Condicionales 

print ("*" * 30)
print ("Clase 13")
print ("*" * 30)

### Primero: los if hacen cumplir el código iterado en si, siempre y cuando tenga un True.

if True: 

    print ("Debería ejecutarse")

if False: 

    print ("Nunca debería ejecutarse")

### Segundo: else y un ejemplo.

## El else significa que sí la codición inicial no se cumple se hará otra cosa.

stock =int(input("Digita el stock ==> "))

if stock >= 100 and stock <= 1000:
    print ("El estock es el correcto")

else: 
    print ("El stock es incorrecto")

### Tercero: elif y el ejemplo de las mascotas.

## Sí no corre la primera condición, el programa pasa a la segunda y así sucesivamente

print ("Versión Incompleta")

pet = input("¿Cuál es tu mascota favorita?  ")

if pet == "perro":
    print ("Tines buen gusto")

if pet == "gato":
    print ("Tienes gustos aburridos")

if pet == "pez":
    print ("tu mascota será comida para gatos")

print ("Versión Completa")

if pet == "perro":
    print ("Tines buen gusto")

elif pet == "gato":
    print ("Tienes gustos aburridos")

elif pet == "pez":
    print ("tu mascota será comida para gatos")

else: 
    print ("Tienes una mascota exótica")

#### Clase 14: Proyecto: Condicionales.

print ("*" * 30)
print ("Clase 14")
print ("*" * 30)

print ("Este proyecto se llevará a cabo en el archivo Recordando01_Game.py")

#### Clase 15: String recargado 

print ("*" * 30)
print ("Clase 15")
print ("*" * 30)

### Primero: "in" para saber si una palabra esta incluida en un string. Teda ana respuesta booleana para confirmarte la existencia de un conjunto de caracteres en un strign

text = "Yo sé programar en python" 
print ("JavaScript" in text)
print ("Python" in text)

### Segundo: "len" pra evaluar el tamaño de un string

size = len(text)
print (size)

### Tercero: "upper"

print (text)
print (text.upper())

### Cuarto: "lower" para pasarlo todo a minúscula 

print(text)
print (text.lower())

### Quinto: "count" para saber el número de veces que se repite una letra en un string 

"print (text.count(a))"

### Sexto: "swapcase" invierte las mayúsculas y las minúsculas

print (text.swapcase())

### Septimo: "startswith" Para consultar si la palabra inicia con determinado conjunto de caracteres

print (text.startswith("Ella"))

### Octavo: "endswith" para saber con que conjunto de caracteres termina un string 

print (text.endswith("python"))

### Noveno: "replace" para sustituir un conjunto de caracteres determinados por otro conjunto de caracteres dados

print (text.replace("Python", "JavaScript"))

### Décimo: "capitalize" pone el primer caracter en mayucula

text_2 = "Este es un título"

print(text_2)
print(text_2.capitalize())

### Undecimo: "title" para poner todas las letras del inicio de cada palabra en mayuscula 

print(text_2.title())

### Duodecimo: "title" isdigit para saver si un strin es un conjunto de dígitos, esta función te responde con booleans

print(text_2.isdigit)

#### Clase 16: Indexing y slicing

print ("*" * 30)
print ("Clase 16")
print ("*" * 30)

### Primero: Cada caracte ocupa un lugar en la cadena de texto, iniciado desde la posición cero.

text = "Tu quieres comer zandía"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])
print(text[6])
print(text[7])
print(text[8])
print(text[9])

### Segundo: Para evaluar el último lugar se puede hacer de la siguiente manera 

size = len(text)
print ("size ==>  ", size)
print(text[size - 1])

### Tercero: Para hacer lo mismo que en el segundo punto, pero mucho más fácil, podemos hacerlo de la siguiente manera.

print(text[-1])
print(text[-2])
print(text[-3])
print(text[-4])
print(text[-5])
print(text[-6])
print(text[-7])
print(text[-8])
print(text[-9])
print(text[-10])
 
### Cuarto: slicing, podemos sacar ciertas pacrtes del texto teniendo en cuenta los conceptos anteriores.

print(text[0:5])

## Lo anterior se puede expresar de la siguiente manera, obiando el cero 

print(text[:5])

## Para dominar el slicing tines que dominar las posiciones del conjunto de caracteres que quieras sacar de determinados strings.

print(text[12:-22])

### Quinto: para escoger caracteres con saltos de posición se hace de la siguiente manera

print(text[12:23:2])

#### Clase 17: Listas 

print ("*" * 30)
print ("Clase 17")
print ("*" * 30)

### Primero: Una lista se delimita por corchetes, es una estructura que guarda un conjunto de datos: 

numeros = [2, 3, "hello", "hola"]

print (numeros)
print (type(numeros))

## Se puede aplicar Indexing y slicing con las listas

print (numeros[3])
print (numeros [:3])

## Los strings no son mutables, pero las listas si son mutables.

"""
text = "Hola bebe, ya que contigo no sirve la..."
text[0] = "Z"
"""
numeros[1] = 3 
print (numeros)

## Se puede saber si hay un elemento en una lista o no. 

print (2 in numeros)

#### Clase 18: Métodos de listas

print ("*" * 30)
print ("Clase 18")
print ("*" * 30)

### Primero: CRUD; significa Create, Read, Update and Delete 

### Segundo: Create 

numeros = [2,3,4,5,2,3,4,9]

### Tercero: Read

print (numeros[4])

### Cuarto: Update

numeros [-2] = 28
print (numeros)

### Quinto: append para agregar valores al final de la lista

numeros.append(123)
print(numeros)

### Sexto: insert es una manera de incluir un nuevo dato en la lista determinando la posición en la que lo quieres tener 

numeros.insert(3, "palo")
print (numeros)

## Insertar o remplaza al elemento anterior on el nuevo incluido, solo reordena los elmentos corriendo para delante los elementos de las listas.

### Septimo: se puede sumar listas, de la siguiente manera.

todo = ["todo1","todo2","todo3"]

new_list = numeros + todo
print (todo)

### Octavo: para saber en que posición esta un elemento, se usa la función index.

index = new_list.index("todo2")
new_list[index] = "camarón con cola"
print (new_list)

### Noveno: para remover usamos remove

new_list.remove("todo1")
print(new_list)

## Pra eliminar también se puede usar "pop"

new_list.pop(4)
print(new_list)

### Décimo: una manera de cambiar el orden de la lista es con reverse 

new_list.reverse()
print(new_list)

### Undecimo: una manera de ordenarlo automática, teniendo como criterios el orden numérico y el orden alfabetico es con la función sort 

numbers = [1,2,3,4,5]
numbers.sort()
print(numbers)

string = ["la","le","li","lo","lu"]
string.sort()
print(string)

## sort no puede ordenar una lista con elementos de distintas naturalesas, no puede comparar en un sentido ordinal strings y números.

print(new_list.sort())

#### Clase 19: Tuplas

print ("*" * 30)
print ("Clase 19")
print ("*" * 30)




























