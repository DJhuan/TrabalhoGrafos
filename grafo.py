class Grafo:
    """Implementação da classe Grafo usando lista de adjacência.
    """

    def __init__(self, vertices=[], arestas=[], direcd=False, pondr=False):
        """Construtor da classe
        Recebe:
            Lista de vértices ex.: [1, 2, 3];
            Lista de arestas como tuplas ex.: [(1,2), (1,3), (2,3)];
            Booleano se é direcionado;
            Booleano se é ponderado.
        """

        self.vertices = vertices
        self.direcioando = direcd
        self.ponderado = pondr

        self.arestas = {}

        filtroPond = None

        if (self.ponderado):
            if len(arestas) > 0:
                if len(arestas[0]) < 3: raise IndexError("Não há dados para ponderar as arestas")
            filtroPond = self.__tupla_Ponderada
        else:
            filtroPond = self.__tupla_naoPonderada


        if self.direcioando:
            for v in self.vertices:
                self.arestas[v] = self.__tuplas_paraDirecionado(v, arestas, filtroPond)
        else:
            for v in self.vertices:
                self.arestas[v] = []

            for aresta in arestas:
                self.arestas[aresta[0]].append(filtroPond(aresta))
                self.arestas[aresta[1]].append(filtroPond((aresta[1], aresta[0], aresta[2])))

        
    def add_vertice(self, nomeVertice):
        self.vertices.append(nomeVertice)

    def add_aresta(self, v1, v2, peso):
        if not self.ponderado: peso = None
        self.arestas[v1].append((v2, peso))
        if not self.direcioando:
            self.arestas[v2].append((v1, peso))

    def rem_aresta(self, v1, v2, pond=None):
        for tupla in self.arestas[v1]:
            if tupla == (v2, pond):
                self.arestas[v1].remove(tupla)
                if not self.direcioando: self.arestas[v2].remove((v1, pond))
    
    def rem_vertice(self, v):
        for aresta in self.arestas[v]:
            self.arestas[v].remove(aresta)
            if not self.direcioando:
                self.arestas[aresta[0]].remove((v, aresta[1]))
            
        self.arestas.pop(v)
        self.vertices.remove(v)

    def __tuplas_paraDirecionado(self, vertice, arestas, filtro):
        listaAdj = []
        for i, aresta in enumerate(arestas):
            if aresta[0] == vertice:
                listaAdj.append(filtro(aresta))
                arestas.pop(i)

        return listaAdj    

    @staticmethod
    def __tupla_naoPonderada(tupla):
        return (tupla[1], None)
    
    def __tupla_Ponderada(self, tupla):
        return (tupla[1], tupla[2])
