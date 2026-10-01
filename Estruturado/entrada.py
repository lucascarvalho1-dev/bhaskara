"""Leitura e validacao dos coeficientes da equacao."""


def ler_numero(mensagem):
    """Le um numero real do usuario, repetindo ate receber um valor valido."""
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Entrada invalida. Digite um numero, por exemplo: 2.5")


def ler_coeficientes():
    """Solicita a, b e c, garantindo que a seja diferente de zero."""
    while True:
        a = ler_numero("Digite o coeficiente a: ")
        if a != 0:
            break
        print("O coeficiente a nao pode ser zero em uma equacao do 2o grau.")

    b = ler_numero("Digite o coeficiente b: ")
    c = ler_numero("Digite o coeficiente c: ")
    return a, b, c
