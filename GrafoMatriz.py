class GrafoMatriz:
    def __init__(self, vertices, arestas, direcionado, ponderado):
        self.vertices = {}
        for i, vertice in enumerate(vertices):
            self.vertices[vertice] = i

        self.grafo = [[None]*len(self.vertices) for _ in range(len(self.vertices))]
        self.direcionado = direcionado
        self.ponderado = ponderado           

        filtro = None
        if len(arestas) > 0:
            if (self.ponderado):
                if len(arestas[0]) < 3: raise IndexError("Não há dados para ponderar as arestas")
                filtro = self.__tupla_ponderada
            else:
                filtro = self.__tupla_naoPonderada

        v = self.vertices
        if self.direcionado :
            for aresta in arestas:
                self.grafo[v[aresta[0]]][v[aresta[1]]] = filtro(aresta)
        else:
            for aresta in arestas:
                self.grafo[v[aresta[0]]][v[aresta[1]]] = filtro(aresta)
                self.grafo[v[aresta[1]]][v[aresta[0]]] = filtro(aresta)

    def AdicionarArestas(self, v1, v2, valor):
        (v1, v2) = (self.vertices[v1], self.vertices[v2])
        self.grafo[self.vertices[v1]][v2] = valor
        if self.direcionado == 0:
            self.grafo[v2][v1] = valor

    def RemoverArestas(self, v1, v2):
        self.grafo[self.vertices[v1]][self.vertices[v2]] = None
        if self.direcionado == 0:
            self.grafo[self.vertices[v2]][self.vertices[v1]] = None

    def AdicionarVertice(self, vName):
        numVertice = len(self.vertices)
        self.vertices[vName] = numVertice
        for i in range(numVertice):
            self.grafo[i].append(None)
        self.grafo.append([None]*(numVertice + 1))

    def __str__(self):
        matriz = ""
        for i in self.vertices:
            i = self.vertices[i]
            for j in self.grafo[i]:
                matriz += "{:>4}".format(str(j)) + ' '
            matriz += '\n'
        return matriz

    @staticmethod
    def __tupla_ponderada(tupla): return (tupla[2])
    def __tupla_naoPonderada(self, tupla): return 0

if __name__ == "__main__":
    v = ["A", "B", "C", "D"]
    a = [("A", "B", 2), ("C", "D", 7)]
    g = GrafoMatriz(v, a, False, True)
    print(g.vertices, '\n')
    print(g)

    g.RemoverArestas("A", "B")
    print(g)

    g.AdicionarVertice("S")
    print(g.vertices, '\n')
    print(g)
