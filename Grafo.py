class Grafo:
    def __init__(self, vertices=[], arestas=[], direcionado=True, ponderado=False):
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
                if not (aresta[0] == aresta[1]):
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
        string = "=== MATRIZ ===\n"
        for v in self.vertices:
            i = self.vertices[v]
            for j in self.matriz[i]:
                string += "{:>4}".format(str(j)) + ' '
            string += '\n'
        string += "\n=== LISTA ===\n"
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
        """Recebe os vértices v1 e v2 que correspondem a uma aresta e a remove. Não retorna nada."""
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
        """Recebe um vértice inicial e realiza a busca em largura a partir dele. Retorna a árvore de busca 
        em largura na forma de lista."""
        arvore = {}
        visitado = ["N"]*len(self.vertices) #Lista de todos os vértices, que informa o estado atual de cada vértice.
        #"N": ainda não foi encontrado.
        #"A": foi encontrado, mas não foi explorado.
        #"V": foi explorado.
        fila = [inicial]
        visitado[self.vertices[fila[0]]] = "A"

        while fila:
            while fila:
                i = fila.pop(0)
                arvore[i] = []
                for j in self.lista[i]:
                    if visitado[self.vertices[j[0]]] == "N":
                        visitado[self.vertices[j[0]]] = "A"
                        fila.append(j[0])
                        arvore[i].append(j)
                visitado[self.vertices[i]] = "V"
            
            #Verifica se há algum vértice que não está conectado aos já explorados.
            cont = 0
            parar = False
            for vertice in arvore:
                if visitado[cont] == "N" and not parar:
                    fila.append(vertice)
                    visitado[cont] = "A"
                    parar = True
                cont = cont+1
        return arvore

    def ArvoreDFS(self, inicial):
        """Faz uma busca em profundidade a partir de um vértice inicial e retorna uma arvore DFS."""
        arvore = {}
        for i in self.vertices:
            arvore[i] = []
        visitado = ["N"]*len(self.vertices)
        pilha = [inicial]
        visitado[self.vertices[inicial]] = "A"

        while pilha:
            i = pilha.pop()
            if visitado[self.vertices[i]] == "A":
                for j in self.lista[i]:
                    if visitado[self.vertices[j[0]]] == "N":
                        visitado[self.vertices[j[0]]] = "A"
                        pilha.append(j[0])
                        arvore[i].append(j)
                visitado[self.vertices[i]] = "V"

        cont = 0
        parar = False
        while cont < len(visitado) and not parar:
            if visitado[cont] == "N":
                pilha.append(list(self.vertices.keys())[cont])
                visitado[cont] = "A"
                parar = True
            cont = cont + 1

        return arvore


    def OrdemTopologica(self):
        """Argoritmo de Kahn. Retorna uma possibilidade de ordem de execução"""
        if self.VerificacoesGrafo("vii") == "O grafo possui ciclos.":
            raise IndexError("O grafo possui ciclos. Não é possível calcular a ordem topológica.")
        grau = {} #Dicionário que contém o grau atual de cada vértice.

        for vertice in self.lista:
            grau[vertice] = 0
        for vertice in self.lista:
            for i in self.lista[vertice]:
                grau[i[0]] += 1

        listaExecucao = []

        while len(listaExecucao) < len(self.vertices):
            for i in grau:
                if grau[i] == 0:
                    listaExecucao.append(i)
                    for j in self.lista[i]:
                        grau[j[0]] -= 1
                    grau[i] = None

        return listaExecucao
    

    def CompConexos(self):
        """Retorna componentes conexos como listas de vértices"""

        if self.direcionado:
            msg = "A função CompConexos não pode ser utilizada em grafos não direcionados!"
            raise(PropriedadesIncompativeis(msg))

        componentes = []
        visitados = [False] * len(self.vertices)

        for vertice in self.vertices:
            verticeId = self.vertices[vertice]
            if not visitados[verticeId]:
                componente = list(self.ArvoreBFS(vertice).keys())
                for v in componente: 
                    visitados[self.vertices[v]] = True

                componentes.append(componente)
                
        return componentes
    
    def CicloArvoreGeradora(self, lista):
        """Transforma o grafo direcionado em não direcionado e verifica o ciclo."""
        arvore2 = {}
        for vertice in lista:
            arvore2[vertice] = []
        for vertice in lista:
            for tupla in lista[vertice]:
                arvore2[vertice].append((tupla[0], tupla[1]))
                if self.direcionado:
                    arvore2[tupla[0]].append((vertice, tupla[1]))
        ciclo = False
        visitado = ["N"]*len(self.vertices)
        pilha = []
        for vertice in arvore2:
            if visitado[self.vertices[vertice]] == "N":
                pilha.append(vertice)
                visitado[self.vertices[vertice]] = "A"
                ciclo = self.verifica_ciclo(vertice, ciclo, visitado, pilha, arvore2, 0)
            
        return ciclo
    
    def ArvoreGeradoraMinima (self):
        listaArestas = [] #configuração: (valor, v1, v2)
        for vertice in self.lista:
            for tupla in self.lista[vertice]:
                if vertice != tupla[0]: #Retira os loops
                    listaArestas.append ((tupla[1],vertice,tupla[0]))
                    if not self.direcionado and (tupla[1], tupla[0], vertice) in listaArestas:
                        listaArestas.remove ((tupla[1],vertice,tupla[0]))
        listaArestas.sort()

        arvore = {}
        for vertice in self.lista:
            arvore[vertice] = []
        
        quantidade = 0
        cont = 0
        qtArestas = len(listaArestas)
        while quantidade < len(self.vertices)-1 and cont < qtArestas:
            cont = cont+1
            aresta = listaArestas.pop(0)
            
            arvore[aresta[1]].append((aresta[2], aresta[0])) 
            if not self.direcionado:
                arvore[aresta[2]].append((aresta[1], aresta[0]))
            
            if self.CicloArvoreGeradora(arvore):
                arvore[aresta[1]].remove((aresta[2], aresta[0]))
                if not self.direcionado:
                    arvore[aresta[2]].remove((aresta[1], aresta[0]))
            else:
                quantidade = quantidade+1

        for i in arvore:
            arvore[i].sort()

        return arvore


    def verifica_ciclo(self, pai, ciclo, visitado, pilha, lista, direcionado):
        """Usa DFS para verificação de ciclo. Se chegar em um vértice que já foi encontrado, mas não explorado, há um ciclo.""" 
        ultimo = len(pilha)-1
        i = pilha[ultimo]
        for j in lista[i]:
            if visitado[self.vertices[j[0]]] == "N":
                visitado[self.vertices[j[0]]] = "A"
                pilha.append(j[0])
                ciclo = self.verifica_ciclo(i, ciclo, visitado, pilha, lista, direcionado)
            elif visitado[self.vertices[j[0]]] == "A" and j[0] != pai:
                return True
            elif direcionado and visitado[self.vertices[j[0]]] == "A": #Se for direcionado e tiver um caminho para o pai, há um ciclo.
                return True
        visitado[self.vertices[i]] = "V"
        ultimo = len(pilha)-1
        pilha.pop(ultimo)
        return ciclo
    
    def Tarjan(self, lista, vertice, visitado, low, tempoD, arestasPonte, tempo, pai, aAnterior):
        """Aplica o método de Tarjan para encontrar arestas ponte"""
        visitado[self.vertices[vertice]] = "A"
        tempoD[self.vertices[vertice]] = tempo
        low[self.vertices[vertice]] = tempo
        for tupla in lista[vertice]:
            if visitado[self.vertices[tupla[0]]] == "N":
                tempo += 1
                self.Tarjan(lista, tupla[0], visitado, low, tempoD, arestasPonte, tempo, vertice, tupla)
                low[self.vertices[vertice]] = min(low[self.vertices[vertice]], low[self.vertices[tupla[0]]])
                if low[self.vertices[tupla[0]]] > tempoD[self.vertices[vertice]]:
                    arestasPonte.append((vertice, tupla[0]))
            elif vertice != tupla[0] and visitado[self.vertices[tupla[0]]] == "A" and (tupla[0] != pai or aAnterior[1] != tupla[1]):
                low[self.vertices[vertice]] = min(low[self.vertices[vertice]], tempoD[self.vertices[tupla[0]]])


        visitado[self.vertices[vertice]] = "V"
    
    def ArestasPonte(self):
        """Transforma o grafo direcionado em não direcionado e chama o método de Tarjan para cada vértice"""
        grafo2 = {}
        for vertice in self.lista:
            grafo2[vertice] = []
        for vertice in self.lista:
            for tupla in self.lista[vertice]:
                grafo2[vertice].append((tupla[0], tupla[1]))
                if self.direcionado:
                    grafo2[tupla[0]].append((vertice, tupla[1]))

        for tupla in grafo2:
            grafo2[tupla].sort()
        print(grafo2)

        visitado = ["N"]*len(self.vertices)
        low = [None]*len(self.vertices)
        tempoD = [None]*len(self.vertices)
        arestasPonte = []
        tempo = 1

        for vertice in self.vertices:
            if visitado[self.vertices[vertice]] == "N":
                self.Tarjan(grafo2, vertice, visitado, low, tempoD, arestasPonte, tempo, vertice, (vertice,0))

        return arestasPonte



    def VerificacoesGrafo(self, opcaoVerificacao):
        """Realiza diferentes verificações no grafo com base na opçao selecionada."""

        if opcaoVerificacao == "i": #quantidade de vertices
            contVertices = len(self.vertices)
            print("Quantidade de Vértices: ", contVertices)

        if opcaoVerificacao == "ii": #quantidade de arestas
            contAresta = 0
            for i in range (len(self.vertices)):
                for j in range (len(self.vertices)):
                    if self.matriz[i][j]:
                        contAresta += 1
            if not self.direcionado:
                contAresta = contAresta // 2
            print("Quantidade de Arestas:", contAresta)

        if opcaoVerificacao == "iii": #conexo?
                visitado = [False] * len(self.vertices)
                self.dfs(0, visitado)
                if all(visitado):
                    print("O grafo é conexo.")
                else:
                    print("O grafo não é conexo.")

        if opcaoVerificacao == "iv":  #bipartido?
            cor = [-1] * len(self.vertices)
            fila = []

            for inicio in range(len(self.vertices)):
                if cor[inicio] == -1:
                    cor[inicio] = 1
                    fila.append(inicio)

                    while fila:
                        u = fila.pop(0)

                        if self.matriz[u][u]:
                            print("O grafo não é bipartido.")
                            return

                        for v in range(len(self.vertices)):
                            if self.matriz[u][v] is not None:
                                if cor[v] == -1:
                                    cor[v] = 1 - cor[u]
                                    fila.append(v)
                                elif cor[v] == cor[u]:
                                    print("O grafo não é bipartido.")
                                    return

            print("O grafo é bipartido.")

        if opcaoVerificacao == "v": #euleriano, semi-euleriano ou nenhum dos dois?
            contador = 0

            for i in self.vertices.keys():
                grau = 0
                for j in self.vertices.keys():
                    if self.matriz[self.vertices[i]][self.vertices[j]] is not None and i != j :
                        grau += 1
                if grau % 2 != 0:
                    contador += 1
            if contador == 0:
                print("É um grafo euleriano.")
            elif contador == 2:
                print("É um grafo Semi-Euleriano.")
            else:
                print("O grafo não é euleriano e nem semi-euleriano.")

        if opcaoVerificacao == "vi": #hamiltoniano?
            print("Ainda não implementado. (hamiltoniano)")

        if opcaoVerificacao == "vii": #tem ciclos?
            """Verifica o ciclo a partir do primeiro vértice"""
            print (self.lista)
            for i in range (len(self.vertices)): #Verifica loop
                if self.matriz[i][i] != None:
                    return("O grafo possui ciclos.")
            ciclo = False
            visitado = ["N"]*len(self.vertices)
            pilha = []
            for vertice in self.lista:
                if visitado[self.vertices[vertice]] == "N":
                    pilha.append(vertice)
                    visitado[self.vertices[vertice]] = "A"
                    ciclo = self.verifica_ciclo(vertice, ciclo, visitado, pilha, self.lista, self.direcionado)
            if ciclo:
                return("O grafo possui ciclos.")
            else:
                return("O grafo não possui ciclos.")

        if opcaoVerificacao == "viii": #planar?
            print("Ainda não implementado. (planar)")

    def Dijkstra(self, verticeInicial):
        distancias = {}
        for key in self.vertices.keys():
            distancias[key] = (False, float('inf'))
        distancias[verticeInicial] = (True, 0, None)
        fila = []
        fila.append(verticeInicial)

        while fila:
            vAtual = fila.pop(0)
            for nomeV, distV in self.lista[vAtual]:
                d = distancias[vAtual][1] + distV

                if not distancias[nomeV][0]:
                    fila.append(nomeV)
                    distancias[nomeV] = (True, d, vAtual)
                elif distancias[nomeV][1] > d:
                    distancias[nomeV] = (True, d, vAtual)

        return distancias
    
    def MenorCaminho(self, vIni, vFinal):
        distancias = self.Dijkstra(vIni)


        (_, d, traceback) = distancias[vFinal]
        caminho = f"{vFinal} (Distancia: {d})"

        while traceback != None:
            caminho = f"{traceback} -> " + caminho
            (*_, traceback) = distancias[traceback]

        return caminho

    def CaminhoHamiltoniano(self, inicio, direcionado=True):
        """
        Verifica se existe um caminho Hamiltoniano a partir de um vértice inicial.

        Parâmetros:
        - inicio: indice do vértice inicial para começar a busca do caminho hamiltoniano.
        - direcionado: booleano que indica se o grafo é direcionado ou não.

        Retorna:
        - Uma lista com o caminho hamiltoniano se existir. Se não existir retorna None.
        """
        caminho = [inicio]
        visitados = [False] * len(self.vertices)
        visitados[inicio] = True

        pilha = [(inicio, caminho[:], visitados[:])]  #Pilha que usa copias para evitar alteração inesperada.

        while pilha:
            v, caminho_atual, visitados_atuais = pilha.pop()

            #Se todos os vértices foram visitados, retorna o caminho hamiltoniano encontrado
            if len(caminho_atual) == len(self.vertices):
                return caminho_atual

            #Itera sobre os vértices adjacentes ao vértice atual
            for i in range(len(self.vertices)):
                if (self.matriz[v][i] is not None or (not direcionado and self.matriz[i][v] is not None)) and not visitados_atuais[i]:
                    novo_caminho = caminho_atual + [i]
                    novos_visitados = visitados_atuais[:]
                    novos_visitados[i] = True
                    pilha.append((i, novo_caminho, novos_visitados))

        return None  #Retorna None se nenhum caminho hamiltoniano foi encontrado
        

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

class PropriedadesIncompativeis(Exception):
    def __init__(self, message):
        super().__init__(message)
        
if __name__ == "__main__":
    v = ["A", "B", "C", "D", "E"]
    a = [("A", "B", 1), ("B", "D", 1), ("D", "C", 1), ("C", "E", 1), ("E", "A", 1)]

    #v = ["A","B","C", "D", "E", "F", "G", "H"]
    #a = [("A","B",1), ("B","C",3), ("D","A",4), ("C","D",1), ("F","E",5), ("G","F",4), ("E","G",4), ("F","H",3)]

    g = Grafo(v, a, True, True)
    #print(g.CompConexos())

    inicio = v.index("A")
    caminho_hamiltoniano = g.caminhoHamiltoniano(inicio, False)  #O caminho hamiltoniano muda ao passar o parametro 'direcionado' como true ou false.

    if caminho_hamiltoniano:
        caminho_hamiltoniano = [v[i] for i in caminho_hamiltoniano]
        print(f"Caminho Hamiltoniano encontrado: {caminho_hamiltoniano}")
    else:
        print("Nenhum caminho Hamiltoniano encontrado.")

    #arvore_dfs = g.ArvoreDFS('A')
    #print("ARVORE DFS: ")
    #print(arvore_dfs)
    #print(g.OrdemTopologica())
    #print(g.ArvoreGeradoraMinima())
    #print(g.ArestasPonte())

    '''contTeste=0
    while contTeste<8:
        print("Insira a opção referente a verificação que deseja fazer: ")
        print("i. qtd de vertices ")
        print("ii. qtd de arestas ")
        print("iii. conexo? ")
        print("iv. bipartido? ")
        print("v. euleriano? ")
        print("vi. hamiltoniano? ")
        print("vii. ciclico? ")
        print("viii. planar? ")
        opcaoVerificacao = input()
        g.VerificacoesGrafo(opcaoVerificacao)
        contTeste+=1'''
    
    
    #print(g.VerificacoesGrafo("vii"))

    print("=== + FIM + ===")
