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
    if not valorado:
        while linha[contador] != '{':
            contador = contador+1
        contador = contador+1
        while linha[contador] != '}':
            if linha[contador] != ',':
                qtVertices = qtVertices+1
            contador = contador+1
        g = Grafo(qtVertices, direcionado, valorado)
        valor = 1

    while linha[contador] != '{':
        contador = contador+1
    while linha[contador] != '}':
        v1 = int(linha[contador+2])
        v2 = int(linha[contador+4])
        g.AdicionarArestas(v1,v2,valor)
        contador = contador+6
print("Grafo em matriz: ")
g.Imprime()
    
print("O que você deseja fazer?")
print("1: Imprimir o grafo em matriz")
print("2: Adicionar vérices")
print("3: Remover vértices")
print("4: Adicionar arestas")
print("5: Remover arestas")
n = input()

if n == "1":
    g.imprime()

if n == "2":
    g.AdicionarVertices()
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


