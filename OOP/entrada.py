"""Entrada e validacao dos coeficientes da equacao."""


class Entrada:
    """Concentra a leitura e a validacao dos dados informados pelo usuario."""

    def ler_numero(self, mensagem):
        """Le um numero real, repetindo ate receber uma entrada valida."""
        while True:
            valor = input(mensagem).strip().replace(",", ".")
            try:
                return float(valor)
            except ValueError:
                print("Entrada invalida. Digite um numero, por exemplo: 2.5")

    def obter_coeficientes(self):
        """Retorna a, b e c, garantindo que a seja diferente de zero."""
        while True:
            a = self.ler_numero("Digite o coeficiente a: ")
            if a != 0:
                break
            print("O coeficiente a nao pode ser zero.")

        b = self.ler_numero("Digite o coeficiente b: ")
        c = self.ler_numero("Digite o coeficiente c: ")
        return a, b, c
