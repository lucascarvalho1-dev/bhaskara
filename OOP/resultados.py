"""Formatacao e exibicao dos resultados no terminal."""


class Resultados:
    """Apresenta os dados calculados pela equacao."""

    @staticmethod
    def formatar_numero(valor):
        """Remove casas decimais desnecessarias da exibicao."""
        return f"{valor:.6g}"

    def exibir(self, equacao, delta, raizes, vertice):
        """Exibe a equacao, delta, raizes e vertice."""
        a = self.formatar_numero(equacao.a)
        b = self.formatar_numero(equacao.b)
        c = self.formatar_numero(equacao.c)

        print("\n--- Resultados ---")
        print(f"Equacao: {a}x^2 + {b}x + {c} = 0")
        print(f"Delta: {self.formatar_numero(delta)}")

        if raizes is None:
            print("A equacao nao possui raizes reais.")
        else:
            x1, x2 = raizes
            print(f"x1: {self.formatar_numero(x1)}")
            print(f"x2: {self.formatar_numero(x2)}")

        xv, yv = vertice
        print(f"Vertice: ({self.formatar_numero(xv)}, {self.formatar_numero(yv)})")
