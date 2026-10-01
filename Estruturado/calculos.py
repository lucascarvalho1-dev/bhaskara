"""Funcoes matematicas para a equacao do segundo grau."""

import math


def calcular_delta(a, b, c):
    """Calcula o discriminante delta = b**2 - 4*a*c."""
    return b ** 2 - 4 * a * c


def calcular_raizes(a, b, delta):
    """Retorna as raizes reais ou None quando delta e negativo."""
    if delta < 0:
        return None

    raiz_delta = math.sqrt(delta)
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    return x1, x2


def calcular_vertice(a, b, delta):
    """Calcula as coordenadas do vertice da parabola."""
    xv = -b / (2 * a)
    yv = -delta / (4 * a)
    return xv, yv


def calcular_pontos(a, b, c, inicio, fim, quantidade=400):
    """Gera pontos (x, y) da parabola no intervalo informado."""
    if quantidade < 2:
        raise ValueError("A quantidade de pontos deve ser pelo menos 2.")

    passo = (fim - inicio) / (quantidade - 1)
    valores_x = [inicio + indice * passo for indice in range(quantidade)]
    valores_y = [a * x ** 2 + b * x + c for x in valores_x]
    return valores_x, valores_y
