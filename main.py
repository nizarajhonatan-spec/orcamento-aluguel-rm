"""Interface gráfica do Gerador de Orçamento de Aluguel R.M."""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from modelos import Apartamento, Casa, Estudio
from servicos.gerador_csv import gerar_csv
from servicos.orcamento import Orcamento


def moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class AplicacaoRM(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("R.M. | Orçamento de Aluguel")
        # A altura anterior (610 px) cortava o botão de exportação no Windows.
        self.geometry("780x810")
        self.minsize(780, 810)
        self.resizable(False, True)
        self.configure(bg="#eef3f8")
        self.orcamento_atual: Orcamento | None = None

        self.tipo = tk.StringVar(value="Apartamento")
        self.quartos = tk.IntVar(value=1)
        self.garagem = tk.BooleanVar(value=False)
        self.possui_criancas = tk.BooleanVar(value=True)
        self.vagas = tk.IntVar(value=0)
        self.parcelas = tk.IntVar(value=5)
        self._montar_interface()
        self._atualizar_campos()
        self._observar_alteracoes()

    def _montar_interface(self) -> None:
        estilo = ttk.Style(self)
        estilo.theme_use("clam")
        estilo.configure("Titulo.TLabel", font=("Arial", 21, "bold"), foreground="#16324f", background="#eef3f8")
        estilo.configure("Sub.TLabel", font=("Arial", 10), foreground="#4f6475", background="#eef3f8")

        ttk.Label(self, text="R.M. Imobiliária", style="Titulo.TLabel").pack(pady=(22, 2))
        ttk.Label(self, text="Gerador de orçamento anual de locação", style="Sub.TLabel").pack(pady=(0, 15))

        referencias = ttk.LabelFrame(self, text=" Valores de referência do enunciado ", padding=12)
        referencias.pack(fill="x", padx=35, pady=(0, 12))
        ttk.Label(
            referencias,
            text=(
                "Apartamento (1 quarto): R$ 700,00     |     "
                "Casa (1 quarto): R$ 900,00     |     Estúdio: R$ 1.200,00\n"
                "2º quarto: +R$ 200,00 (apto.) / +R$ 250,00 (casa)     |     "
                "Garagem: +R$ 300,00     |     Apto. sem crianças: -5%\n"
                "Estúdio: 2 vagas +R$ 250,00; cada vaga adicional +R$ 60,00"
            ),
            justify="center",
        ).pack()

        formulario = ttk.LabelFrame(self, text=" Dados do imóvel ", padding=18)
        formulario.pack(fill="x", padx=35)
        ttk.Label(formulario, text="Tipo de imóvel:").grid(row=0, column=0, sticky="w", pady=7)
        combo_tipo = ttk.Combobox(formulario, textvariable=self.tipo, values=["Apartamento", "Casa", "Estúdio"], state="readonly", width=24)
        combo_tipo.grid(row=0, column=1, sticky="w", padx=12)
        combo_tipo.bind("<<ComboboxSelected>>", lambda _e: self._atualizar_campos())

        ttk.Label(formulario, text="Quantidade de quartos:").grid(row=1, column=0, sticky="w", pady=7)
        self.combo_quartos = ttk.Combobox(formulario, textvariable=self.quartos, values=[1, 2], state="readonly", width=10)
        self.combo_quartos.grid(row=1, column=1, sticky="w", padx=12)

        self.check_garagem = ttk.Checkbutton(formulario, text="Incluir garagem (+ R$ 300,00)", variable=self.garagem)
        self.check_garagem.grid(row=2, column=1, sticky="w", padx=12, pady=7)
        self.check_criancas = ttk.Checkbutton(formulario, text="Cliente possui crianças", variable=self.possui_criancas)
        self.check_criancas.grid(row=3, column=1, sticky="w", padx=12, pady=7)

        ttk.Label(formulario, text="Vagas do estúdio:").grid(row=4, column=0, sticky="w", pady=7)
        self.combo_vagas = ttk.Combobox(formulario, textvariable=self.vagas, values=[0, 2, 3, 4, 5], state="readonly", width=10)
        self.combo_vagas.grid(row=4, column=1, sticky="w", padx=12)

        ttk.Label(formulario, text="Parcelas do contrato (R$ 2.000):").grid(row=5, column=0, sticky="w", pady=7)
        self.combo_parcelas = ttk.Combobox(formulario, textvariable=self.parcelas, values=[1, 2, 3, 4, 5], state="readonly", width=10)
        self.combo_parcelas.grid(row=5, column=1, sticky="w", padx=12)

        ttk.Button(self, text="Calcular orçamento", command=self.calcular).pack(pady=14)
        self.resultado = tk.Label(self, text="Preencha os dados e clique em calcular.", bg="#ffffff", fg="#16324f", font=("Arial", 11), justify="left", anchor="w", padx=18, pady=12, relief="solid", bd=1, width=72, height=9)
        self.resultado.pack(padx=35)
        self.botao_csv = ttk.Button(self, text="Exportar 12 mensalidades em CSV", command=self.exportar, state="disabled")
        self.botao_csv.pack(pady=16)

    def _atualizar_campos(self) -> None:
        tipo = self.tipo.get()
        comum = "readonly" if tipo in ("Apartamento", "Casa") else "disabled"
        self.combo_quartos.configure(state=comum)
        self.check_garagem.configure(state="normal" if tipo in ("Apartamento", "Casa") else "disabled")
        self.check_criancas.configure(state="normal" if tipo == "Apartamento" else "disabled")
        self.combo_vagas.configure(state="readonly" if tipo == "Estúdio" else "disabled")

    def _observar_alteracoes(self) -> None:
        """Evita exportar ou exibir um cálculo feito com dados anteriores."""
        for variavel in (
            self.tipo,
            self.quartos,
            self.garagem,
            self.possui_criancas,
            self.vagas,
            self.parcelas,
        ):
            variavel.trace_add("write", self._invalidar_orcamento)

    def _invalidar_orcamento(self, *_args) -> None:
        self.orcamento_atual = None
        self.resultado.configure(
            text="Dados alterados. Clique em calcular para gerar um novo orçamento."
        )
        self.botao_csv.configure(state="disabled")

    def _criar_imovel(self):
        if self.tipo.get() == "Apartamento":
            return Apartamento(self.quartos.get(), self.garagem.get(), self.possui_criancas.get())
        if self.tipo.get() == "Casa":
            return Casa(self.quartos.get(), self.garagem.get())
        return Estudio(self.vagas.get())

    def calcular(self) -> None:
        try:
            self.orcamento_atual = Orcamento(self._criar_imovel(), self.parcelas.get())
            o = self.orcamento_atual
            base, adicionais, desconto = self._detalhar_calculo()
            meses_contrato = (
                "mês 1" if self.parcelas.get() == 1
                else f"meses 1 a {self.parcelas.get()}"
            )
            self.resultado.configure(text=(
                "BASE CÁLCULO\n"
                f"Valor-base da categoria: {moeda(base)}\n"
                f"Acréscimos: {adicionais}\n"
                f"Desconto: {desconto}\n"
                f"Aluguel mensal final: {moeda(o.aluguel_mensal)}\n"
                f"Contrato imobiliário: R$ 2.000,00 em {self.parcelas.get()} parcela(s)\n"
                f"Parcela do contrato: {moeda(o.parcela_contrato)} ({meses_contrato})\n"
                f"Primeira mensalidade (aluguel + parcela): {moeda(o.primeira_mensalidade)}\n"
                f"Total previsto em 12 meses: {moeda(o.total_anual)}"
            ))
            self.botao_csv.configure(state="normal")
        except ValueError as erro:
            messagebox.showerror("Dados inválidos", str(erro))

    def _detalhar_calculo(self) -> tuple[float, str, str]:
        """Explica os valores usados no cálculo conforme o enunciado."""
        tipo = self.tipo.get()
        acrescimos: list[str] = []

        if tipo == "Apartamento":
            base = 700.0
            if self.quartos.get() == 2:
                acrescimos.append("2º quarto +R$ 200,00")
            if self.garagem.get():
                acrescimos.append("garagem +R$ 300,00")
            desconto = "5% sobre o aluguel" if not self.possui_criancas.get() else "não aplicado"
        elif tipo == "Casa":
            base = 900.0
            if self.quartos.get() == 2:
                acrescimos.append("2º quarto +R$ 250,00")
            if self.garagem.get():
                acrescimos.append("garagem +R$ 300,00")
            desconto = "não se aplica a casas"
        else:
            base = 1200.0
            if self.vagas.get() >= 2:
                acrescimos.append("2 vagas +R$ 250,00")
                extras = self.vagas.get() - 2
                if extras:
                    acrescimos.append(f"{extras} vaga(s) adicional(is) +{moeda(extras * 60.0)}")
            desconto = "não se aplica a estúdios"

        return base, "; ".join(acrescimos) if acrescimos else "nenhum", desconto

    def exportar(self) -> None:
        if self.orcamento_atual is None:
            return
        destino = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")], initialfile="orcamento_rm_12_meses.csv")
        if destino:
            try:
                gerar_csv(self.orcamento_atual, destino)
                messagebox.showinfo(
                    "Arquivo gerado",
                    "As 12 mensalidades foram exportadas com sucesso.",
                )
            except (OSError, PermissionError) as erro:
                messagebox.showerror(
                    "Erro ao gerar CSV",
                    f"Não foi possível salvar o arquivo.\n\nDetalhes: {erro}",
                )


if __name__ == "__main__":
    AplicacaoRM().mainloop()
