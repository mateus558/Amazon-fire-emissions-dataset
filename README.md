# Análise das queimadas no Brasil

*Trabalho parte da disciplina de Mineração de Dados (2020/2) do PPGCC-UFJF*

## Objetivo

Analisar os dados do BDQueimadas do programa queimadas do Instituto Nacional de Pesquisas Espaciais (INPE) utilizando técnicas de mineração de dados.

## Programa Queimadas

É o programa de monitoramento da ocorrência de fogo na vegetação criado pelo INPE para a América do sul e central, África e Europa. O **BDQueimada** é o Banco de dados do programa queimadadas do INPE com os dados coletados dos focos de fogo a partir de imagens de satélite .

## Dataset
É composto por dados extraídos do BDQueimada de focos de fogo ativo de queimadas e de incêndios florestais detectados por satélite. Foram extraídos os dados compreendendo o período de 01/01/2017 até 24/09/2020 contendo 11953450 registros de focos de fogo.

#### Colunas categóricas
|   Coluna  |                                 Descrição                                |       Exemplo       |
|:---------:|:------------------------------------------------------------------------:|:-------------------:|
|  datahora | Horário de referência da passagem do satélite.                           | 2017/08/18 01:06:19 |
|  satelite | Nome do algorítmo utilizado e referencia ao satélite provedor da imagem. | NOAA-20             |
|    pais   | Nome do país.                                                            | Brasil              |
|   estado  | Nome do estado.                                                          | GOIAS               |
| municipio | Nome do município.                                                       | JUSSARA             |
|   bioma   | Nome do Bioma segundo referência do IBGE 2004.                           | Amazonia            |

#### Colunas numéricas

|    Coluna    |                                     Descrição                             |  Válido | Inválido |
|--------------|---------------------------------------------------------------------------|:-------:|:--------:|                                                 
|  diasemchuva | Número de dias sem chuva até a detecção do foco.                          |   >= 0  |   -999   |
| precipitacao | Valor da precipitação acumulada no dia até o momento da detecção do foco. |   >= 0  |   -999   |
|   riscofogo  | Valor do Risco de Fogo previsto para o dia da detecção do foco.           | 0.0-1.0 |   -999   |

|   Coluna  |                                       Descrição                                       |           Domínio           |
|:---------:|:-------------------------------------------------------------------------------------:|:---------------------------:|
|  latitude | Latitude do centro do píxel de fogo ativo apresentada em unidade de graus decimais.   |  90 até -90 (4 casas dec.)  |
| longitude | Longitude do centro do píxel de fogo ativo apresentada em unidade de graus decimais.  | 180 até -180 (4 casas dec.) |
|    frp    | Energia radiante emitida por unidade de tempo pela vegetação queimada. MW (megawatts) |     double (1 casa dec.)    |

