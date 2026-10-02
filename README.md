# 🐍 Calculadora de Bhaskara

<div align="center">

### Três formas de resolver uma equação do 2º grau

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![Matplotlib](https://img.shields.io/badge/Matplotlib-gráficos-11557C?style=for-the-badge&logo=python&logoColor=FFD43B)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-F7DF1E?style=for-the-badge&labelColor=3776AB)

</div>

Projeto desenvolvido na disciplina de **Técnicas de Programação** do IFMA Monte Castelo. A aplicação calcula o delta, as raízes e o vértice de uma equação do segundo grau, além de representar a parábola em um gráfico.

## ✨ O que este projeto apresenta

- 🧮 Cálculo completo de equações do segundo grau;
- 📈 Visualização da parábola, do vértice e das raízes reais;
- 🧱 Comparação entre programação estruturada e orientação a objetos;
- 🖥️ Uma versão com interface gráfica usando `tkinter`.

## 🛠️ Requisitos

- **Python 3.11**;
- **Matplotlib**;
- **Tkinter**, incluído na instalação padrão do Python no Windows e usado pela versão com janelas.

Na raiz do repositório, instale o Matplotlib com:

```powershell
py -3.11 -m pip install matplotlib
```

## 📂 Versões disponíveis

### 1. 🧩 Estruturado

A pasta `Estruturado/` divide o programa em módulos e utiliza funções para validar os dados, realizar os cálculos, exibir os resultados e gerar o gráfico. A interação acontece pelo terminal.

**Como executar:**

```powershell
py -3.11 Estruturado/main.py
```

Informe os coeficientes `a`, `b` e `c`. Os resultados serão exibidos no terminal e o gráfico da parábola será aberto pelo Matplotlib.

### 2. 🏗️ OOP

A pasta `OOP/` implementa a calculadora com classes como `EquacaoSegundoGrau`, `Entrada`, `Resultados` e `GraficoParabola`. A aplicação continua no terminal, mas os dados e comportamentos ficam organizados em objetos.

**Como executar:**

```powershell
py -3.11 OOP/main.py
```

Digite os coeficientes solicitados. O programa exibirá os resultados e abrirá o gráfico.

### 3. 🪟 OOP_janelas

A pasta `OOP_janelas/` combina orientação a objetos com uma interface gráfica em `tkinter`. É possível informar os coeficientes, escolher o intervalo e a quantidade de pontos do gráfico, selecionar o tema e ativar ou desativar a grade.

**Como executar:**

```powershell
py -3.11 OOP_janelas/main.py
```

Preencha os campos da janela e clique em **Calcular**. O gráfico será renderizado dentro da própria aplicação.

## ⚖️ Comparação rápida

| Versão | Estrutura | Interface | Ponto forte |
| --- | --- | --- | --- |
| `Estruturado` | Funções e módulos | Terminal | Fluxo direto e fácil de acompanhar. |
| `OOP` | Classes e objetos | Terminal | Melhor encapsulamento e separação de responsabilidades. |
| `OOP_janelas` | Classes e objetos | Janela gráfica | Experiência visual mais completa e configurável. |

### Em uma frase

🧩 **Estruturado** é ótimo para entender o passo a passo do algoritmo.  
🏗️ **OOP** organiza melhor os dados e comportamentos.  
🪟 **OOP_janelas** mantém essa organização e acrescenta uma experiência gráfica.

## 🎓 Contexto acadêmico

**Disciplina:** Técnicas de Programação  
**Instituição:** IFMA - Campus Monte Castelo  
**Tema:** Aula prática com VS Code e GitHub