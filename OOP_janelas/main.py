"""Janela principal e orquestracao da aplicacao."""

import tkinter as tk
from tkinter import ttk

from calculos import EquacaoSegundoGrau
from entrada import Entrada
from grafico import GraficoParabola
from resultados import Resultados


class AplicacaoBhaskara:
    """Monta a interface e coordena entrada, calculos e apresentacao."""

    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora de Bhaskara")
        self.janela.geometry("1100x700")
        self.janela.minsize(850, 560)
        self._configurar_estilos()
        self._criar_interface()

    def _configurar_estilos(self):
        self.estilo = ttk.Style(self.janela)
        try:
            self.estilo.theme_use("clam")
        except tk.TclError:
            pass
        self.estilo.configure("Titulo.TLabel", font=("TkDefaultFont", 16, "bold"))

    def _criar_interface(self):
        container = ttk.Frame(self.janela, padding=16)
        container.pack(fill="both", expand=True)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(1, weight=1)

        ttk.Label(
            container,
            text="Calculadora de equacao do 2o grau",
            style="Titulo.TLabel",
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 14))

        painel_esquerdo = ttk.Frame(container)
        painel_esquerdo.grid(row=1, column=0, sticky="nsw", padx=(0, 16))
        self.entrada = Entrada(painel_esquerdo)
        self.entrada.pack(fill="x")

        ttk.Button(
            painel_esquerdo,
            text="Calcular",
            command=self.calcular,
        ).pack(fill="x", pady=(12, 0))

        ttk.Button(
            painel_esquerdo,
            text="Limpar",
            command=self.limpar,
        ).pack(fill="x", pady=(6, 0))

        self.resultados = Resultados(painel_esquerdo)
        self.resultados.pack(fill="x", pady=(12, 0))

        self.grafico = GraficoParabola(container)
        self.grafico.grid(row=1, column=1, sticky="nsew")

    def calcular(self):
        configuracao = self.entrada.obter_configuracao()
        if configuracao is None:
            return

        equacao = EquacaoSegundoGrau(
            configuracao["a"],
            configuracao["b"],
            configuracao["c"],
        )
        delta = equacao.calcular_delta()
        raizes = equacao.calcular_raizes()
        vertice = equacao.calcular_vertice()
        pontos = equacao.calcular_pontos(
            configuracao["inicio_x"],
            configuracao["fim_x"],
            configuracao["quantidade"],
        )

        self.resultados.exibir(equacao, delta, raizes, vertice)
        self.grafico.exibir(
            equacao,
            pontos,
            vertice,
            raizes,
            configuracao["tema"],
            configuracao["grade"],
        )

    def limpar(self):
        self.entrada.limpar()
        self.resultados.limpar()
        self.grafico.limpar()

    def executar(self):
        """Inicia o loop de eventos da janela."""
        self.janela.mainloop()


if __name__ == "__main__":
    aplicacao = AplicacaoBhaskara(tk.Tk())
    aplicacao.executar()
