# Primero crearemos dos variables, una que guarde la elección del usuario y otra la de la computadora.

U_O = input("Piedra, papel o tijera:   ")

C_O = "papel"

if U_O == C_O: 
    print ("Empate!!!")

elif U_O == "piedra":
    if C_O == "tijera":
        print ("Ganaste!!!")
    else:
        print ("Perdiste")

elif U_O == "papel":
    if C_O == "piedra":
        print ("Ganaste!!!")
    else:
        print ("Perdiste")

elif U_O == "tijera":
    if C_O == "papel":
        print ("Ganaste!!!")
    else:
        print ("Perdiste")



