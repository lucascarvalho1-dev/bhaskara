# Calculadora de Bhaskara

Projeto desenvolvido na disciplina de Técnicas de Programação do IFMA Monte Castelo. O repositório apresenta três versões de uma calculadora de equações do segundo grau, com cálculo das raízes, do vértice e visualização da parábola.

## Requisitos

- Python 3.11
- `matplotlib`

No Windows, a partir da raiz do repositório, instale a dependência com:

```powershell
py -3.11 -m pip install matplotlib
```

A versão `OOP_janelas` também usa `tkinter`, que acompanha a instalação padrão do Python no Windows.

## Versões

### Estruturado

A pasta `Estruturado/` organiza o programa em módulos e utiliza funções para validar os dados, realizar os cálculos, exibir os resultados e gerar o gráfico. A interação acontece pelo terminal.

Para executar:

```powershell
py -3.11 Estruturado/main.py
```

Informe os coeficientes `a`, `b` e `c` no terminal. Ao final, os resultados são mostrados e o gráfico da parábola é aberto pelo Matplotlib.

### OOP

A pasta `OOP/` implementa a mesma calculadora usando classes, como `EquacaoSegundoGrau`, `Entrada`, `Resultados` e `GraficoParabola`. A aplicação continua sendo executada pelo terminal, mas as responsabilidades ficam reunidas em objetos.

Para executar:

```powershell
py -3.11 OOP/main.py
```

Digite os coeficientes solicitados. O programa exibe os resultados no terminal e abre o gráfico pelo Matplotlib.

### OOP_Janelas

A pasta `OOP_janelas/` usa orientação a objetos e oferece uma interface gráfica com `tkinter`. Nela, é possível informar os coeficientes, definir o intervalo e a quantidade de pontos do gráfico, escolher o tema e ativar ou desativar a grade. O gráfico é incorporado à própria janela com Matplotlib.

Para executar:

```powershell
py -3.11 OOP_janelas/main.py
```

Preencha os campos da janela e clique em **Calcular**.

## Comparação

| Versão | Organização | Interface | Característica principal |
| --- | --- | --- | --- |
| `Estruturado` | Funções e módulos | Terminal | É a abordagem mais direta e simples de acompanhar passo a passo. |
| `OOP` | Classes e objetos | Terminal | Encapsula os dados e comportamentos, facilitando a organização e a manutenção. |
| `OOP_janelas` | Classes e objetos | Janela gráfica | Reaproveita a orientação a objetos e oferece uma interação mais visual e configurável. |

Em resumo, a versão estruturada é adequada para entender o fluxo básico do algoritmo. A versão `OOP` separa melhor as responsabilidades do sistema, enquanto `OOP_janelas` acrescenta uma experiência gráfica mais completa sem abandonar essa organização.