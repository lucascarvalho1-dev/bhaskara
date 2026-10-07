"""Modelo e calculos da equacao do segundo grau."""

import math


class EquacaoSegundoGrau:
    """Equação do 2o grau ax2 + bx + c = 0 e seus cálculos."""

    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("O coeficiente a nao pode ser zero.")
        self.a = a
        self.b = b
        self.c = c

    def calcular_delta(self):
        """Retorna o discriminante: b2 - 4ac."""
        return self.b ** 2 - 4 * self.a * self.c

    def calcular_raizes(self):
        """Retorna as raizes reais ou None se delta for negativo."""
        delta = self.calcular_delta()
        if delta < 0:
            return None

        raiz_delta = math.sqrt(delta)
        x1 = (-self.b + raiz_delta) / (2 * self.a)
        x2 = (-self.b - raiz_delta) / (2 * self.a)
        return x1, x2

    def calcular_vertice(self):
        """Retorna as coordenadas (xv, yv) do vertice."""
        delta = self.calcular_delta()
        xv = -self.b / (2 * self.a)
        yv = -delta / (4 * self.a)
        return xv, yv

    def calcular_pontos(self, inicio, fim, quantidade=400):
        """Retorna listas de x e y para desenhar a parabola."""
        if quantidade < 2:
            raise ValueError("A quantidade de pontos deve ser pelo menos 2.")

        passo = (fim - inicio) / (quantidade - 1)
        valores_x = [inicio + indice * passo for indice in range(quantidade)]
        valores_y = [self.valor_em(x) for x in valores_x]
        return valores_x, valores_y

    def valor_em(self, x):
        """Calcula f(x) para um ponto da parabola."""
        return self.a * x ** 2 + self.b * x + self.c
