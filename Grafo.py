import time

class Grafo:
    def __init__(self, vertices=[], arestas=[], direcionado=True):

        """Construtor da classe Grafo"""

        self.vertices = vertices
        self.direcionado = False if direcionado == "nao_direcionado" else True
        self.lista = {}

        # Funcionamento da população dos dados
        #    id = id da aresta atual
        #    de = vértice de onde parte a aresta
        #  para = vértice destino da aresta
        #  peso = valor do peso da aresta

        ### GRAFO EM MATRIZ ==========================
        nmr_vertices = len(self.vertices)
        self.matriz = [[None for _ in range(nmr_vertices)] for _ in range(nmr_vertices)]
        self.arestas = [[None for _ in range(nmr_vertices)] for _ in range(nmr_vertices)]

        if self.direcionado :
            for id, de, para, peso in arestas:
                self.matriz [de][para] = peso
                self.arestas[de][para] = id

        else:
            for id, de, para, peso in arestas:
                self.matriz [de][para] = peso
                self.matriz [para][de] = peso
                self.arestas[de][para] = id
                self.arestas[para][de] = id
        ### FIM DA INICIAÇÃO EM MATRIZ ===============

        ### GRAFO EM LISTA ===========================
        for v in self.vertices:
            self.lista[v] = []

        if self.direcionado:
            for id, de, para, peso in arestas:
                self.lista[de].append((para, peso))
        else:
            for id, de, para, peso in arestas:
                self.lista[de].append((para, peso))
                if not (de == para):
                    self.lista[para].append((de, peso))

        ### FIM DA INICIAÇÃO EM LISTA ================
    
    def __str__(self):
        """Método chamado implicitamente pelo interpretador ou explicitamente pelo usuário. 
Não recebe nada e retorna uma string que representa tanto a matriz
quanto a lista de adjacência."""
        string = "==== MATRIZ ====\n"
        for v in self.vertices:
            i = self.vertices[v]
            for j in self.matriz[i]:
                string += "{:>4}".format(str(j)) + ' '
            string += '\n'
        
        string = "=== ARESTAS ===\n"
        for v in self.vertices:
            i = self.vertices[v]
            for j in self.matriz[i]:
                string += "{:>4}".format(str(j)) + ' '
            string += '\n'

        string += "\n==== LISTA ====\n"
        for key in self.lista:
            string += f"{key}: {str(self.lista[key])}\n"
            
        return string
    
    def AdicionarArestas(self, id, v1, v2, valor=0):
        """Adiciona a aresta a partir de dois vértices recebidos e um valor. Não retorna nada."""
        self.matriz[v1][v2] = valor
        self.lista[v1].append((v2, valor))
        self.arestas[v1][v2] = id

        if not self.direcionado:
            self.matriz[v2][v1] = valor
            self.lista[v2].append((v1, valor))
            self.arestas[v2][v1] = id

    def RemoverArestas(self, v1, v2):
        """Recebe os vértices v1 e v2 que correspondem a uma aresta e a remove. Não retorna nada."""
        if v1 not in self.lista or v2 not in self.lista:
            raise IndexError("Os vértices fornecidos não existem")
        
        self.matriz [v1][v2] = None
        self.arestas[v1][v2] = None
        if not self.direcionado:
            self.matriz [v2][v1] = None
            self.arestas[v2][v1] = None
        
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

    def ArvoreBFS(self):
        """Realiza a busca em largura a partir do vértice 0. Retorna os identificadores das arestas."""
        listaArestas = []
        visitado = ["N"]*len(self.vertices) #Lista de todos os vértices, que informa o estado atual de cada vértice.
        #"N": ainda não foi encontrado.
        #"A": foi encontrado, mas não foi explorado.
        #"V": foi explorado.
        fila = [0]
        visitado[0] = "A"

        while fila:
            i = fila.pop(0)
            for j in self.lista[i]:
                if visitado[self.vertices[j[0]]] == "N":
                    visitado[self.vertices[j[0]]] = "A"
                    fila.append(j[0])
                    listaArestas.append(self.arestas[i][j[0]])
            visitado[i] = "V"
            
        listaArestas.sort()
        return listaArestas

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
    
    def CicloArvoreGeradora(self, arvore):
        pass

    def CompFortementeCnx(self):
        """Encontra componentes fortemente conexas em um grafo orientado usando o algoritmo de Kosaraju"""

        # Descobre os tempos de fechamento dos vértices
        tempos_fechamento = self._temporizar()

        # Usando esses tempos, ele faz o mesmo, porém com arestas invertidas
        self._inverterArcos()
        # !!! Apesar de rearoveitar a variável abaixo, o seu conteúdo serão as
        # componentes fortemente conexas !!!
        tempos_fechamento = self._temporizar(tempos_fechamento)

        # Ao fim, voltamos os arcos para sua orientação original
        self._inverterArcos()

        # Extrair os vértices das tuplas
        vertices_conexos = []

        # Para cada componente encontrado
        # Em cada componente tiremos o vértice segundo elemento da tupla, logo
        # v[1]
        # Todos os elementos do mesmo componente serão juntados numa lista e
        # apresentados em grupos dentro da lista vertices_conexos
        for componente in tempos_fechamento:
            vertices_conexos.append(list(map(lambda v: v[1], componente)))
            
        return vertices_conexos


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
        for vertice in arvore:
            if visitado[vertice] == "N":
                pilha.append(vertice)
                visitado[vertice] = "A"
                ciclo = self.verifica_ciclo(vertice, ciclo, visitado, pilha, arvore, 0)
            
        return ciclo
    
    def ArvoreGeradoraMinima (self):
        ehPond = False
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] != 1 and self.matriz[i][j] != None:
                    ehPond = True
        
        if ehPond == False:
            return -1

        listaArestas = [] #configuração: (valor, v1, v2)
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if i < j and self.matriz[i][j] != None: #Retira os loops e arestas repetidas
                    listaArestas.append ((self.matriz[i][j],i,j))
        listaArestas.sort()

        arvore = {}
        listaArestas2 = []
        for vertice in self.lista:
            arvore[vertice] = []
        
        quantidade = 0
        cont = 0
        qtArestas = len(listaArestas)
        while quantidade < len(self.vertices)-1 and cont < qtArestas:
            cont = cont+1
            aresta = listaArestas.pop(0)
            
            arvore[aresta[1]].append((aresta[2], aresta[0])) 
            arvore[aresta[2]].append((aresta[1], aresta[0]))
            
            if self.CicloArvoreGeradora(arvore):
                arvore[aresta[1]].remove((aresta[2], aresta[0]))
                arvore[aresta[2]].remove((aresta[1], aresta[0]))
            else:
                quantidade = quantidade+1
                listaArestas2.append(self.arestas[aresta[1]][aresta[2]])

        listaArestas2.sort()

        return listaArestas2

    def verifica_ciclo(self, pai, ciclo, visitado, pilha, lista, direcionado):
        """Usa DFS para verificação de ciclo. Se chegar em um vértice que já foi encontrado, mas não explorado, há um ciclo.""" 
        ultimo = len(pilha)-1
        i = pilha[ultimo]
        for j in lista[i]:
            if visitado[j[0]] == "N":
                visitado[j[0]] = "A"
                pilha.append(j[0])
                ciclo = self.verifica_ciclo(i, ciclo, visitado, pilha, lista, direcionado)
            elif visitado[j[0]] == "A" and j[0] != pai:
                return True
            elif direcionado and visitado[j[0]] == "A": #Se for direcionado e tiver um caminho para o pai, há um ciclo.
                return True
        visitado[i] = "V"
        ultimo = len(pilha)-1
        pilha.pop(ultimo)
        return ciclo
    
    def Tarjan(self, lista, vertice, visitado, low, tempoD, arestasPonte, tempo, pai, aAnterior):
        """Aplica o método de Tarjan para encontrar arestas ponte"""
        visitado[vertice] = "A"
        tempoD[vertice] = tempo
        low[vertice] = tempo
        for tupla in lista[vertice]:
            if visitado[tupla[0]] == "N":
                tempo += 1
                self.Tarjan(lista, tupla[0], visitado, low, tempoD, arestasPonte, tempo, vertice, tupla)
                low[vertice] = min(low[vertice], low[tupla[0]])
                if low[tupla[0]] > tempoD[vertice]:
                    arestasPonte.append(self.arestas[vertice][tupla[0]])
            elif vertice != tupla[0] and visitado[tupla[0]] == "A" and (tupla[0] != pai or aAnterior[1] != tupla[1]):
                low[vertice] = min(low[vertice], tempoD[tupla[0]])


        visitado[self.vertices[vertice]] = "V"
    
    def ArestasPonte(self):
        """Transforma o grafo direcionado em não direcionado e chama o método de Tarjan para cada vértice"""
        grafo2 = {}
        for vertice in self.vertices:
            grafo2[vertice] = []
        for vertice in self.vertices:
            for tupla in self.lista[vertice]:
                grafo2[vertice].append((tupla[0], tupla[1]))
                if self.direcionado:
                    grafo2[tupla[0]].append((vertice, tupla[1]))

        for i in grafo2:
            grafo2[i].sort()

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
    
    def FechoTransitivo(self):
        if not self.direcionado:
            return -1
        
        listaVertices = [0]
        visitado = ["N"]*len(self.vertices) #Lista de todos os vértices, que informa o estado atual de cada vértice.
        #"N": ainda não foi encontrado.
        #"A": foi encontrado, mas não foi explorado.
        #"V": foi explorado.
        fila = [0]
        visitado[0] = "A"

        while fila:
            i = fila.pop(0)
            for j in self.lista[i]:
                if visitado[self.vertices[j[0]]] == "N":
                    visitado[self.vertices[j[0]]] = "A"
                    fila.append(j[0])
                    listaVertices.append(j[0])
            visitado[i] = "V"

        listaVertices.sort()
            
        return listaVertices
    def _dfs(self, v_ini, tempo=1, tempos=[], visitados=set()):
        a_explorar = [v_ini]
        retornos = []

        while a_explorar:
            v_atual = a_explorar[-1]  # Olhe para o vértice no topo da pilha
            if v_atual not in visitados:
                visitados.add(v_atual)
                tempo += 1
                houve_explorado = False

                for filho in self.lista[v_atual]:
                    filho = filho[0]
                    if filho not in visitados:
                        a_explorar.append(filho)
                        houve_explorado = True

                if not houve_explorado:
                    tempos.append((tempo, v_atual))
                    tempo += 1
                    retornos.append(a_explorar.pop()) # Remova e processe o vértice atual
            else:
                # Se todos os filhos forem visitados, defina o tempo de término
                tempos.append((tempo, v_atual)) 
                tempo += 1
                retornos.append(a_explorar.pop())

        return tempos, tempo, visitados
    
    def _temporizar(self, tempo_decresc=[]):
        # Atribui um tempo de descoberta a cada vértice do grafo usando DFS.
        # Caso uma lista com tempos tenha sido fornecida, a atribuição dos tempos
        # será feita na ordem decrescente dos tempos da lista.
        # Esta especificidade mencionada é utilizada no algoritmo de Kosaraju

        visitados = set()
        tempo = 1
        tempos = []

        if not tempo_decresc:
            for v in self.vertices:
                if v not in visitados:
                    tempos, tempo, visitados = self._dfs(v, tempo, tempos, visitados)

        else:
            for v in reversed(tempo_decresc):
                v = v[1] # Utiliza somente o vértice da tupla
                if v not in visitados:
                    componente, tempo, visitados = self._dfs(v, tempo, [], visitados)
                    # Aqui, usamos .append pois no fim teremos uma lista de
                    # componentes fortemente conexos.
                    tempos.append(componente)

        return tempos

    def _inverterArcos(self):
        # Semelhante ao transpor uma matriz, este "transpõe" a lista 
        lista_invertida = {}
        for v in self.lista.keys():
            lista_invertida[v] = []

        for v in self.lista.keys():
            for filhos in self.lista[v]:
                lista_invertida[filhos[0]].append((v, filhos[1]))
        
        self.lista = lista_invertida

    @staticmethod
    def conexosParaString(listasDeConexos):
        """Transforma uma lista de componentes conexos em uma grande string paresentável ao usuário"""
        saida = ""
        for cmpsConexos in listasDeConexos:
            for vertice in cmpsConexos:
                saida += str(vertice) + " "
            saida += " "

        return saida

class PropriedadesIncompativeis(Exception):
    def __init__(self, message):
        super().__init__(message)
        
if __name__ == "__main__":
    entradas = list(map(int, input().split()))
    direc = input()
    v = [i for i in range(entradas[0])]

    g = Grafo(v, direcionado=direc)
    for i in range(entradas[1]):
        entradas = list(map(int, input().split()))
        g.AdicionarArestas(entradas[0], entradas[1], entradas[2], entradas[3])
    
    print(g.FechoTransitivo())
    #print(g)

    #g.RemoverArestas(entradas[1], entradas[2])

    #print(g)
    listaDeComp = g.CompFortementeCnx()
    print(listaDeComp)

    print("=== + FIM + ===")

"""
4 4
nao_direcionado
0 0 1 1
1 1 2 1
2 1 3 1
3 2 3 1

8 12
direcionado
0 0 1 1
1 1 4 1
2 2 3 1
3 2 6 1
4 3 2 1
5 3 7 1
6 4 0 1
7 4 5 1
8 5 6 1
9 6 5 1
10 6 7 1
11 7 7 1

8 14
direcionado
0 0 1 1
1 1 2 1
2 2 0 1
3 3 1 1
4 3 2 1
5 3 4 1
6 4 3 1
7 4 5 1
8 5 2 1
9 5 6 1
10 6 5 1
11 7 4 1
12 7 6 1
13 7 7 1

8 9
direcionado
0 0 1 1
1 1 2 1
2 2 3 1
3 3 0 1
4 2 4 1
5 4 5 1
6 5 6 1
7 6 4 1
8 6 7 1
"""