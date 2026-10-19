import unittest
from bibgrafo.grafo_errors import VerticeInvalidoError
from meu_grafo_lista_adj_nao_dir import MeuGrafo


def cria_grafo(vertices, arestas):
    g = MeuGrafo()
    for v in vertices:
        g.adiciona_vertice(v)
    for rotulo, v1, v2 in arestas:
        g.adiciona_aresta(rotulo, v1, v2)
    return g


class TestBuscas(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba (com arestas paralelas)
        self.g_p = cria_grafo(
            ['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
            [
                ('a1', 'J', 'C'),
                ('a2', 'C', 'E'),
                ('a3', 'C', 'E'),
                ('a4', 'P', 'C'),
                ('a5', 'P', 'C'),
                ('a6', 'T', 'C'),
                ('a7', 'M', 'C'),
                ('a8', 'M', 'T'),
                ('a9', 'T', 'Z'),
            ],
        )
        # Grafo com laço e um vértice isolado (D)
        self.g_l = cria_grafo(
            ['A', 'B', 'C', 'D'],
            [
                ('a1', 'A', 'A'),
                ('a2', 'A', 'B'),
                ('a3', 'B', 'C'),
                ('a4', 'A', 'C'),
            ],
        )

    def test_dfs(self):
        esperado_j = cria_grafo(
            ['J', 'C', 'E', 'P', 'T', 'M', 'Z'],
            [
                ('a1', 'J', 'C'),
                ('a2', 'C', 'E'),
                ('a4', 'C', 'P'),
                ('a6', 'C', 'T'),
                ('a8', 'T', 'M'),
                ('a9', 'T', 'Z'),
            ],
        )
        self.assertEqual(self.g_p.dfs('J'), esperado_j)

        esperado_z = cria_grafo(
            ['Z', 'T', 'C', 'J', 'E', 'P', 'M'],
            [
                ('a9', 'Z', 'T'),
                ('a6', 'T', 'C'),
                ('a1', 'C', 'J'),
                ('a2', 'C', 'E'),
                ('a4', 'C', 'P'),
                ('a7', 'C', 'M'),
            ],
        )
        self.assertEqual(self.g_p.dfs('Z'), esperado_z)

    def test_bfs(self):
        esperado_j = cria_grafo(
            ['J', 'C', 'E', 'P', 'T', 'M', 'Z'],
            [
                ('a1', 'J', 'C'),
                ('a2', 'C', 'E'),
                ('a4', 'C', 'P'),
                ('a6', 'C', 'T'),
                ('a7', 'C', 'M'),
                ('a9', 'T', 'Z'),
            ],
        )
        x = self.g_p.bfs('J')
        self.assertEqual(x, esperado_j)

        esperado_z = cria_grafo(
            ['Z', 'T', 'C', 'M', 'J', 'E', 'P'],
            [
                ('a9', 'Z', 'T'),
                ('a6', 'T', 'C'),
                ('a8', 'T', 'M'),
                ('a1', 'C', 'J'),
                ('a2', 'C', 'E'),
                ('a4', 'C', 'P'),
            ],
        )
        self.assertEqual(self.g_p.bfs('Z'), esperado_z)

    def test_laco_e_vertice_isolado(self):
        # DFS desce por B antes de voltar a A; BFS pega C direto de A
        self.assertEqual(
            self.g_l.dfs('A'),
            cria_grafo(['A', 'B', 'C'], [('a2', 'A', 'B'), ('a3', 'B', 'C')]),
        )
        self.assertEqual(
            self.g_l.bfs('A'),
            cria_grafo(['A', 'B', 'C'], [('a2', 'A', 'B'), ('a4', 'A', 'C')]),
        )

        # A partir de um vértice isolado, a árvore tem só a raiz
        self.assertEqual(self.g_l.dfs('D'), cria_grafo(['D'], []))
        self.assertEqual(self.g_l.bfs('D'), cria_grafo(['D'], []))

    def test_quantidade_de_arestas(self):
        for v in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            for arvore in (self.g_p.dfs(v), self.g_p.bfs(v)):
                self.assertEqual(len(arvore.vertices), 7)
                self.assertEqual(len(arvore.arestas), 6)

    def test_nao_modifica_grafo_original(self):
        antes = str(self.g_p)
        self.g_p.dfs('J')
        self.g_p.bfs('J')
        self.assertEqual(str(self.g_p), antes)

    def test_vertice_inexistente(self):
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.dfs('X')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.bfs('X')


if __name__ == '__main__':
    unittest.main()