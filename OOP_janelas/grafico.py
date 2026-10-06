"""Integracao do grafico Matplotlib com o Tkinter."""

import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class GraficoParabola(tk.Frame):
    """Painel que renderiza a parabola dentro da janela principal."""

    def __init__(self, master):
        super().__init__(master, bd=0, highlightthickness=0)
        self.figure = Figure(figsize=(7, 4.5), dpi=100)
        self.eixo = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        self._mostrar_mensagem_inicial()

    def _mostrar_mensagem_inicial(self):
        self.eixo.clear()
        self.figure.patch.set_facecolor("#ffffff")
        self.eixo.set_facecolor("#ffffff")
        self.eixo.text(
            0.5,
            0.5,
            "O grafico aparecera aqui",
            ha="center",
            va="center",
            transform=self.eixo.transAxes,
        )
        self.eixo.set_axis_off()
        self.canvas.draw_idle()

    def limpar(self):
        self._mostrar_mensagem_inicial()

    def exibir(self, equacao, pontos, vertice, raizes, tema, grade):
        valores_x, valores_y = pontos
        xv, yv = vertice
        fundo = "#202124" if tema == "Escuro" else "#ffffff"
        cor_texto = "#f1f3f4" if tema == "Escuro" else "#202124"
        cor_curva = "#8ab4f8" if tema == "Escuro" else "#1a73e8"

        self.eixo.clear()
        self.figure.patch.set_facecolor(fundo)
        self.eixo.set_facecolor(fundo)
        self.eixo.plot(
            valores_x,
            valores_y,
            color=cor_curva,
            linewidth=2,
            label="Parabola",
        )
        self.eixo.scatter([xv], [yv], color="#ea4335", zorder=3, label="Vertice")

        if raizes is not None:
            x1, x2 = raizes
            self.eixo.scatter(
                [x1, x2],
                [0, 0],
                color="#34a853",
                zorder=3,
                label="Raizes",
            )

        self.eixo.axhline(0, color=cor_texto, linewidth=0.8)
        self.eixo.axvline(0, color=cor_texto, linewidth=0.8)
        self.eixo.set_title("Grafico da parabola", color=cor_texto)
        self.eixo.set_xlabel("x", color=cor_texto)
        self.eixo.set_ylabel("f(x)", color=cor_texto)
        self.eixo.tick_params(colors=cor_texto)
        for espinha in self.eixo.spines.values():
            espinha.set_color(cor_texto)
        self.eixo.grid(grade, alpha=0.3)
        legenda = self.eixo.legend()
        for texto in legenda.get_texts():
            texto.set_color(cor_texto)
        legenda.get_frame().set_facecolor(fundo)
        legenda.get_frame().set_edgecolor(cor_texto)
        self.figure.tight_layout()
        self.canvas.draw_idle()
