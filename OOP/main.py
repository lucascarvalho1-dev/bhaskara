"""Aplicacao de terminal para calculo de Bhaskara."""

from calculos import EquacaoSegundoGrau
from entrada import Entrada
from grafico import GraficoParabola
from resultados import Resultados


class AplicacaoBhaskara:
    """Orquestra a entrada, os calculos, a saida e o grafico."""

    def __init__(self):
        self.entrada = Entrada()
        self.resultados = Resultados()
        self.grafico = GraficoParabola()

    def executar(self):
        """Executa o fluxo completo da aplicacao."""
        a, b, c = self.entrada.obter_coeficientes()
        equacao = EquacaoSegundoGrau(a, b, c)
        delta = equacao.calcular_delta()
        raizes = equacao.calcular_raizes()
        vertice = equacao.calcular_vertice()
        pontos = equacao.calcular_pontos(*self._intervalo_grafico(equacao, raizes))

        self.resultados.exibir(equacao, delta, raizes, vertice)
        self.grafico.exibir(equacao, pontos, vertice, raizes)

    def _intervalo_grafico(self, equacao, raizes):
        """Calcula uma janela adequada de x para o grafico."""
        xv, _ = equacao.calcular_vertice()
        if raizes is None:
            largura = max(5.0, abs(xv) + 5.0)
            return xv - largura, xv + largura

        x1, x2 = raizes
        margem = max(1.0, abs(x2 - x1) * 0.2)
        return min(x1, x2) - margem, max(x1, x2) + margem


if __name__ == "__main__":
    AplicacaoBhaskara().executar()
