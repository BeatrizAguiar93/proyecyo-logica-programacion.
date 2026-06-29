# Posición inicial de la serpiente
x = 5
y = 5

while True:

    # Mostrar tablero
    for fila in range(11):
        for columna in range(11):
            if fila == y and columna == x:
                print("S", end=" ")
            else:
                print(".", end=" ")
        print()

    # Mostrar posición
    print(f"\nPosición: ({x}, {y})")

    # Pedir movimiento
    movimiento = input("Mover (w=arriba, s=abajo, a=izquierda, d=derecha): ")

    # Movimiento con if, elif y else
    if movimiento == "w":
        y -= 1

    elif movimiento == "s":
        y += 1

    elif movimiento == "a":
        x -= 1

    elif movimiento == "d":
        x += 1

    else:
        print("Movimiento no válido.")

    # Verificar límites
    if x < 0 or x > 10 or y < 0 or y > 10:
        print("\n¡GAME OVER!")
        break

    print("\n" * 3)