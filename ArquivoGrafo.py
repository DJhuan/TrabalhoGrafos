import re
from pathlib import Path

PROJECT_DIR = Path(__file__).parent

path = PROJECT_DIR / 'g.txt'
vertices = []
arestas = []

class ArquivoGrafo:
    def __init__(self, filepath):
        self.filepath = filepath
        

        self.vertices = []
        self.arestas = []

    def carregar_dados(self):
        with open(self.filepath, 'rt') as document:
            buffer = ""
            match = False
            while not match:
                buffer += document.read(1)

                bufferAvaliation = re.search("V={", buffer.replace(' ', ''))
                if bufferAvaliation: match = True
            
            # --- Leitura dos vértices
            buffer = ""
            while not buffer.endswith('}'):
                buffer += document.read(1)
                if buffer.endswith(','): 
                    vertices.append(buffer.replace(',', '').replace(' ', ''))
                    buffer = ""
            vertices.append(buffer.split('}')[0].replace(' ', ''))
            # --- Fim da leitura dos vértices


            # --- Leitura das arestaas
            buffer = ""

            match = False
            while not match:
                buffer += document.read(1)

                bufferAvaliation = re.search("A={", buffer.replace(' ', ''))
                if bufferAvaliation: match = True

            buffer = ""
            while not buffer.endswith('}'):
                buffer += document.read(1)
                bufferAvaliation = None

                if buffer.endswith(')'):
                    bufferAvaliation = re.search("(.*,.*)|(.*,.*,.*)", buffer.replace(' ', ''))
                if bufferAvaliation:
                    #print(buffer)
                    buffer = buffer.replace(' ', '').replace('(', '').replace(")", '').split(',')
                    if buffer[0] == '': buffer.pop(0)
                    if len(buffer) == 2: arestas.append((buffer[0], buffer[1]))
                    elif len(buffer) == 3: arestas.append((buffer[0], buffer[1], int(buffer[2])))
                    else: raise IndexError("A quantidade de argumentos não faz sentido!")
                    buffer = ""

            # --- Fim da leitura das arestas
            self.vertices = vertices
            self.arestas = arestas

arq = ArquivoGrafo(path)
arq.carregar_dados()
print(arq.vertices, arq.arestas)
    