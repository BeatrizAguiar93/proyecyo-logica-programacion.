#juego_serpiente
#IMPORTACION DE VARIBLES

import random
import sys 
# DECLARACION DE VARIABLES

x = 5
y = 5
foot_x = (random.randint(0,10))
foot_y = (random.randint(0,10))

#INTRUCCIONES

print("inicio")
print("usa: w:arriba s:abajo a:izquierda d:abajo")

# INICIO DEL JUEGO

while True:
    print(f"\nposicion actual: ({x}),{y}")
    direccion=input("direccion:")
# CREACION DE COMIDA
    
    if x == food_x and y == food_y:
        food_x = random.randint(0, 9)
        food_y = random.randint(0, 9)
        
#

    if direccion == "w":
        y+= 1

    elif direccion == "s":
        y -= 1

    elif direccion == "a":
        x-=1

    elif direccion == "d":
        x+=1
    else:
        print("direccion no valida")
    continue

    if x<0 or x > 10  or  y < 0 or y >10:
        print("!game over¡ saliste del tablero.")
    break

    for fila in range(11):
        for columna in range(11):
            if fila == y and columna == x:
                print("s", end="")
            
            else:
                print(".", end="")
        print()