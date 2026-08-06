"""Regra de negócio para compor o orçamento anual."""

from dataclasses import dataclass
from modelos import Imovel


@dataclass(frozen=True)
class Orcamento:
    imovel: Imovel
    parcelas_contrato: int = 1
    VALOR_CONTRATO = 2000.0

    def __post_init__(self) -> None:
        if not 1 <= self.parcelas_contrato <= 5:
            raise ValueError("O contrato deve ser dividido entre 1 e 5 parcelas.")

    @property
    def aluguel_mensal(self) -> float:
        return self.imovel.calcular_aluguel()

    @property
    def parcela_contrato(self) -> float:
        return round(self.VALOR_CONTRATO / self.parcelas_contrato, 2)

    @property
    def primeira_mensalidade(self) -> float:
        return round(self.aluguel_mensal + self.parcela_contrato, 2)

    def gerar_mensalidades(self) -> list[dict[str, float | int]]:
        mensalidades = []
        acumulado_contrato = 0.0
        for mes in range(1, 13):
            contrato = self.parcela_contrato if mes <= self.parcelas_contrato else 0.0
            # Corrige eventual centavo de arredondamento na última parcela.
            if mes == self.parcelas_contrato:
                contrato = round(self.VALOR_CONTRATO - acumulado_contrato, 2)
            acumulado_contrato += contrato
            total = round(self.aluguel_mensal + contrato, 2)
            mensalidades.append({
                "mes": mes,
                "aluguel": self.aluguel_mensal,
                "contrato": contrato,
                "total": total,
            })
        return mensalidades

    @property
    def total_anual(self) -> float:
        return round(sum(item["total"] for item in self.gerar_mensalidades()), 2)
