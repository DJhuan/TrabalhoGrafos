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
- `lista`: dicionário usado para representar a lista de adjacência dos vértices. Aqui, as chaves do dicionário correspondem ao vértice de onde parte a aresta, enquanto os valores são as arestas, representadas por tuplas que armazenam o vértice de chegada e o peso da aresta.
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

- `Conexo`: informa se um grafo é conexo ou não.
  - Recebe: nada.
  - Retorna: inteiro.
  - Funcionamento
    Temos duas opções a serem seguidas nesse caso, uma em que o grafo é direcionado e a outra em que ele não é.

    1 - Caso seja direcionado, declaramos um vetor 'visitado' que cada posição informa o estado de exploração de um vértice ("N" - não visitado, "A" - achado, "V" - visitado) e, incialmente, todos estão em estado "N". Em seguida informamos que o vértice 0 foi achado.

    Declaramos um dicionário chamado 'grafo', em que adicionamos todos os vértices como chaves e iniciamos os valores das chaves como um vetor. Para cada vértice no nosso grafo original, buscamos quais são as arestas que saem dele e populamos o dicionário convertendo os arcos para arestas bidirecionais.

    Chamamos o método 'bfsConexo()' utilizando como parâmetros o vetor de vértices visitados, o grafo convertido em não direcionado e o vértice inicial (0).

    Daí, iteramos sobre 'visitado', caso exista um vértice que não tenha sido visitado retornamos 0, indicando que não é conexo, casocontrário retornamos 1.

    2 - Caso não seja direcionado, então declaramos um vetor que marca os vértices visitados, chamado 'visitado', e iniciamos todas as posições como falsas.

    Chamamos dfs(), passando como parâmetros 0 (vértice inicial) e o vetor de 'visitado'. Ao fim do procedimento, toda posição que estiver com o valor lógico True representa um vértice visitado.

    Se todas as posições de 'visitado' têm valor lógico True, dizemos que ele é conexo retornando 1, caso contrário retornamos 0.

- `CompConexos`: Calcula o número de componentes conexos em um grafo não direcionado.
  - Recebe: nada.
  - Retorna: número de componentes conexos do grafo.
  - Funcionamento

    Como o funcionamento do algoritmo depende do grafo ser não orientado, o método retorna -1 caso a condição não seja satisfeita.

    O algoritmo itera por todos os vértices do grafo e inicia uma busca em profundidade usando o método auxiliar '_dfs()' para todos os vértices que ainda não foram visitados. Todos os vértices descobertos durante a busca são varcados como visitados e 1 é somado ao número de componentes.

    Ao fim, o número de componentes é retornado.

- `CompFortementeCnx`: encontra a quantidade de componentes formetmente conexas no grafo.
  - Recebe: nada.
  - Retorna: número de componentes fortemente conexas.
  - Funcionamento

    Baseado no algoritmo de Kosaraju para componentes fortemente conexas.

    O método foi planejado para funcionar com grafos direcionados, portanto retornará -1 se essa exigência não for atendida.

    Uma variável chamada tempos_fechamento irá guardar em um vetor várias tuplas no formato (tempo_de_fechamento, vértice). Esse vetor é gerado pelo método auxiliar '_temporizar()'.

    A fim de garantir que os tempos de fechamento estarão ordenados, o método sort (da própria linguagem) é chamado para ordenar em ordem crescente, levando em consideração somente o primeiro elemento das tuplas, ou seja, o tempo de fechamento.

    Continuando o algoritmo, criamos uma cópia do grafo atual e invertemos os seus arcos, de modo que agora obtemos um grafo transposto.

    As componentes conexas, agora, são obtidas a partir do resultado do método '_temporizarReversa()', chamada a partir do grafo transposto, utilizando os tempos de fechamento como parâmetro. A variável 'componentes_conexas' armazena um vetor de vetores. Esses vetores contém os vértices que participam de um componente.

    Finalmente, o retorno é dado pelo tamanho do vetor armazenado em 'componentes_conexas'.

- `Cortes`: Aplica o algoritmo de Tarjan para vértices de articulação e arestas ponte.
  - Recebe: um inteiro que identifica o objetivo da aplicação do algoritmo.
  - Retorna: A lista de vértices de articulação ou de arestas ponte.
  - Funcionamento
    O método inicializa todos os elementos da lista de visitados como "N" (não visitados), os vetores de tempo de descoberta, low e pai como None em todos os elementos, e o tempo como 1.

    Se o id for 1, é criada uma lista de arestas ponte e o algoritmo de Tarjan para arestas ponte é chamado para cada vértice não visitado. Depois, é retornada a lista de arestas ponte.

    Se o id for 2, é criada uma lista de vértices de articulação e o algoritmo de Tarjan para vértices de articulação é chamado para cada vértice não visitado. Depois, é retornada a lista de vértices de articulação.

- `ArvoreBFS`: encontra a árvore de busca em largura.
  - Recebe: vértice inicial, 0 por padrão.
  - Retorna: identificadores das arestas da árvore de busca em largura.
  - Funcionamento
    Inicializamos a lista das arestas da árvore como uma lista vazia, é a lista dos vértices visitados tem todos os seus elementos inicializados como "N" (não visitado). Adicionamos o vértice inicial na fila e o colocamos como achado ("A").

    Enquanto a fila não estiver vazia, exploramos o primeiro elemento e verificamos se cada vizinho já foi visitado ou achado. Se não, colocamos o vizinho como achado ("A"), adicionamos ele na fila e adicionamos a aresta que sai do vértice para esse vizinho na lista de arestas. Depois de explorar o vértice, colocamos ele como visitado ("V").

    Quando a fila finalmente estiver vazia, retornamos a lista de arestas.

- `ArvoreGeradoraMinima`: encontra o valor total da árvore geradora mínima.
  - Recebe: nada.
  - Retorna: inteiro que representa a soma de todas as arestas da árvore geradora mínima.
  - Funcionamento
    O método começa criando uma lista de arestas, que inicialmente é vazia. Percorremos a matriz de adjacência do grafo, colocando todas as arestas encontradas na lista de arestas, com a configuração (valor, v1, v2). Como o método funciona apenas para grafos não direcionados, colocamos a condição de que o vértice de saída tem que ser menor que o vértice de entrada, para retirar loops e não representar a mesma aresta duas vezes, como é feito em grafos não direcionados. Depois, a lista é ordenada pelo valor das arestas.

    Criamos um dicionário, que representa a árvore geradora mínima, e inicializamos os valores correspondentes a todas as chaves como uma lista vazia. Inicializamos também o valor da árvore como 0.

    Enquanto a quantidade de arestas da árvore for menor que a quantidade de vértices-1 e a lista de arestas não estiver vazia, pegamos o elemento de menor valor da lista e adicionamos ele na árvore. Verificamos se a adição desse elemento cria ciclos, com a ajuda da função CicloArvoreGeradora. Se criar ciclos, a aresta é retirada. Se não, adicionamos o valor da aresta ao valor da árvore.

    Quando uma das condições de parada for atingida, retornamos a soma de todas as arestas da árvore.

- `OrdemTopologica`: encontra uma possibilidade de ordem de execução, utilizando a busca em profundidade.
  - Recebe: 
    - `listaExecucao`: inicialmente vazia.
    - `visitado`: verifica se cada vértice foi visitado. Inicializado como "N" para todos os vértices.
  - Retorna: lista que contém a ordem de execução.
  - Funcionamento
    O método chama a função dfsOrdemTop para cada vértice não visitado, marcando o vértice como "A" (achado).
    Como a função auxiliar adiciona os vértices no final da lista, o método retorna a lista invertida. 

- `Dijkstra`: encontra o caminho mínimo entre dois vértices utilizando o algoritmo de Dijkstra.
  - Recebe:
    - `vInicial`: de onde saímos com a busca.
    - `vFinall`: onde queremos chegar com a busca.
  - Retorna: inteiro que representa a distância mínima entre os vértices.
  - Funcionamento
    O método foi planejado para funcionar com grafos não direcionados, portanto retornará -1 se essa exigência não for atendida.

    Primeiro o algoritmo declara um array, que armazena a distância do vértice inicial até o vértice da posição atual. Inicialmente todas as distâncias são iniciadas como infinitas, mas logo em seguida o vértice inicial recebe distância 0.

    Um heap é declarado, e armazenamos nele uma tupla com uma distância e um vértice. Incluímos nessa fila o vértice inicial e sua distância (0).

    Enquanto houver vértices a serem explorados no heap, dizemos que o vértice a ser explorado é a remoção do item que possui a menor distância até então.

    Se ele ainda não tiver sido visitado, atualizamos seu estado de exploração no array de visitados.

    Caso o vértice atual seja o vértice final, retornamos a distância armazenada no array de distâncias da posição correspondente ao vértice atual.

    Caso contrário, para cada vizinho do vértice que acabamos de visitar fazemos:

    Se ele não foi visitado, dizemos que a candidata à nova distância do vértice é a distância do vértice atual mais o peso da aresta que o liga ao seu vizinho.

    Se a nova distância for menor que a que já está armazenada para o vizinho, atualizamos esse valor e adicionamos o vértice no heap.

    Ao final de tudo, caso o vértice final não tenha sido encontrado, retornamos -1, indicando que não existe caminho até ele.

- `FluxoMaximo`: método que calcula o valor do fluxo máximo do grafo, considerando o vértice de saída como 0 e o de chegada n-1.
  - Recebe: nada
  - Retorna: inteiro que representa o fluxo máximo do grafo.
  - Funcionamento

    O método foi planejado para funcionar com grafos direcionados, portanto retornará -1 se essa exigência não for atendida.

    Depois ela define o vértice de origem como 0 e o de destino como o último vertice, inicializa uma lista "pai" pra armazenar o caminho encontrado e também inicializa uma variável "fluxo maximo" pra armazenar o fluxo total.

    Enquanto for possível explorar o grafo a partir da função 'bfs()', significa que há um caminho que sai do vértice inicial para o final. Usando o caminho obtido, o menor peso de aresta, representado por 'fluxo_caminho' é anotado e o fluxo máximo é atualizado.

    Em seguida as capacidades resuduais são atualizadas no grafo. Isso significa que, para cada aresta do caminho, removemos o valor de 'fluxo_caminho' da aresta orientada de modo saida -> chegada e somamos 'fluxo_caminho' na aresta orientada na direção chegada -> saida.

    No final retorna o valor do fluxo máximo encontrado.

- `FechoTransitivo`: encontra os vértices alcançados por determinado vértice.
  - Recebe:
    - `pilha`: pilha usada na busca em profundidade. Inicialmente vazia.
    - `visitado`: lista que verifica se o vértice foi visitado, achado ou não foi visitado.
    - `listaVertices`: lista que contém o fecho transitivo do vértice. Inicialmente vazia.
  - Retorna: uma lista com o fecho transitivo do vértice 0.
  - Funcionamento
    O método marca o vértice inicial como "A" (achado) e o adiciona na pilha.

    Enquanto a pilha não estiver vazia, pegamos seu último elemento e verificamos se cada vizinho foi explorado. Se não, marca-o como "A" (achado), adiciona-o na pilha e no fecho transitivo, e chama o método novamente.

    Depois que todos os vizinhos forem processados, o vértice é marcado como "V" (visitado).

    Quando a pilha estiver vazia, o método retorna o fecho transitivo atualizado.

#### Métodos auxiliares

- `bfs`: busca por um vértice utilizando a busca em largura, mantendo também o caminho para chegar até ele.
  - Recebe:
    - `origem`: vértice de origem.
    - `destino`: vértice de destino.
    - `pai`: vetor com os pais dos vértices (ordem de visitação).
  - Retorna: booleano que indica se foi possível encontrar o vértice de destino.
  - Funcionamento:

    Declara uma fila que mantém a ordem de exploração dos vértices e um vetor para verificar quem foi visitado. O vértice inicial é imediatamente marcado como visitado.

    Enquanto houver itens na fila:

    Buscamos pelo primeiro item, e iteramos sobre a linha da matriz de adjacência que representa as arestas desse vértice.
    Caso a aresta exista, seu valor seja maior que zero e o filho ainda não tenha sido visitado: adicionamos o filho na fila, marcamos que ele foi visitado e atualizamos o vetor de pais, dizendo que o vértice aos quais os filhos estamos explorando é pai do filho marcado como visitado.

    Ao fim, retornamos se o filho foi visitado.

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

- `_inverterArcos`: inverte a orientação dos arcos da lista de adjacência. !A matriz de adjacência não é transposta nesta função!
  - Recebe: nada.
  - Retorna: nada.

- `TarjanA`: algoritmo de Tarjan para arestas ponte.
  - Recebe:
    - `vertice`: vértice que será processado.
    - `visitado`: lista que verifica se o vértice foi visitado, achado ou não foi visitado.
    - `low`: lista com o low de cada vértice.
    - `tempoD`: lista com os tempos de descoberta de cada vértice.
    - `pai`: lista com o pai de cada vértice.
    - `arestasPonte`: lista de arestas ponte.
    - `tempo`: tempo atual.
  - Retorna: nada.
  - Funcionamento

    O vértice é marcado como "A" (achado). O tempo de descoberta e o low do vértice recebem o valor do tempo.

    Para cada vizinho do vértice, se ele não foi visitado, o pai do vizinho recebe o valor do vértice e é chamado o método novamente, passando o vizinho como o parâmetro "vertice". Depois, é verificado se o low do vértice é mmaior que o low do vizinho. Se for, o low do vértice recebe o low do vizinho. Se o low do vizinho é maior que o tempo de descoberta do vértice, a aresta entre eles é uma ponte.

    Se o vizinho não foi visitado e não é o pai do vértice, significa que há uma aresta que retorna a um antecessor do vértice. Então, se o tempo de descoberta do vizinho for menor que o low do vértice, o low do vértice passa a ser o tempo de descoberta do vizinho.

    Depois de processar todos os vizinhos, o vértice é marcado como visitado.

- `TarjanV`: algoritmo de Tarjan para vértices de articulação.
  - Recebe:
    - `vertice`: vértice que será processado.
    - `visitado`: lista que verifica se o vértice foi visitado, achado ou não foi visitado.
    - `low`: lista com o low de cada vértice.
    - `tempoD`: lista com os tempos de descoberta de cada vértice.
    - `pai`: lista com o pai de cada vértice.
    - `verticesArtic`: lista de vértices de articulação.
    - `tempo`: tempo atual.
  - Retorna: nada.
  - Funcionamento

    O vértice é marcado como "A" (achado). O tempo de descoberta e o low do vértice recebem o valor do tempo.

    Para cada vizinho do vértice, se ele não foi visitado, o pai do vizinho recebe o valor do vértice e é chamado o método novamente, passando o vizinho como o parâmetro "vertice". Depois, é verificado se o low do vértice é mmaior que o low do vizinho. Se for, o low do vértice recebe o low do vizinho. Se o low do vizinho é maior ou igual ao o tempo de descoberta do vértice, o vértice é uma articulação.

    Se o vizinho não foi visitado e não é o pai do vértice, significa que há uma aresta que retorna a um antecessor do vértice. Então, se o tempo de descoberta do vizinho for menor que o low do vértice, o low do vértice passa a ser o tempo de descoberta do vizinho.

    Depois de processar todos os vizinhos, o vértice é marcado como visitado.

- `CicloArvoreGeradora`: verifica, a cada adição de uma aresta, se há ciclos ná árvore.
  - Recebe: um dicionário que representa a árvore geradora mínima.
  - Retorna: um booleano que verifica se possui ou não um ciclo.
  -Funcionamento

    O valor booleano que verifica a presença de ciclos é inicializado como falso. É também criada uma lista para verificar se o vértice foi visitado, achado ou não foi visitado, e uma pilha, inicialmente vazia. 

    Para cada vértice não visitado da árvore, o vértice é marcado como "A" (achado) e é chamada a função verifica_ciclo.

    Quando todos os vértices forem processados, o programa retorna o booleano, dizendo se possui ou não um ciclo.

- `verifica_ciclo`: tem a função de encontrar um ciclo em um grafo.
  - Recebe: 
    - `pai`: o pai do vértice que será processado.
    - `ciclo`: booleano que verifica a presença de ciclos.
    - `visitado`: lista que verifica se o vértice foi visitado, achado ou não foi visitado.
    - `pilha`: pilha que será usada na busca em profundidade.
    - `lista`: grafo que será processado.
    - `direcionado`: diz se o grafo é direcionado ou não.
  - Retorna: um booleano que verifica se possui ou não um ciclo.
  - Funcionamento

    O método pega o último elemento da pilha e verifica se cada vizinho já foi explorado. Se não, marca o vizinho como "A" (achado), adiciona ele na pilha e chama o método novamente, passado o vértice atual como pai. 

    Se o vizinho já foi achado, mas não foi explorado, e não é o pai do vértice, significa que há um ciclo. Se o grafo é direcionado, mesmo se o vizinho for o pai do vértice, há um ciclo. Nesses dois casos, a função retorna verdadeiro.

    O último elemento da pilha é retirado e a função retorna o valor booleano que verifica a presença de ciclos.  

- `dfsOrdemTop`: atualiza a lista de execução, a pertir da busca em profundidade.
  - Recebe:
    - `listaExecucao`: estado atual da lista de execução.
    - `visitado`: lista que verifica se o vértice foi visitado, achado ou não foi visitado.
    - `v`: vértice que será processado.
  - Retorna: a lista de execução atualizada.
  - Funcionamento

  Para cada vizinho do vértice, é chamado o método novamente, passando-o como v, além de marcá-lo como "A" (achado). Quando todos os vizinhos já tiverem sido processados, o vértice é marcado como "V" (visitado) e é adicionado na lista de execução. O método, enfim, retorna a lista de execução atualizada.

#### Métodos estáticos

- `conexosParaString`: Transforma uma lista de componentes conexos em uma grande string.
  - Recebe: lista de lista de vértices.
  - Retorna: o que o método retorna.

- `nomedometodo`: descrição do que o método faz pela classe.
  - Recebe: o que é passado para o método
  - Retorna: o que o método retorna.