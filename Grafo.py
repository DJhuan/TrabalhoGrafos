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
        """Método chamado implicitamente pelo interpretador. 
Não recebe nada e retorna uma string que representa tanto a matriz
quanto a lista de adjacência."""
        string = ""
        for i in self.vertices:
            i = self.vertices[i]
            for j in self.matriz[i]:
                string += "{:>4}".format(str(j)) + ' '
            string += '\n'

        for key in self.lista:
            string += f"{key}: {str(self.lista[key])}\n"
            
        return string
    
    def AdicionarArestas(self, v1, v2, valor=0):
        """Adiciona a aresta a partir de dois vértices recebidos e um valor. Não retorna nada."""
        self.matriz[self.vertices[v1]][self.vertices[v2]] = valor
        self.lista[v1].append((v2, valor))

        if not self.direcionado:
            self.matriz[self.vertices[v2]][self.vertices[v1]] = valor
            self.lista[v2].append((v1, valor))

    def RemoverArestas(self, v1, v2):
        """Recebe os vértices v1 2 v2 que correspondem a uma aresta, não retorna nada."""
        if v1 not  in self.lista or v2 not  in self.lista:
            raise IndexError("Os vértices fornecidos não existem")
        self.matriz[self.vertices[v1]][self.vertices[v2]] = None
        if not self.direcionado:
            self.matriz[self.vertices[v2]][self.vertices[v1]] = None
        
        for tupla in self.lista[v1]:
            if tupla[0] == v2:
                self.lista[v1].remove(tupla)
                if not self.direcionado:
                    for tupla2 in self.lista[v2]:
                        if tupla2[0] == v1:
                            self.lista[v2].remove(tupla2)

    def AdicionarVertice(self, vertice):
        """Adiciona um novo vértice ao grafo e atualiza a matriz e a lista de adjacências."""
        if vertice in self.vertices:
            print(f"Vértice '{vertice}' já existe.")
        else:
            i = len(self.vertices)
            self.vertices[vertice] = i
            for linha in self.matriz:
                linha.append(None)
            self.matriz.append([None] * (i + 1))
            self.lista[vertice] = []

            for v in self.lista:
                self.lista[v].append((vertice, None))

    def RemoverVertice(self, vertice):
        """Remove um vértice do grafo e atualiza a matriz e a lista de adjacências."""
        if vertice not in self.vertices:
            print(f"Vértice '{vertice}' não existe.")
        else:
            i = self.vertices[vertice]

            self.matriz.pop(i)
            for linha in self.matriz:
                linha.pop(i)

            self.lista.pop(vertice)
            for chave in self.lista:
                self.lista[chave] = [(v, peso) for v, peso in self.lista[chave] if v != vertice]

            del self.vertices[vertice]
            for v in self.vertices:
                if self.vertices[v] > i:
                    self.vertices[v] -= 1

    def ArvoreBFS(self, inicial):
        arvore = {}
        for i in self.vertices:
            arvore[i] = []
        visitado = ["N"]*len(self.vertices)
        fila = [inicial]
        visitado[self.vertices[fila[0]]] = "A"

        while fila:
            while fila:
                i = fila.pop(0)
                for j in self.lista[i]:
                    if visitado[self.vertices[j[0]]] == "N":
                        visitado[self.vertices[j[0]]] = "A"
                        fila.append(j[0])
                        arvore[i].append(j)
                visitado[self.vertices[i]] = "V"
            
            cont = 0
            parar = False
            for vertice in self.vertices:
                if visitado[cont] == "N" and not parar:
                    fila.append(vertice)
                    visitado[cont] = "A"
                    parar = True
                cont = cont+1

        return arvore

    @staticmethod
    def __LISTA_tupla_naoPonderada(tupla):
        """Recebe uma tupla (v1, v2, valor) que será formatada 
em uma tupla do tipo aresta não ponderada."""
        return (tupla[1], 0)
    
    def __LISTA_tupla_Ponderada(self, tupla):
        """Recebe uma tupla (v1, v2, valor) que será formatada 
em uma tupla do tipo aresta não ponderada."""
        return (tupla[1], tupla[2])
    
    # As funções abaixo tem o mesmo objetivo das acima, com a diferença que 
    def __MATRIZ_tupla_ponderada(self, tupla): return (tupla[2])
    def __MATRIZ_tupla_naoPonderada(self, _): return 0
        
if __name__ == "__main__":
    v = ["A","B","C","D"]
    a = [("A","A",2), ("A","B",6), ("A","C",9), ("A","D",4)]
    g = Grafo(v, a, False, False)
    g.AdicionarArestas("C","D")
    #g.RemoverArestas("A","B")
    print(g.ArvoreBFS("B"))
    print(g)
