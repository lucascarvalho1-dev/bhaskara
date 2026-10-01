"""Componentes visuais e validacao dos dados de entrada."""

import tkinter as tk
from tkinter import messagebox, ttk


class Entrada(ttk.LabelFrame):
    """Painel com os campos e opcoes usados pela calculadora."""

    def __init__(self, master):
        super().__init__(master, text="Dados da equacao", padding=12)
        self._criar_variaveis()
        self._criar_componentes()

    def _criar_variaveis(self):
        self.a_var = tk.StringVar(value="1")
        self.b_var = tk.StringVar(value="-5")
        self.c_var = tk.StringVar(value="6")
        self.inicio_x_var = tk.StringVar(value="-2")
        self.fim_x_var = tk.StringVar(value="7")
        self.quantidade_var = tk.StringVar(value="400")
        self.tema_var = tk.StringVar(value="Claro")
        self.grade_var = tk.BooleanVar(value=True)

    def _criar_componentes(self):
        campos = (
            ("Coeficiente a", self.a_var),
            ("Coeficiente b", self.b_var),
            ("Coeficiente c", self.c_var),
            ("Inicio do eixo x", self.inicio_x_var),
            ("Fim do eixo x", self.fim_x_var),
            ("Quantidade de pontos", self.quantidade_var),
        )

        for linha, (rotulo, variavel) in enumerate(campos):
            ttk.Label(self, text=rotulo).grid(row=linha, column=0, sticky="w", pady=3)
            ttk.Entry(self, textvariable=variavel, width=14).grid(
                row=linha, column=1, sticky="ew", padx=(12, 0), pady=3
            )

        ttk.Label(self, text="Tema do grafico").grid(row=6, column=0, sticky="w", pady=3)
        ttk.Combobox(
            self,
            textvariable=self.tema_var,
            values=("Claro", "Escuro"),
            state="readonly",
            width=12,
        ).grid(row=6, column=1, sticky="ew", padx=(12, 0), pady=3)

        ttk.Checkbutton(self, text="Exibir grade", variable=self.grade_var).grid(
            row=7, column=0, columnspan=2, sticky="w", pady=(8, 0)
        )
        self.columnconfigure(1, weight=1)

    def obter_configuracao(self):
        """Valida os campos e retorna os valores prontos para a aplicacao."""
        try:
            a = float(self.a_var.get().strip().replace(",", "."))
            b = float(self.b_var.get().strip().replace(",", "."))
            c = float(self.c_var.get().strip().replace(",", "."))
            inicio_x = float(self.inicio_x_var.get().strip().replace(",", "."))
            fim_x = float(self.fim_x_var.get().strip().replace(",", "."))
            quantidade = int(self.quantidade_var.get().strip())
        except ValueError:
            messagebox.showerror(
                "Entrada invalida",
                "Informe numeros validos nos coeficientes e no intervalo.",
                parent=self.winfo_toplevel(),
            )
            return None

        if a == 0:
            messagebox.showerror(
                "Equacao invalida",
                "O coeficiente a nao pode ser zero.",
                parent=self.winfo_toplevel(),
            )
            return None
        if inicio_x >= fim_x:
            messagebox.showerror(
                "Intervalo invalido",
                "O inicio do eixo x deve ser menor que o fim.",
                parent=self.winfo_toplevel(),
            )
            return None
        if quantidade < 2:
            messagebox.showerror(
                "Quantidade invalida",
                "A quantidade de pontos deve ser pelo menos 2.",
                parent=self.winfo_toplevel(),
            )
            return None

        return {
            "a": a,
            "b": b,
            "c": c,
            "inicio_x": inicio_x,
            "fim_x": fim_x,
            "quantidade": quantidade,
            "tema": self.tema_var.get(),
            "grade": self.grade_var.get(),
        }
