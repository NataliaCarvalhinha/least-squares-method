# Método dos Mínimos Quadrados para a Previsão de Infartos  

## Descrição

Este projeto visa a utilização do método dos mínimos quadrados para a previsão de mortes por infarto com base em dados de saúde. O trabalho foi realizado como parte do curso de Álgebra Linear II da Universidade Federal do Rio de Janeiro.

## Autor

Natália Carvalhinha Sacco de Lemos Basto

### Conteúdo do Projeto

O projeto está organizado da seguinte maneira:

#### 1. Introdução

Descrição geral do problema abordado.

#### 2. Método

Explicação detalhada do método dos mínimos quadrados aplicado ao problema.

#### 3. Resultados

Apresentação dos resultados obtidos após a aplicação do método para casos de morte e não morte.

#### 4. Conclusão

Conclusões e considerações finais sobre a eficácia do método utilizado.

#### 5. Referências

Listagem das referências bibliográficas utilizadas no desenvolvimento do projeto.

## Uso do Código

O código em Python presente neste repositório realiza a implementação do método dos mínimos quadrados para a previsão de mortes por infarto.

## Execução do Código

1. Execute o arquivo main.py.
2. O programa solicitará a entrada de dados relacionados à saúde do paciente.
3. Com base nos coeficientes calculados, o programa determinará se há previsão de morte por infarto.

## Dependências

Pandas: Utilizado para manipulação de dados tabulares.

## Estrutura do Código

O código está organizado em funções que realizam etapas específicas do método dos mínimos quadrados.

- print_matriz(Titulo1, A): Função para imprimir uma matriz.
- mutiplicarMatrizes(A, B): Função para multiplicar duas matrizes.
- matrizIdentidade(tamanho): Função para gerar uma matriz identidade.
- matriz_inversa(matriz, matriz_identidade): Função para calcular a matriz inversa.
- minimosQuadrados(A, b): Função para calcular os coeficientes pelo método dos mínimos quadrados.
- TransformadaArqLista(A, b, aprox, linhas, colunas, df, nome_colunas): Função para transformar os dados do arquivo em listas de matrizes.
- main(): Função principal que realiza a leitura dos dados, transformação em matrizes e cálculo dos coeficientes.
- teste(): Função para realizar um teste interativo, inserindo dados fictícios e obtendo a previsão de morte ou não.

## Referências

BOLDRINI, José Luiz et al. Álgebra Linear. 3. ed. São Paulo: Harbra, 1986.
CABRAL, Marco A. P.; GOLDFELD, Paulo. Curso de Álgebra Linear: fundamentos e aplicações. 3. ed. Rio de Janeiro: Instituto de Matemática, 2012.
