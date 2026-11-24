from grafo_lista_adj_test_nao_dir import MeuGrafo

grafo = MeuGrafo()

grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")

grafo.adiciona_aresta("a1", "A", "B", 3)
grafo.adiciona_aresta("a2", "A", "C", 2)
grafo.adiciona_aresta("a3", "A", "D", 2)
grafo.adiciona_aresta("a4", "B", "D", 4)
grafo.adiciona_aresta("a5", "B", "E", 10)
grafo.adiciona_aresta("a6", "C", "D", 5)
grafo.adiciona_aresta("a7", "C", "E", 7)
grafo.adiciona_aresta("a8", "D", "E", 9)

x = grafo.dijkstra("A", "E")
print(x)