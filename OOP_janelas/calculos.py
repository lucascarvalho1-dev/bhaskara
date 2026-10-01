"""Classe de dominio com os calculos da equacao do segundo grau."""

import math


class EquacaoSegundoGrau:
    """Representa uma equacao ax^2 + bx + c = 0 sem depender da interface."""

    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("O coeficiente a nao pode ser zero.")
        self.a = a
        self.b = b
        self.c = c

    def calcular_delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def calcular_raizes(self):
        delta = self.calcular_delta()
        if delta < 0:
            return None

        raiz_delta = math.sqrt(delta)
        return (
            (-self.b + raiz_delta) / (2 * self.a),
            (-self.b - raiz_delta) / (2 * self.a),
        )

    def calcular_vertice(self):
        delta = self.calcular_delta()
        return -self.b / (2 * self.a), -delta / (4 * self.a)

    def calcular_pontos(self, inicio_x, fim_x, quantidade):
        if quantidade < 2:
            raise ValueError("A quantidade de pontos deve ser pelo menos 2.")

        passo = (fim_x - inicio_x) / (quantidade - 1)
        valores_x = [inicio_x + indice * passo for indice in range(quantidade)]
        valores_y = [self.valor_em(x) for x in valores_x]
        return valores_x, valores_y

    def valor_em(self, x):
        return self.a * x ** 2 + self.b * x + self.c
