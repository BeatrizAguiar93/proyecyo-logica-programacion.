#juego_serpiente

x = 5
y = 5

print("inicio")
print("usa: w:arriba s:abajo a:izquierda d:abajo")

while True:
    print(f"\nposicion actual: ({x}),{y}")
    direccion=input("direccion:")

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