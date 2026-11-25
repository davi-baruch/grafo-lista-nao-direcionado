from meu_grafo_matriz_adj_dir import MeuGrafo

grafo = MeuGrafo()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")

grafo.adiciona_aresta("a1", "A", "B")
grafo.adiciona_aresta("a2", "A", "D")
grafo.adiciona_aresta("a3", "B", "C")
grafo.adiciona_aresta("a3", "C", "A")

print(grafo.matriz_binaria())