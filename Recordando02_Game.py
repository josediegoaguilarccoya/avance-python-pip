# Primero: crearemos dos variables, una que guarde la elección del usuario y otra la de la computadora.
# Cuarto: importaremos ramdon para que la elección de la computadora se aleatoria. Con esto le quitamos los zesgos a las posibilidades de la compuetadora.

import random

# Tercero: agregaremos una tupla para que la computadora tenga la variedad de opciones ideal. Además si en algun momento el usuario elije un valor fuera de los parametros de la tupla se pueda enviar un mensaje que corrija la acción.

options = ("piedra", "papel", "tijera")

U_wins = 0
C_wins = 0

rounds = 1 

while True:

    print("*" * 15)
    print("ROUND", rounds)
    print("*" * 15)

    U_O = input("Piedra, papel o tijera:   ")
    U_O = U_O.lower()

# Quinto: si la opción del usuario no esta en los parametros de la tupla.

    if not U_O in options: 
        print ("Esa elección no es valida")
        continue

    C_O = random.choice(options)

    print ("Computadora:  ", C_O)
    print ("Usuario:  ", U_O)

# Segundo: usamos las condicionales y analizamos cada uno de los eventos posibles, así creamos una secuencia lógica.

    if U_O == C_O: 
    
        print (C_O.title(), " VS ", U_O.title())
        print ("Empate!!!")

    elif U_O == "piedra":
        if C_O == "tijera":
            
            print (C_O.title(), " VS ", U_O.title())
            print ("Ganaste!!!")
            U_wins += 1
        else:
            
            print (C_O.title(), " VS ", U_O.title())
            print ("Perdiste")
            C_wins += 1

    elif U_O == "papel":
        if C_O == "piedra":
            
            print (C_O.title(), " VS ", U_O.title())
            print ("Ganaste!!!")
            U_wins += 1

        else:
            
            print (C_O.title(), " VS ", U_O.title())
            print ("Perdiste")
            C_wins += 1


    elif U_O == "tijera":
        if C_O == "papel":
            
            print (C_O.title(), " VS ", U_O.title())
            print ("Ganaste!!!")
            U_wins += 1

        else:
            
            print (C_O.title(), " VS ", U_O.title())
            print ("Perdiste")
            C_wins += 1

    if  C_wins == 3:
        print ("VICTORIA de la computadora")
        break

    if  U_wins == 3:
        print ("VICTORIA del usuario!!!!!!")
        break

    rounds += 1 
    



