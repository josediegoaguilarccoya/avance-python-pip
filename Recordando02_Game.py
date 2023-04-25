# Primero: crearemos dos variables, una que guarde la elección del usuario y otra la de la computadora.

U_O = input("Piedra, papel o tijera:   ")
U_O = U_O.lower()

C_O = "papel"

# Segundo: usamos las condicionales y analizamos cada uno de los events posibles, así creamos una secuencia lógica.

if U_O == C_O: 
    print ("Computadora:  ", C_O)
    print ("Usuario:  ", U_O)
    print (C_O.title(), " VS ", U_O.title())
    print ("Empate!!!")

elif U_O == "piedra":
    if C_O == "tijera":
        print ("Computadora:  ", C_O)
        print ("Usuario:  ", U_O)
        print (C_O.title(), " VS ", U_O.title())
        print ("Ganaste!!!")
    else:
        print ("Computadora:  ", C_O)
        print ("Usuario:  ", U_O)
        print (C_O.title(), " VS ", U_O.title())
        print ("Perdiste")

elif U_O == "papel":
    if C_O == "piedra":
        print ("Computadora:  ", C_O)
        print ("Usuario:  ", U_O)
        print (C_O.title(), " VS ", U_O.title())
        print ("Ganaste!!!")
    else:
        print ("Computadora:  ", C_O)
        print ("Usuario:  ", U_O)
        print (C_O.title(), " VS ", U_O.title())
        print ("Perdiste")

elif U_O == "tijera":
    if C_O == "papel":
        print ("Computadora:  ", C_O)
        print ("Usuario:  ", U_O)
        print (C_O.title(), " VS ", U_O.title())
        print ("Ganaste!!!")
    else:
        print ("Computadora:  ", C_O)
        print ("Usuario:  ", U_O)
        print (C_O.title(), " VS ", U_O.title())
        print ("Perdiste")

    



