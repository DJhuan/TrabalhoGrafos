class Grafo:
    def __init__(self, vertices, direcionado, valorado):
        self.vertices = vertices
        self.grafo = [['']*self.vertices for i in range(self.vertices)]
        self.direcionado = direcionado
        self.valorado = valorado

    def AdicionarArestas(self, v1, v2, valor):
        self.grafo[v1-1][v2-1] = valor
        if self.direcionado == 0:
            self.grafo[v2-1][v1-1] = valor

    def RemoverArestas(self, v1, v2):
        self.grafo[v1-1][v2-1] = ''
        if self.direcionado == 0:
            self.grafo[v2-1][v1-1] = ''

    def Imprime(self):
        for i in range(self.vertices):
            print(self.grafo[i])

    def AdicionarVertices(self):
        for i in range(self.vertices):
            self.grafo[i].append('')
        self.grafo.append(['']*(self.vertices+1))
        self.vertices = self.vertices+1

    def RemoverVertices(self, vertice):
        for i in range(self.vertices):
            del self.grafo[i][vertice-1]
        del self.grafo[vertice-1]
        self.vertices = self.vertices-1

    def dfs(self, vertice, visitado):
        visitado[vertice] = True
        for i in range(self.vertices):
            if self.grafo[vertice][i] != '' and not visitado[i]:
                self.dfs(i, visitado)

    def transpor(self):
        grafo_transposto = [['']*self.vertices for i in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                grafo_transposto[j][i] = self.grafo[i][j]
        return grafo_transposto


    def verifica_ciclo_dfs(self, v, visitado, pai):
        visitado[v] = True
        for i in range(self.vertices):
            if self.grafo[v][i] != '':
                if visitado[i] == False:
                    if self.verifica_ciclo_dfs(i, visitado, v):
                        return True
                elif self.direcionado or pai != i:
                    return True

        return False

    def verifica_ciclo(self):
        visitado = [False] * self.vertices
        for i in range(self.vertices):
            if visitado[i] == False:
                if self.verifica_ciclo_dfs(i, visitado, -1) == True:
                    return True

        return False

    def Verificacoes (self, opcaoVerificacao):

        if opcaoVerificacao == "i":
            contVertices = 0
            for i in range(self.vertices):
                contVertices += 1
            print("Quantidade de Vértices: ", contVertices)

        if opcaoVerificacao == "ii":
            contAresta = 0
            for i in range (self.vertices):
                for j in range (self.vertices):
                    if self.grafo[i][j] != '':
                        contAresta += 1
            if self.direcionado == 0:
                contAresta = contAresta // 2
            print("Quantidade de Arestas:", contAresta)

        if opcaoVerificacao == "iii":
            numVertice = int(input("Insira o número do vértice da qual você deseja saber o grau: "))
            grauEntrada = 0
            grauSaida = 0

            for j in range (self.vertices):
                if self.grafo[numVertice-1][j] != '':
                    grauSaida += 1
                if self.grafo[j][numVertice-1] != '':
                    grauEntrada += 1

            if self.direcionado:
                print("O grau de saída do vértice ", numVertice, "é igual a ", grauSaida)
                print("O grau de entrada do vértice ", numVertice, "é igual a ", grauEntrada)
                print("O grau do vértice ", numVertice, "é igual a ", grauSaida + grauEntrada)
            else:
                print("O grau do vértice ", numVertice, "é igual a ", grauSaida)

        if opcaoVerificacao == "iv":
            visitado = [False] * self.vertices
            self.dfs(0, visitado)
            if all(visitado):
                print("O grafo é conexo.")
            else:
                print("O grafo não é conexo.")

        if opcaoVerificacao == "v":
            visitado = [False] * self.vertices
            self.dfs(0, visitado)
            if not all(visitado):
                print("O grafo não é fortemente conexo.")
            else:
                grafo_transposto = self.transpor()
                self.grafo = grafo_transposto
                visitado = [False] * self.vertices
                self.dfs(0, visitado)
                if not all(visitado):
                    print("O grafo não é fortemente conexo.")
                else:
                    print("O grafo é fortemente conexo.")

        if opcaoVerificacao == "vi":
            if self.verifica_ciclo():
                print("O grafo possui ciclos.")
            else:
                print("O grafo não possui ciclos.")

        if opcaoVerificacao == "vii":
            contador = 0

            for i in range(self.vertices):
                grau = 0
                for j in range(self.vertices):
                    if self.grafo[i][j] != '' and i != j :
                        grau += 1
                if grau % 2 != 0:
                    contador += 1
            if contador == 0:
                print("É um grafo euleriano.")
            elif contador == 2:
                print("É um grafo Semi-Euleriano.")
            else:
                print("O grafo não é euleriano e nem semi-euleriano.")


    def ArvoreBFS(self, inicial):
        arvore = [['']*self.vertices for i in range(self.vertices)]
        visitado = ["N"]*self.vertices
        fila = [inicial-1]
        acabou = False

        while not acabou:
            acabou = True
            for i in fila:
                nVertice = 0
                for j in self.grafo[i]:
                    if j != '' and visitado[nVertice] == "N":
                        visitado[nVertice] = "A"
                        fila.append(nVertice)
                        arvore[i][nVertice] = 1
                    nVertice = nVertice+1
                visitado[i] = "V"
            
            n = len(fila)
            for i in range(n):
                fila.pop(0)
            cont = 0
            while cont < len(visitado):
                if visitado[cont] == "N":
                    acabou = False
                    fila.append(cont)
                    visitado[cont] = "A"
                    cont = len(visitado)
                cont = cont+1

        print("Árvore de busca em largura:")
        for i in range (len(arvore)):
            print(arvore[i])



def EscreveArquivo(g, nomeArquivo):
    with open(nomeArquivo, "w") as arquivo:
        arquivo.write("V = {")
        if g.vertices != 0:
            arquivo.write("1")
        for vertice in range(g.vertices-1):
            arquivo.write(",")
            arquivo.write(str(vertice+2))
        arquivo.write("} A = {")
        if not g.direcionado:
            n = 0
            primeiro = True
            for linha in g.grafo:
                for i in range(n,g.vertices):
                    if linha[i] != '':
                        if not primeiro:
                            arquivo.write(",")
                        else:
                            primeiro = False
                        arquivo.write("(")
                        arquivo.write(str(n+1))
                        arquivo.write(",")
                        arquivo.write(str(i+1))
                        if g.valorado:
                            arquivo.write(",")
                            arquivo.write(str(linha[i]))
                        arquivo.write(")")
                n = n+1
        else:
            n = 0
            primeiro = True
            for linha in g.grafo:
                for elemento in range(g.vertices):
                    if linha[elemento] != '':
                        if not primeiro:
                            arquivo.write(",")
                        else:
                            primeiro = False
                        arquivo.write("(")
                        arquivo.write(str(n+1))
                        arquivo.write(",")
                        arquivo.write(str(elemento+1))
                        if g.valorado:
                            arquivo.write(",")
                            arquivo.write(str(linha[elemento]))
                        arquivo.write(")")
                n = n+1

        arquivo.write("}")


nomeArquivo = input("Escreva o nome do arquivo: ")
with open("./" + nomeArquivo, "r") as arquivo:
    direcionado = int(input("O grafo é direcionado? 1 é sim e 0 é não: "))
    valorado = int(input("O grafo é valorado? 1 é sim e 0 é não: "))
    linha = arquivo.read()
    qtVertices = 0
    contador = 0
    while linha[contador] != '{':
        contador = contador+1
    contador = contador+1
    while linha[contador] != '}':
        if linha[contador] != ',':
            qtVertices = qtVertices+1
        contador = contador+1
    g = Grafo(qtVertices, direcionado, valorado)
        
    if not valorado:
        valor = 1
        while linha[contador] != '{':
            contador = contador+1
        while linha[contador] != '}':
            v1 = int(linha[contador+2])
            v2 = int(linha[contador+4])
            g.AdicionarArestas(v1,v2,valor)
            contador = contador+6
    else:
        while linha[contador] != '{':
            contador = contador+1
        while linha[contador] != '}':
            v1 = int(linha[contador+2])
            v2 = int(linha[contador+4])
            print(linha[contador+6])
            valor = int(linha[contador+6])
            g.AdicionarArestas(v1,v2,valor)
            contador = contador+8

print("Grafo em matriz: ")
g.Imprime()

print("O que você deseja fazer?")
print("1: Imprimir o grafo em matriz")
print("2: Adicionar vérices")
print("3: Remover vértices")
print("4: Adicionar arestas")
print("5: Remover arestas")
print("6: Verificações no grafo")
print("7: Busca em largura (BFS)")
n = input()

if n == "1":
    g.imprime()

if n == "2":
    g.AdicionarVertices()
    g.Imprime()
    EscreveArquivo(g,nomeArquivo)

if n == "3":
    vertice = int(input("Qual vértice você deseja remover? "))
    if vertice > g.vertices or vertice <= 0:
        print("Esse vértice não existe.")
    else:
        g.RemoverVertices(vertice)
        g.Imprime()
        EscreveArquivo(g,nomeArquivo)

if n == "4":
    v1 = int(input("Insira o vértice de saída: "))
    if v1 > g.vertices or v1 <= 0:
        print("Esse vértice não existe.")
    else:
        v2 = int(input("Insira o vértice de chegada: "))
        if v2 > g.vertices or v2 <= 0:
            print("Esse vértice não existe.")
        else:
            if valorado:
                valor = int(input("Insira o valor: "))
            else:
                valor = 1
            g.AdicionarArestas(v1, v2, valor)
            EscreveArquivo(g,nomeArquivo)
            g.Imprime()

if n == "5":
    v1 = int(input("Insira o vértice de saída: "))
    if v1 > g.vertices or v1 <= 0:
        print("Esse vértice não existe.")
    else:
        v2 = int(input("Insira o vértice de chegada: "))
        if v2 > g.vertices or v2 <= 0:
            print("Esse vértice não existe.")
        else:
            g.RemoverArestas(v1,v2)
            EscreveArquivo(g,nomeArquivo)
            g.Imprime()

if n == "6":
    print("Qual tipo de verificação você deseja fazer?  ")
    print("i. Quantidade de vértices")
    print("ii. Quantidade de arestas")
    print("iii. Grau de um vértice")
    print("iv. O grafo é conexo?")
    if g.direcionado == 1:
        print("v. O grafo é fortemente conexo?")
    print("vi. O grafo possui ciclos?")
    print("vii. O grafo é Euleriano? Responda com 'Euleriano', 'Semi-Euleriano' ou 'Não'")
    opcaoVerificacao = input()
    g.Verificacoes(opcaoVerificacao)

if n == "7":
    vInicial = int(input("Qual o vértice inicial? "))
    g.ArvoreBFS(vInicial)



