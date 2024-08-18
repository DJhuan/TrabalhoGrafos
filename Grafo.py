import copy

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

    def ArvoreBFS(self, v=0):
        """Realiza a busca em largura a partir do vértice v. Retorna os identificadores das arestas."""
        listaArestas = []
        visitado = ["N"]*len(self.vertices) #Lista de todos os vértices, que informa o estado atual de cada vértice.
        #"N": ainda não foi encontrado.
        #"A": foi encontrado, mas não foi explorado.
        #"V": foi explorado.
        fila = [v]
        visitado[v] = "A"

        while fila:
            i = fila.pop(0)
            for j in self.lista[i]:
                if visitado[self.vertices[j[0]]] == "N":
                    visitado[self.vertices[j[0]]] = "A"
                    fila.append(j[0])
                    listaArestas.append(self.arestas[i][j[0]])
            visitado[i] = "V"

        return listaArestas

    def ArvoreDFS(self):
        """Realiza a busca em profundidade a partir do vértice 0. Retorna os identificadores das arestas."""
        listaArestas = []
        visitado = ["N"] * len(self.vertices)  #Lista de todos os vértices, que informa o estado atual de cada vértice.
        #"N": ainda não foi encontrado.
        #"A": foi encontrado, mas não foi explorado.
        #"V": foi explorado.

        def dfs_aux(v):
            visitado[v] = "A"
            for u, _ in sorted(self.lista[v]):
                if visitado[self.vertices[u]] == "N":
                    listaArestas.append(self.arestas[v][u])
                    dfs_aux(u)
            visitado[v] = "V"

        dfs_aux(0)  #Inicia a DFS a partir do vértice 0

        #Verifica se tem vértices desconectados e ignora eles
        if "N" in visitado:
            print("O grafo é desconexo. Considerando apenas a árvore com a raiz 0.")

        return listaArestas

    def OrdemTopologica(self, pilha, listaExecucao, visitado):
        """Argoritmo DFS. Retorna uma possibilidade de ordem de execução"""
        visitado[0] = "A"
        pilha.append(0)
        while pilha:
            t = len(pilha)-1
            i = pilha.pop(t)
            for j in self.lista[i]:
                if visitado[self.vertices[j[0]]] == "N":
                    visitado[self.vertices[j[0]]] = "A"
                    pilha.append(j[0])
                    listaExecucao.append(j[0])
                    listaExecucao = self.FechoTransitivo(pilha, listaExecucao, visitado)
            visitado[i] = "V"

        listaExecucao.reverse()
        return listaExecucao

    def CompConexos(self):
        """Retorna a quantidade de componentes conexos do grafo"""

        if self.direcionado:
            msg = "A função CompConexos não pode ser utilizada em grafos direcionados!"
            raise(PropriedadesIncompativeis(msg))

        componentes = 0
        visitados = set()

        for vertice in self.vertices:
            if vertice not in visitados:
                _, _, componente = self._dfs(vertice)
                for v in componente: 
                    visitados.add(v)

                componentes += 1
                
        return componentes

    def CompFortementeCnx(self):
        """Conta quantas componentes fortemente conexas há no grafo."""

        # Descobre os tempos de fechamento dos vértices
        tempos_fechamento = self._temporizar()

        # Garante que os tempos de fechamento estarão ordenados crescentemente
        # a função lambda abaixo apenas indica a qual item da dupla será
        # considerado durante a ordenação, no caso o tempo, que é o primeiro;
        tempos_fechamento.sort(key=lambda tempo: tempo[0])

        # Para evitar incoerências futuras, criamos um novo grafo com arestas invertidas
        gTransposto = copy.deepcopy(self)
        gTransposto._inverterArcos()
        componentes_conexas = gTransposto._temporizarReversa(tempos_fechamento)
        del gTransposto
        return len(componentes_conexas)

    def CicloArvoreGeradora(self, lista):
        """Transforma o grafo direcionado em não direcionado e verifica o ciclo."""
        arvore = {}
        for vertice in lista:
            arvore[vertice] = []
        for vertice in lista:
            for tupla in lista[vertice]:
                arvore[vertice].append((tupla[0], tupla[1]))
                if self.direcionado:
                    arvore[tupla[0]].append((vertice, tupla[1]))
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
        listaArestas = [] #configuração: (valor, v1, v2)
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if i < j and self.matriz[i][j] != None: #Retira os loops e arestas repetidas
                    listaArestas.append ((self.matriz[i][j],i,j))
        listaArestas.sort()

        arvore = {}
        valor = 0
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
                valor += aresta[0]

        return valor

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

    def TarjanA(self, vertice, visitado, low, tempoD, pai, arestasPonte, tempo):
        """Aplica o método de Tarjan para encontrar arestas ponte"""
        visitado[vertice] = "A"
        tempoD[vertice] = tempo
        low[vertice] = tempo
        for tupla in self.lista[vertice]:
            u = tupla[0]
            if visitado[u] == "N":
                #print (vertice, pai)
                pai[u] = vertice
                tempo += 1
                self.TarjanA(u, visitado, low, tempoD, pai, arestasPonte, tempo)
                low[vertice] = min(low[vertice], low[u])
                if low[u] > tempoD[vertice]:
                    arestasPonte.append(self.arestas[vertice][u])
            elif visitado[u] == "A" and u != pai[vertice]:
                low[vertice] = min(low[vertice], tempoD[u])

        visitado[vertice] = "V"

    def TarjanV(self, vertice, visitado, low, tempoD, pai, verticesArtic, tempo):
        """Aplica o método de Tarjan para encontrar arestas ponte"""
        visitado[vertice] = "A"
        tempoD[vertice] = tempo
        low[vertice] = tempo
        for tupla in self.lista[vertice]:
            u = tupla[0]
            if visitado[u] == "N":
                pai[u] = vertice
                tempo += 1
                self.TarjanV(u, visitado, low, tempoD, pai, verticesArtic, tempo)
                low[vertice] = min(low[vertice], low[u])
                if low[u] >= tempoD[vertice]:
                    verticesArtic.append(vertice)
            elif visitado[u] == "A" and u != pai[vertice]:
                low[vertice] = min(low[vertice], tempoD[u])

        visitado[vertice] = "V"

    def Cortes(self, id):
        visitado = ["N"]*len(self.vertices)
        low = [None]*len(self.vertices)
        tempoD = [None]*len(self.vertices)
        pai = [None]*len(self.vertices)
        tempo = 1

        if id == 1:
            arestasPonte = []
            for vertice in self.vertices:
                if visitado[self.vertices[vertice]] == "N":
                    self.TarjanA(vertice, visitado, low, tempoD, pai, arestasPonte, tempo)

            arestasPonte.sort()
            return arestasPonte

        if id == 2:
            verticesArtic = []
            for vertice in self.vertices:
                if visitado[self.vertices[vertice]] == "N":
                    self.TarjanV(vertice, visitado, low, tempoD, pai, verticesArtic, tempo)

            verticesArtic.sort()
            return verticesArtic


    def dfs(self, vertice, visitado):
        """Função de busca em profundidade (DFS) para percorrer o grafo."""

        visitado[vertice] = True

        #Percorre todos os vértices adjacentes ao vértice atual
        for i in range(len(self.vertices)):
            if self.matriz[vertice][i] is not None and not visitado[i]:
                self.dfs(i, visitado)  #Recursivamente visita os vértices adjacentes


    def VerificacoesGrafo(self, opcaoVerificacao):
        # i: Verifica se é conexo
        # ii: Veriftica se é bipartido
        # iii: Verifica se é eulerianfo
        # iv: Verifica se tem ciclos
        # Retorna 1 se a resposta for sim e 0 se a resposta for não.

        if opcaoVerificacao == "i":  #Conexo?
            if self.direcionado:
                return 1 if len(self.CompFortementeCnx()) == 1 else 0
            else:
                visitado = [False] * len(self.vertices)
                self.dfs(0, visitado)
                return 1 if all(visitado) else 0

        if opcaoVerificacao == "ii":  #Bipartido?
            cor = [-1] * len(self.vertices)
            fila = []

            for inicio in range(len(self.vertices)):
                if cor[inicio] == -1:
                    cor[inicio] = 1
                    fila.append(inicio)

                    while fila:
                        u = fila.pop(0)
                        for v in range(len(self.vertices)):
                            if self.matriz[u][v] is not None:
                                if cor[v] == -1:
                                    cor[v] = 1 - cor[u]
                                    fila.append(v)
                                elif cor[v] == cor[u]:
                                    return 0
            return 1

        if opcaoVerificacao == "iii":  #Euleriano?
            if self.direcionado:
                #Verifica se é fortemente conexo
                if len(self.CompFortementeCnx()) != 1:
                    return 0
                #Verifica se o numero de arestas de entrada é igual ao de saída para cada vertice
                for vertice in self.vertices:
                    grau_entrada = sum(1 for i in range(len(self.vertices)) if self.matriz[i][vertice] is not None)
                    grau_saida = sum(1 for i in range(len(self.vertices)) if self.matriz[vertice][i] is not None)
                    if grau_entrada != grau_saida:
                        return 0
                return 1
            else:
                #Verifica se é conexo
                visitado = [False] * len(self.vertices)
                self.dfs(0, visitado)
                if not all(visitado):
                    return 0
                #Verifica se todos os vértices tem grau par
                for vertice in self.vertices:
                    grau = sum(1 for i in range(len(self.vertices)) if self.matriz[vertice][i] is not None or self.matriz[i][vertice] is not None)
                    if grau % 2 != 0:
                        return 0
                return 1

        if opcaoVerificacao == "iv":  #Tem ciclos?
            if self.direcionado:
                visitado = ["N"] * len(self.vertices)
                pilha = []
                for vertice in self.lista:
                    if visitado[self.vertices[vertice]] == "N":
                        pilha.append(vertice)
                        visitado[self.vertices[vertice]] = "A"
                        if self.verifica_ciclo(vertice, False, visitado, pilha, self.lista, self.direcionado):
                            return 1
                return 0
            else:
                for i in range(len(self.vertices)):
                    if self.matriz[i][i] is not None:
                        return 1
                visitado = ["N"] * len(self.vertices)
                pilha = []
                for vertice in self.lista:
                    if visitado[self.vertices[vertice]] == "N":
                        pilha.append(vertice)
                        visitado[self.vertices[vertice]] = "A"
                        if self.verifica_ciclo(vertice, False, visitado, pilha, self.lista, self.direcionado):
                            return 1
                return 0


    def bfs(self, origem, destino, pai):
        """Realiza uma busca em largura (BFS) para encontrar um caminho aumentante"""
        visitado = [False] * len(self.vertices)
        fila = [origem]
        visitado[origem] = True

        while fila:
            u = fila.pop(0)

            for indice, valor in enumerate(self.matriz[u]):
                if visitado[indice] == False and valor is not None and valor > 0:
                    fila.append(indice)
                    visitado[indice] = True
                    pai[indice] = u

        return visitado[destino]

    def FluxoMaximo(self):
        """Calcula o valor do fluxo máximo de 0 a n-1."""
        if not self.direcionado:
            return "A função de fluxo máximo só pode ser usada em grafos direcionados."

        origem = 0
        destino = len(self.vertices) - 1
        pai = [-1] * len(self.vertices)
        fluxo_maximo = 0

        while self.bfs(origem, destino, pai):
            fluxo_caminho = float('Inf')
            s = destino
            while s != origem:
                fluxo_caminho = min(fluxo_caminho, self.matriz[pai[s]][s] if self.matriz[pai[s]][s] is not None else 0)
                s = pai[s]
            fluxo_maximo += fluxo_caminho
            v = destino
            while v != origem:
                u = pai[v]
                if self.matriz[u][v] is None:
                    self.matriz[u][v] = 0
                if self.matriz[v][u] is None:
                    self.matriz[v][u] = 0
                self.matriz[u][v] -= fluxo_caminho
                self.matriz[v][u] += fluxo_caminho
                v = pai[v]

        return fluxo_maximo

    def Dijkstra(self, verticeInicial):
        distancias = {}
        for key in self.vertices:
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

        try:
            (_, d, traceback) = distancias[vFinal]
            caminho = f"{vFinal} (Distancia: {d})"

            while traceback != None:
                caminho = f"{traceback} -> " + caminho
                (*_, traceback) = distancias[traceback]
        except ValueError:
            return -1

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

    def FechoTransitivo(self, pilha, visitado, listaVertices):
        #"N": ainda não foi encontrado.
        #"A": foi encontrado, mas não foi explorado.
        #"V": foi explorado.
        visitado[0] = "A"
        pilha.append(0)
        while pilha:
            t = len(pilha)-1
            i = pilha.pop(t)
            for j in self.lista[i]:
                if visitado[self.vertices[j[0]]] == "N":
                    visitado[self.vertices[j[0]]] = "A"
                    pilha.append(j[0])
                    listaVertices.append(j[0])
                    listaVertices = self.FechoTransitivo(pilha, visitado, listaVertices)
            visitado[i] = "V"

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
    
    def _temporizar(self):
        # Atribui um tempo de descoberta a cada vértice do grafo usando DFS.

        visitados = set()
        tempo = 1
        tempos = []
        for v in self.vertices:
            if v not in visitados:
                tempos, tempo, visitados = self._dfs(v, tempo, tempos, visitados)

        return tempos
    
    def _temporizarReversa(self, tempo_decresc):
        # Encontra as componentes fortemente conexas

        visitados = set()
        tempos = []
        for tupla in reversed(tempo_decresc):
            v = tupla[1] # Utiliza somente o vértice da tupla
            if v not in visitados:
                componente, _, visitados = self._dfs(v, 0, [], visitados)
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
    funcoes = list(map(int, input().split()))
    entradas = list(map(int, input().split()))
    direc = input()
    v = [i for i in range(entradas[0])]

    g = Grafo(v, direcionado=direc)
    for i in range(entradas[1]):
        entradas = list(map(int, input().split()))
        g.AdicionarArestas(entradas[0], entradas[1], entradas[2], entradas[3])

    for i in funcoes:
        if i == 0:
            print('IMPLEMENTAR')
        elif i == 1:
            print('IMPLEMENTAR')
        elif i == 2:
            arvore_dfs = g.ArvoreDFS()
            for j in range(len(arvore_dfs)):
                if j == len(arvore_dfs) - 1:
                    print(arvore_dfs[j])
                else:
                    print(arvore_dfs[j], end=' ')
        elif i == 3:
            print("IMPLEMENTAR")
        elif i == 4:
            print(g.CompConexos())
        elif i == 5:
            print(g.CompFortementeCnx())
        elif i == 6:
            if g.direcionado:
                print ("-1")
            else:
                vertices = g.Cortes(2)
                for j in range (len(vertices)):
                    if j == len(vertices)-1:
                        print (vertices[j])
                    else:
                        print (vertices[j], end=' ')
        elif i == 7:
            if g.direcionado:
                print ("-1")
            else:
                arestas = g.Cortes(1)
                for j in range (len(arestas)):
                    if j == len(arestas)-1:
                        print (arestas[j])
                    else:
                        print (arestas[j], end=' ')
        elif i == 8:
            print('IMPLEMENTAR')
        elif i == 9:
            arvore = g.ArvoreBFS()
            for j in range (len(arvore)):
                if j == len(arvore)-1:
                    print (arvore[j])
                else:
                    print (arvore[j], end=' ')
        elif i == 10:
            ehPond = False
            for i in range(len(g.matriz)):
                for j in range(len(g.matriz[i])):
                    if g.matriz[i][j] != 1 and g.matriz[i][j] != None:
                        ehPond = True
            if ehPond == False or g.direcionado or g.VerificacoesGrafo("iii") == "O grafo é conexo.":
                print ("-1")
            else:
                print(g.ArvoreGeradoraMinima())
        elif i == 11:
            if g.VerificacoesGrafo("iii"):
                print ("é euleriano")
            else:
                print("não é euleriano")
            """
            else:
                ordem = g.OrdemTopologica()
                for j in range (len(ordem)):
                    if j == len(ordem)-1:
                        print (ordem[j])
                    else:
                        print (ordem[j], end=' ')
            """
        elif i == 12:
            print ('IMPLEMENTAR')
        elif i == 13:
            print ('IMPLEMENTAR')
        elif i == 14:
            if not g.direcionado:
                print (-1)
            else:
                fecho = g.FechoTransitivo([], ["N"]*len(g.vertices), [])
                for j in range (len(fecho)):
                    if j == len(fecho)-1:
                        print (fecho[j])
                    else:
                        print (fecho[j], end=' ')


    print("=== + FIM + ===")

"""
5
5 7
direcionado
0 0 1 2    
1 0 2 4    
2 1 2 5    
3 1 4 3
4 2 3 8
5 3 1 2
6 3 4 4

"""
