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
    
    def AdicionarArestas(self, v1, v2, valor):
        aresta = (v1, v2, valor)
        (v1, v2) = (self.vertices[v1], self.vertices[v2])
        self.matriz[v1][v2] = valor
        if self.direcionado == 0:
            self.matriz[v2][v1] = valor

        if self.ponderado:
            filtroPond = self.__LISTA_tupla_Ponderada
        else:
            filtroPond = self.__LISTA_tupla_Ponderada

        if self.direcionado:
            self.lista[aresta[0]].append(filtroPond(aresta))
        else:
            self.lista[aresta[0]].append(filtroPond(aresta))
            self.lista[aresta[1]].append(filtroPond((aresta[1], aresta[0], aresta[2])))

    def RemoverArestas(self, v1, v2):
        """Recebe os vértices v1 2 v2 que correspondem a uma aresta, não retorna nada."""
        if v1 not  in self.lista or v2 not  in self.lista:
            raise IndexError("Os vértices fornecidos não existem")
        self.matriz[self.vertices[v1]][self.vertices[v2]] = None
        if not self.direcionado:
            self.matriz[self.vertices[v2]][self.vertices[v1]] = None
        
        # Para cada tupla que representa uma aresta, no dicionário de v1, verifica se existe a tupla (v2, peso);
        for tupla in self.lista[v1]:
            if tupla[0] == v2:
                self.lista[v1].remove(tupla)
                if not self.direcionado:
                    for tupla2 in self.lista[v2]:
                        if tupla2[0] == v1:
                            self.lista[v2].remove(tupla2)


    @staticmethod
    def __LISTA_tupla_naoPonderada(tupla):
        return (tupla[1], None)
    
    def __LISTA_tupla_Ponderada(self, tupla):
        return (tupla[1], tupla[2])
    
    def __MATRIZ_tupla_ponderada(self, tupla): return (tupla[2])
    def __MATRIZ_tupla_naoPonderada(self, tupla): return 0
        
if __name__ == "__main__":
    v = ["A","B","C","D"]
    a = [("A","A",2), ("A","B",6), ("A","C",9), ("A","D",4)]
    g = Grafo(v, a, True, True)
    g.AdicionarArestas("C","D",1)
    g.RemoverArestas("A","B")
    print(g)
    print(g.lista)