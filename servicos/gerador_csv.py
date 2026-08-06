"""Exportação das 12 mensalidades para arquivo CSV."""

import csv
from pathlib import Path
from .orcamento import Orcamento


def gerar_csv(orcamento: Orcamento, destino: str | Path) -> Path:
    caminho = Path(destino)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", newline="", encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerow(["Mês", "Aluguel (R$)", "Contrato (R$)", "Total (R$)"])
        for item in orcamento.gerar_mensalidades():
            escritor.writerow([
                item["mes"],
                f'{item["aluguel"]:.2f}'.replace(".", ","),
                f'{item["contrato"]:.2f}'.replace(".", ","),
                f'{item["total"]:.2f}'.replace(".", ","),
            ])
    return caminho
