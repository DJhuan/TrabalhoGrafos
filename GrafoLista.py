class GrafoLista:
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
        self.lista = {}

        filtroPond = None


        if len(arestas) > 0:
            if (self.ponderado):
                if len(arestas[0]) < 3: raise IndexError("Não há dados para ponderar as arestas")
                filtroPond = self.__tupla_Ponderada
            else:
                filtroPond = self.__tupla_naoPonderada


        if self.direcioando:
            for v in self.vertices:
                self.lista[v] = self.__tuplas_paraDirecionado(v, arestas, filtroPond)
        else:
            for v in self.vertices:
                self.lista[v] = []

            for aresta in arestas:
                self.lista[aresta[0]].append(filtroPond(aresta))
                self.lista[aresta[1]].append(filtroPond((aresta[1], aresta[0], aresta[2])))

        
    def add_vertice(self, nomeVertice):
        if nomeVertice not in self.vertices:
            self.vertices.append(nomeVertice)
            self.lista[nomeVertice] = []

    def add_aresta(self, v1, v2, peso):
        if not self.ponderado: peso = None
        if v1 not in self.lista: self.add_vertice(v1)
        if v2 not in self.lista: self.add_vertice(v2)
        self.lista[v1].append((v2, peso))

        if not self.direcioando:
            self.lista[v2].append((v1, peso))

    def rem_aresta(self, v1, v2, pond=None):
        """Recebe os vértices v1 2 v2 que correspondem a uma aresta, não retorna nada."""
        if v1 not  in self.lista or v2 not  in self.lista:
            raise IndexError("Os vértices fornecidos não existem")
        
        # Para cada tupla que representa uma aresta, no dicionário de v1, verifica se existe a tupla (v2, peso);
        for tupla in self.lista[v1]:
            if tupla == (v2, pond):
                self.lista[v1].remove(tupla)
                if not self.direcioando: self.lista[v2].remove((v1, pond))
        
                
    def rem_vertice(self, v):
        """Recebe a aresta que será removida, não retornando nada."""
        if not self.direcioando:
            arestas = self.lista[v]
            for aresta in arestas:
                self.lista[aresta[0]].remove((v, aresta[1]))
            
        self.lista.pop(v)
        self.vertices.remove(v)

    def __tuplas_paraDirecionado(self, vertice, arestas, filtro):
        """Organiza uma lista de tuplas de um único vértice. O argumento 'filtro'
é usado como forma de padronizar a ponderação dos vértices. Ex.: se o arquivo fornece
os pesos de cada vértice, e o grafo é não ponderado, o filtro pode normalizar esse valor para 'None'."""
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
