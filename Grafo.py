class Grafo:
    def __init__(self, vertices, arestas, direcionado, ponderado):
        """Construtor da classe"""
        self.vertices = {}
        for i, vertice in enumerate(vertices):
            self.vertices[vertice] = i

        self.direcionado = direcionado
        self.ponderado = ponderado
        self.lista = {}

        ### GRAFO EM MATRIZ

        self.matriz = [[None]*len(self.vertices) for _ in range(len(self.vertices))]     

        filtro = None
        if len(arestas) > 0:
            if (self.ponderado):
                if len(arestas[0]) < 3: raise IndexError("Não há dados para ponderar as arestas")
                filtro = self.__MATRIZ_tupla_ponderada
            else:
                filtro = self.__MATRIZ_tupla_naoPonderada

        v = self.vertices
        if self.direcionado :
            for aresta in arestas:
                print(aresta)
                self.matriz[v[aresta[0]]][v[aresta[1]]] = filtro(aresta)
        else:
            for aresta in arestas:
                self.matriz[v[aresta[0]]][v[aresta[1]]] = filtro(aresta)
                self.matriz[v[aresta[1]]][v[aresta[0]]] = filtro(aresta)

        print(arestas)

        ### GRAFO EM LISTA
        filtroPond = None

        if len(arestas) > 0:
            if (self.ponderado):
                if len(arestas[0]) < 3: raise IndexError("Não há dados para ponderar as arestas")
                filtroPond = self.__LISTA_tupla_Ponderada
            else:
                filtroPond = self.__LISTA_tupla_naoPonderada


        if self.direcionado:
            for v in self.vertices:
                self.lista[v] = self.__tuplas_paraDirecionado(v, arestas, filtroPond)
        else:
            for v in self.vertices:
                self.lista[v] = []

            for aresta in arestas:
                self.lista[aresta[0]].append(filtroPond(aresta))
                self.lista[aresta[1]].append(filtroPond((aresta[1], aresta[0], aresta[2])))


    def __tuplas_paraDirecionado(self, vertice, arestas, filtro):
        """Organiza uma lista de tuplas de um único vértice. O argumento 'filtro'
é usado como forma de padronizar a ponderação dos vértices. Ex.: se o arquivo fornece
os pesos de cada vértice, e o grafo é não ponderado, o filtro pode normalizar esse valor para 'None'."""
        listaAdj = [filtro(aresta) for aresta in arestas if aresta[0] == vertice]

        return listaAdj
    
    def __str__(self):
        matriz = ""
        for i in self.vertices:
            i = self.vertices[i]
            for j in self.matriz[i]:
                matriz += "{:>4}".format(str(j)) + ' '
            matriz += '\n'
        return matriz

    @staticmethod
    def __LISTA_tupla_naoPonderada(tupla):
        return (tupla[1], None)
    
    def __LISTA_tupla_Ponderada(self, tupla):
        return (tupla[1], tupla[2])
    
    def __MATRIZ_tupla_ponderada(self, tupla): return (tupla[2])
    def __MATRIZ_tupla_naoPonderada(self, tupla): return 0
        
if __name__ == "__main__":
    v = ["A", "B", "C", "D"]
    a = [("A", "A", 14), ("A", "B", 3), ("A", "C", 2), ("A", "D", 0)]
    g = Grafo(v, a, False, True)
    print(g)
    print(g.lista)