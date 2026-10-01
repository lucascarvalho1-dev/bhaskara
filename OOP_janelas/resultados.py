"""Componentes visuais para exibicao dos resultados."""

import tkinter as tk
from tkinter import ttk


class Resultados(ttk.LabelFrame):
    """Painel que mostra delta, raizes e vertice."""

    def __init__(self, master):
        super().__init__(master, text="Resultados", padding=12)
        self.texto_var = tk.StringVar(value="Preencha os dados e clique em Calcular.")
        ttk.Label(
            self,
            textvariable=self.texto_var,
            justify="left",
            anchor="w",
        ).pack(fill="both", expand=True)

    @staticmethod
    def _formatar_numero(valor):
        return f"{valor:.6g}"

    def exibir(self, equacao, delta, raizes, vertice):
        linhas = [
            f"Equacao: {self._formatar_numero(equacao.a)}x^2 + "
            f"{self._formatar_numero(equacao.b)}x + "
            f"{self._formatar_numero(equacao.c)} = 0",
            f"Delta: {self._formatar_numero(delta)}",
        ]

        if raizes is None:
            linhas.append("Raizes reais: nao existem")
        else:
            x1, x2 = raizes
            linhas.extend(
                (
                    f"x1: {self._formatar_numero(x1)}",
                    f"x2: {self._formatar_numero(x2)}",
                )
            )

        xv, yv = vertice
        linhas.append(
            f"Vertice: ({self._formatar_numero(xv)}, "
            f"{self._formatar_numero(yv)})"
        )
        self.texto_var.set("\n".join(linhas))

    def limpar(self):
        self.texto_var.set("Preencha os dados e clique em Calcular.")
