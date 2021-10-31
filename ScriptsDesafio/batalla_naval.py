import numpy as np

# Tablero de la flota
naves = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

def tablero_naves(naves):
    # Dibuja el tablero de la flota
    print("    A    B    C    D    E")
    num_fila = 1
    for fila in naves:
        print(num_fila, fila)
        num_fila = num_fila + 1


# Bucle for para insertar cinco naves al azar
for n in range(5):
    num_fila = np.random.choice(5,5,replace=False)
    num_col = np.random.choice(5,5,replace=False)
    naves[num_fila[n]][num_col[n]] = 'X'
tablero_naves(naves)


# Limpiar la pantalla para que el Destructor no vea donde estan las naves
print("\n"*50)
print("Comienzan los disparos!!")
disparos = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]


# El juego concluye al alcanzar 20 disparos o hundir las cinco naves
num_disparos = 0
naves_hundidas = 0
# Funcion para ubicar los disparos
def ubica_disparo():
    columna = input("Ingrese columna (1 a 5): ")
    while columna not in "12345":
        print("Columna equivocada! ")
        columna = input("Ingrese columna (1 a 5): ")

    fila = input("Ingrese fila (1 a 5): ")
    while fila not in "12345":
        print("Fila equivocada!")
        fila = input("Ingrese fila (1 a 5):")

    return int(fila) - 1, int(columna) - 1

while num_disparos < 20 and naves_hundidas < 5:
    print("Ubique un disparo")
    num_fila, num_col = ubica_disparo()

    if naves[num_fila][num_col] == 'X':
        print("Hundido!")
        disparos[num_fila][num_col] = 'X'
        num_disparos = num_disparos + 1
        naves_hundidas = naves_hundidas + 1
    else:
        disparos[num_fila][num_col] = '.'
        print("Agua!")
        num_disparos = num_disparos + 1

    tablero_naves(disparos)
    
print("Terminado!")
