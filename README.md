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

- `CompFortementeCnx`: encontra a quantidade de componentes formetmente conexas no grafo.
  - Recebe: nada
  - Retorna: número de componentes fortemente conexas.
  - Funcionamento

    Bbaseado no algoritmo de Kosaraju para componentes fortemente conexas.

    O método foi planejado para funcionar com grafos direcionados, portanto retornará -1 se essa exigência não for atendida

    Uma variável chamada tempos_fechamento irá guardar em um vetor várias tuplas no formato (tempo_de_fechamento, vértice). Esse vetor é gerado pelo método auxiliar '_temporizar()'.

    A fim de garantir que os tempos de fechamento estarão ordenados, o método sort (da própria linguagem) é chamado para ordenar em ordem crescente, levando em consideração somente o primeiro elemento das tuplas, ou seja, o tempo de fechamento.

    Continuando o algoritmo, criamos uma cópia do grafo atual e invertemos os seus arcos, de modo que agora obtemos um grafo transposto.

    As componentes conexas, agora, são obtidas a partir do resultado do método '_temporizarReversa()', chamada a partir do grafo transposto, utilizando os tempos de fechamento como parâmetro. A variável 'componentes_conexas' armazena um vetor de vetores. Esses vetores contém os vértices que participam de um componente.

    Finalmente, o retorno é dado pelo tamanho do vetor armazenado em 'componentes_conexas'.

- `nomedometodo`: descrição do que o método faz pela classe.
  - Recebe: o que é passado para o método
  - Retorna: o que o método retorna.
