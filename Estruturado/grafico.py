"""Visualizacao da parabola com Matplotlib."""


def mostrar_grafico(a, b, c, pontos, vertice, raizes=None):
    """Exibe a curva, o vertice e, quando existirem, as raizes reais."""
    import matplotlib.pyplot as plt

    valores_x, valores_y = pontos
    xv, yv = vertice

    plt.figure("Grafico da equacao do 2o grau")
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.plot(valores_x, valores_y, label=f"y = {a:g}x² + {b:g}x + {c:g}")
    plt.scatter([xv], [yv], color="red", zorder=3, label="Vertice")

    if raizes is not None:
        x1, x2 = raizes
        plt.scatter([x1, x2], [0, 0], color="green", zorder=3, label="Raizes")

    plt.title("Parabola da equacao do 2o grau")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()
