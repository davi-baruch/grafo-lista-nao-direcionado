## Exemplo simples do algoritmo de dijkstra

grafo = {
    'A': {'B': 8, 'C': 2, 'D': 5, 'E': 4},
    'B': {'D': 7, 'E': 10},
    'C': {'D': 3},
    'D': {'E': 2},
    'E': {},
}

def dijkstra(grafo, inicio, destino):
    if destino not in grafo:
        print("Vértice inválido")

    # Começa com todos os vértice igual a infinito
    distancias = {vertice: float("inf") for vertice in grafo}
    distancias[inicio] = 0

    # Guarda os vértices predecessores
    predecessores = {}

    # Guarda os vértices que ainda não foram visitados
    nao_visitados = list(grafo.keys())

    while nao_visitados:
        # Pega o menor valor do vértice que ainda não foi visitado
        atual = min(nao_visitados, key=lambda v:distancias[v])

        # Se o vértice atual for igual o vértice de destino
        if (atual == destino) or (distancias[atual] == float("inf")):
            break

        # Verifica todos os vizinho adjacentes ao vértice atual
        for vizinho, peso in grafo[atual].items():
            nova_distancia = distancias[atual] + peso

            # Se encontrou um caminho menor que o atual, atualiza
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = atual

        # Marca o vértice como visitado
        nao_visitados.remove(atual)

        # Reconstrói o caminho de trás pra frente
        menor_caminho = []
        passo = destino
        while passo in predecessores:
            menor_caminho.insert(0, passo)
            passo = predecessores[passo]

        if menor_caminho:
            menor_caminho.insert(0, inicio)

    return distancias[destino], menor_caminho
        
resultado = dijkstra(grafo, "A", "F")

print(resultado)