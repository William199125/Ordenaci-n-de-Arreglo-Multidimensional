# Definir la matriz bidimensional 3x3
matriz = [
    [9, 3, 7],
    [1, 5, 8],
    [4, 6, 2]
]

# Función para ordenar una fila específica utilizando Bubble Sort
def bubble_sort_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiar los elementos si están en el orden incorrecto
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1, que es la segunda fila)
fila_a_ordenar = 1

# Ordenar la fila especificada
bubble_sort_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
