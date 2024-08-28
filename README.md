# Trabalho prático

Algoritmos em Grafos

Universidade Federal de Lavras

## Discentes

- Jhuan Carlos Sabaini Dassie
- Lívia Della Garza Silva
- Marina Hermógenes Siqueira

---

## Sumário

1. [Objetivo](#objetivo)
2. [Implementação](#implementação)
   1. [Grafo](#grafo)
        - [Atributos](#atributos)
        - [Metodos](#métodos)

---

## Objetivo

O objetivo deste trabalho é implementar algoritimos para análise das propriedades de um grafo.

---

## Implementação

A implementação foi feita completamente sobre uma classe chamada Grafo. Como ideia inicial, pensamos em implementar o grafo em duas estruturas diferentes (matriz e lista de adjacência), tirando proveito disso ao desenvolver os métodos que analisam as propriedades do grafo.

### Grafo

#### Atributos

- `vertices`: lista com os vértices inseridos.
- `direcionado`: booleano que indica se o grafo é direcionado / orientado.
- `lista`: dicionário usado para representar a lista de adjacência dos vértices. Aqui, as chaves do dicionário corresponde ao vértice de onde parte a aresta, enquanto os valores são as arestas, representadas por tuplas que armazenam o vértice de chegada e o peso da aresta.
- `matriz`: matriz de adjacência.
- `arestas`: matriz utilizada para armazenar o identificador das arestas.

#### Métodos

- `__str__`: método que transforma o grafo em uma representação escrita que pode ser escrita no terminal ou então armazenada num arquivo. A representação escrita conta com a matriz de adjacência, matriz de id de arestas e lista de adjacência.
  - Recebe: nada.
  - Retorna: uma string.

- `AdicionarArestas`: Adiciona uma nova aresta no grafo.
  - Recebe:
    - `id`: identificador que representa a aresta.
    - `v1`: vétice de onde parte a aresta.
    - `v2`: vétice de chegada da aresta.
    - `valor`: peso da aresta. Por padrão, seu valor é 0.
  - Retorna: nada.

- `RemoverArestas`: remove uma aresta do grafo.
  - Recebe:
    - `v1`: vétice de onde parte a aresta.
    - `v2`: vétice de chegada da aresta.
  - Retorna: nada.

- `AdicionarVertice`: Adiciona um novo vértice no grafo.
  - Recebe:
    - `vertice`: nome do vértice adicionado que será a nova chave no dicionário e linha da matriz de adjacência.
  - Retorna: nada.

- `RemoverVertice`: Remove um vértice do grafo.
  - Recebe:
    - `vertice`: nome do vértice removido.
  - Retorna: nada.

- `CompConexos`: Calcula o número de componentes conexos em um grafo não direcionado.
  - Recebe: nada.
  - Retorna: número de componentes conexos do grafo.
  - Funcionamento

    Como o funcionamento do algoritmo depende do grafo ser não orientado, o método retorna -1 caso a condição não seja satisfeita.

    O algoritmo itera por todos os vértices do grafo e inicia uma busca em profundidade usando o método auxiliar '_dfs()' para todos os vértices que ainda não foram visitados. Todos os vértices descobertos durante a busca são varcados como visitados e 1 é somado ao número de componentes.

    Ao fim, o número de componentes é retornado.

- `CompFortementeCnx`: encontra a quantidade de componentes formetmente conexas no grafo.
  - Recebe: nada
  - Retorna: número de componentes fortemente conexas.
  - Funcionamento

    Baseado no algoritmo de Kosaraju para componentes fortemente conexas.

    O método foi planejado para funcionar com grafos direcionados, portanto retornará -1 se essa exigência não for atendida

    Uma variável chamada tempos_fechamento irá guardar em um vetor várias tuplas no formato (tempo_de_fechamento, vértice). Esse vetor é gerado pelo método auxiliar '_temporizar()'.

    A fim de garantir que os tempos de fechamento estarão ordenados, o método sort (da própria linguagem) é chamado para ordenar em ordem crescente, levando em consideração somente o primeiro elemento das tuplas, ou seja, o tempo de fechamento.

    Continuando o algoritmo, criamos uma cópia do grafo atual e invertemos os seus arcos, de modo que agora obtemos um grafo transposto.

    As componentes conexas, agora, são obtidas a partir do resultado do método '_temporizarReversa()', chamada a partir do grafo transposto, utilizando os tempos de fechamento como parâmetro. A variável 'componentes_conexas' armazena um vetor de vetores. Esses vetores contém os vértices que participam de um componente.

    Finalmente, o retorno é dado pelo tamanho do vetor armazenado em 'componentes_conexas'.

#### Métodos auxiliares

- `bfsConexo`: busca em largura para verificar se um grafo é conexo.
  - Recebe:
    `visitado`: vetor de vértices visitados.
    `lista`: dicionario que representa um grafo como lista de adjacencia.
    `vertice`: vertice inicial.
  - Retorna: nada.
  - Funcionamento:

      Inicia uma fila que marca a ordem de exploração dos vértices com o parâmetro 'vertice' incluído.

      Indica também que, no vetor de vértices visitados, a posição que representa o estado do vertice inicial ele foi achado.

      Enquanto houver itens a ser explorados na fila, removemos o que há no início dela e o chamamos de 'i'.

      Iteramos dentro da lista de adjacência de 'i' buscando os vértices que ainda não foram visitados, marcando-os como achados e adicionando na fila de exploração.

      Depois de iterar marcamos o vértice atual 'i' como visitado.

      Ao fim das iterações, o vetor 'visitado' estará com os dados dos vértices encontrados ou não.

- `_dfs`: função de busca em profundidade planejada para marcar o tempo de exploração de cada vértice.
  - Recebe:
    - `v_ini`: vérice que inicia a busca.
    - `tempo`: último tempo marcado.
    - `tempos`: vetor de tuplas (tempo_de_fechamento, vértice).
  - Retorna:
    - `tempos`: mesmo que acima.
    - `tempo`: último tempo marcado.
    - `visitados`: set de vértices já visitados.
  - Funcionamento

    Uma pilha 'a_explorar' manterá os vértices a sereme explorados na DFS. Iniciamos ela já com o vértice inical.

    Enquanto houver vértices na pilha:

    Buscamos o vértive no topo da pilhae, 'v_atual', e:

    1 - Se ele não tiver sido visitado, dizemos que ele foi visitado e somamos 1 no tempo.

    Depois, para cada filho do v_atual não explorado, colocamos ele na fila de exploração, e dizemos que houve uma exploração de um vértice novo.

    No caso de não houver a exploração de um vértice novo, adicionamos no vetor de tempos de fechamento uma tupla composta por ('tempo', 'v_atual'), somamos mais 1 no tempo, e removemos o topo da pilha.

    2 - Se o vértice que está no topo da pilha já tiver sido visitado, adicionamos uma nova tupla ('tempo', 'v_atual') ao vetor tempos, somamos 1 no tempo e removemos o item do topo da lista.

    Ao fim, retorna-se os tempos de fechamento, o último tempo registrado e os vértices já visitados.
  
- `_temporizar`: atribui um tempo de fechamento para cada vértice do grafo baseado numa exploração por profundidade.
  - Recebe: nada
  - Retorna: um vetor com tuplas no formato (tempo_de_fechamento, vértice)
  - Funcionamento

    Para cada vértice não visitado no grafo, inicia uma busca em profundidade.

    O método alimenta, a cada iteração, a busca em profundidade com o vértice a ser explorado, o último tempo de fechamento usado e os vértices já visitados.

    Ao fim, retorna um vetor de tuplas no formato (tempo_de_fechamento, vértice).

- `_temporizarReversa`: funcionamento semelhante ao método '_temporizar()', mas o critério para exploração dos vértices é diferente.
  - Recebe: um vetor de tuplas (tempo_de_fechamento, vértice).
  - Retorna: um vetor com um componente fortemente conexo.
  - Funcionamento:

    Semelhante ao método '_temporizar()', ambém inicia uma busca em profundidade por todos os vértices ainda não visitados, todavia, aqui levamos em consideração uma ordem de como os vértices serão explorados.

    A ordem é determinada pelo argumento 'tempo_decresc', que será iterado reversamente. Aqui, espera-se uma lista de tuplas (tempo_de_fechamento, vértice), ordenada crescentemente em relação ao primeiro parâmetro.

    Outra diferença é que esse método não se importa mais em marcar o tempo de maneira correta, ou então de atualizar o vetor 'tempos' durante as iterações, isso porque o que será retornado pela função '_dfs()' já será um componente fortemente conexo, então esse componente é adicionado diretamente na variável 'tempos', que é retornada ao fim da execução do método.

- `nomedometodo`: descrição do que o método faz pela classe.
  - Recebe: o que é passado para o método
  - Retorna: o que o método retorna.
