"""Ponto de entrada da calculadora de Bhaskara."""

from calculos import calcular_delta, calcular_pontos, calcular_raizes, calcular_vertice
from entrada import ler_coeficientes
from grafico import mostrar_grafico
from resultados import mostrar_resultados


def executar():
    """Le os dados, calcula os resultados e mostra a parabola."""
    a, b, c = ler_coeficientes()
    delta = calcular_delta(a, b, c)
    raizes = calcular_raizes(a, b, delta)
    vertice = calcular_vertice(a, b, delta)

    xv, _ = vertice
    if raizes is None:
        largura = max(5.0, abs(xv) + 5.0)
        inicio, fim = xv - largura, xv + largura
    else:
        x1, x2 = raizes
        margem = max(1.0, abs(x2 - x1) * 0.2)
        inicio, fim = min(x1, x2) - margem, max(x1, x2) + margem

    pontos = calcular_pontos(a, b, c, inicio, fim)
    mostrar_resultados(a, b, c, delta, raizes, vertice)
    mostrar_grafico(a, b, c, pontos, vertice, raizes)


if __name__ == "__main__":
    executar()
