import collections
from collections import *

from bibgrafo import aresta
from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {'X-Z', 'X-W', ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        vertices = self.vertices
        pares_nao_adjacentes = set()

        for v in range(len(vertices)):
            for i in range(v + 1, len(vertices)):
                u = vertices[v]
                j = vertices[i]

                sao_adjacentes = False

                for aresta in self.arestas.values():
                    v1 = aresta.v1.rotulo
                    v2 = aresta.v2.rotulo

                    if (v1 == u.rotulo and v2 == j.rotulo) or (v1 == j.rotulo and v2 == u.rotulo):
                        sao_adjacentes = True
                        break

                # adicionar um par de set se não achar nenhuma aresta
                if not sao_adjacentes:
                    par = f"{u.rotulo}-{j.rotulo}"
                    pares_nao_adjacentes.add(par)

        return pares_nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        lacos = []

        for aresta in self.arestas.values():
            if aresta.v1 == aresta.v2:
                lacos.append(aresta.rotulo)

        qnt = len(lacos)

        if qnt > 0:
            return True
        else:
            return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        qnt = 0

        for aresta in self.arestas.values():
            v1 = aresta.v1.rotulo
            v2 = aresta.v2.rotulo

            if v1 == V and v2 == V:
                qnt += 2
            elif v1 == V or v2 == V:
                qnt += 1

        return qnt

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas = list(self.arestas.values())
        qnt = 0

        for i in range(len(arestas)):
            for j in range(i + 1, len(arestas)):

                a1 = arestas[i]
                a2 = arestas[j]

                if (a1.v1 == a2.v1 and a1.v2 == a2.v2) or (a1.v1 == a2.v2 and a1.v2 == a2.v1):
                    return True

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê um set que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        # if not self.existe_rotulo_vertice(V):
        #     raise VerticeInvalidoError()

        arestas = set()

        for aresta, vertice in self.arestas.items():
            v1 = vertice.v1.rotulo
            v2 = vertice.v2.rotulo

            if V == v1 or V == v2:
                arestas.add(aresta)

        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''

        # Não pode ter laço
        if self.ha_laco():
            return False

        # Não pode ter arestas paralelas
        if self.ha_paralelas():
            return False

        # Deve ter todos os vértices adjacentes
        vertices_adjacentes = self.vertices_nao_adjacentes()

        if len(vertices_adjacentes) > 0:
            return False

        return True

    def outra_ponta(self, a, V: str):
        """Dada uma aresta incidente em V, retorna o rótulo da outra ponta."""
        a = self.get_aresta(a)

        if a.v1.rotulo == V:
            return a.v2.rotulo
        elif a.v2.rotulo == V:
            return a.v1.rotulo

    def dfs(self, V=''):
        """
        Executa a busca em profundidade a partir do vértice de rótulo V.
        Returns: a árvore DFS como um MeuGrafo.
        Raises: VerticeInvalidoError se V não existe no grafo.
        """
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        self.get_vertice(V)

        arvore = MeuGrafo()
        arvore.adiciona_vertice(V)
        visitados = set()
        visitados.add(V)

        def visita(u):
            vizinhos = []

            for aresta in self.arestas_sobre_vertice(u):
                w = self.outra_ponta(aresta, u) # retorna o outro vértice
                vizinhos.append((w, aresta))

            for w, aresta in vizinhos:
                if w not in visitados:
                    visitados.add(w)
                    arvore.adiciona_vertice(w)
                    arvore.adiciona_aresta(aresta, u, w)
                    visita(w)

        visita(V)
        return arvore

    def bfs(self, V=''):
        """
        Executa a busca em largura a partir do vértice de rótulo V.
        Returns: a árvore BFS como um MeuGrafo.
        Raises: VerticeInvalidoError se V não existe no grafo.
        """
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        arvore = MeuGrafo()
        arvore.adiciona_vertice(V)

        fila = collections.deque()
        fila.append(V)

        visitados = set()
        visitados.add(V)

        while len(fila) > 0:
            u = fila.popleft()
            vizinhos = []

            for aresta in self.arestas_sobre_vertice(u):
                w = self.outra_ponta(aresta, u)
                vizinhos.append((w, aresta))

            # ordenar vizinhos
            vizinhos.sort(key=lambda x: (x[0], x[1]))

            for w, aresta in vizinhos:
                if w not in visitados:
                    visitados.add(w)
                    arvore.adiciona_vertice(w)
                    arvore.adiciona_aresta(aresta, u, w)
                    fila.append(w)

        return arvore