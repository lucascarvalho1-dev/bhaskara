"""Exibicao dos resultados da equacao."""


def formatar_numero(valor):
    """Formata numeros sem casas decimais desnecessarias."""
    return f"{valor:.6g}"


def mostrar_resultados(a, b, c, delta, raizes, vertice):
    """Mostra delta, raizes e vertice no terminal."""
    print("\n--- Resultados ---")
    print(f"Equacao: {formatar_numero(a)}x^2 + {formatar_numero(b)}x + {formatar_numero(c)} = 0")
    print(f"Delta: {formatar_numero(delta)}")

    if raizes is None:
        print("A equacao nao possui raizes reais.")
    else:
        x1, x2 = raizes
        print(f"x1: {formatar_numero(x1)}")
        print(f"x2: {formatar_numero(x2)}")

    xv, yv = vertice
    print(f"Vertice: ({formatar_numero(xv)}, {formatar_numero(yv)})")
