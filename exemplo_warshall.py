# Exemplo de grafo representado por matriz de adjacencia

vertices = ["A", "B", "C", "D"]

matriz = [
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]


def imprimir_matriz(matriz_adjacencia):
    print("   " + "  ".join(vertices))
    for vertice, linha in zip(vertices, matriz_adjacencia):
        print(vertice, linha)


def warshall(matriz_adjacencia):
    copia_matriz = [linha.copy() for linha in matriz_adjacencia]
    n = len(copia_matriz)

    for i in range(n):
        for j in range(n):
            if copia_matriz[i][j] == 1:
                for k in range(n):
                    if copia_matriz[i][k] == 1:
                        copia_matriz[i][k] = 1

    return copia_matriz
    
print("Matriz de adjacencia:")
imprimir_matriz(matriz)

print("\nMatriz de alcançabilidade:")
warshall(matriz)