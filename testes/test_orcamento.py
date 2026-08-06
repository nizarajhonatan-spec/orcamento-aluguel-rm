import csv
import tempfile
import unittest
from pathlib import Path

from modelos import Apartamento, Casa, Estudio
from servicos.gerador_csv import gerar_csv
from servicos.orcamento import Orcamento


class TesteImoveis(unittest.TestCase):
    def test_apartamento_basico_com_desconto(self):
        self.assertEqual(Apartamento(possui_criancas=False).calcular_aluguel(), 665.0)

    def test_apartamento_completo_com_desconto(self):
        self.assertEqual(Apartamento(2, True, False).calcular_aluguel(), 1140.0)

    def test_casa_com_dois_quartos_e_garagem(self):
        self.assertEqual(Casa(2, True).calcular_aluguel(), 1450.0)

    def test_estudio_com_quatro_vagas(self):
        self.assertEqual(Estudio(4).calcular_aluguel(), 1570.0)

    def test_estudio_rejeita_uma_vaga(self):
        with self.assertRaises(ValueError):
            Estudio(1)

    def test_contrato_em_cinco_parcelas(self):
        orcamento = Orcamento(Casa(), 5)
        self.assertEqual(orcamento.parcela_contrato, 400.0)
        self.assertEqual(orcamento.gerar_mensalidades()[0]["total"], 1300.0)
        self.assertEqual(orcamento.gerar_mensalidades()[5]["total"], 900.0)
        self.assertEqual(orcamento.total_anual, 12800.0)

    def test_todas_as_opcoes_de_parcelamento(self):
        for parcelas in range(1, 6):
            with self.subTest(parcelas=parcelas):
                orcamento = Orcamento(Apartamento(), parcelas)
                mensalidades = orcamento.gerar_mensalidades()
                parcelas_geradas = [item["contrato"] for item in mensalidades]
                self.assertEqual(sum(parcelas_geradas), 2000.0)
                self.assertEqual(sum(valor > 0 for valor in parcelas_geradas), parcelas)
                self.assertEqual(orcamento.total_anual, 10400.0)

    def test_arredondamento_contrato_em_tres_parcelas(self):
        mensalidades = Orcamento(Apartamento(), 3).gerar_mensalidades()
        self.assertEqual(
            [item["contrato"] for item in mensalidades[:3]],
            [666.67, 666.67, 666.66],
        )

    def test_orcamento_tem_doze_meses(self):
        self.assertEqual(len(Orcamento(Estudio(), 3).gerar_mensalidades()), 12)

    def test_csv_tem_cabecalho_e_doze_linhas(self):
        with tempfile.TemporaryDirectory() as pasta:
            arquivo = gerar_csv(Orcamento(Apartamento(), 2), Path(pasta) / "teste.csv")
            with arquivo.open(encoding="utf-8-sig") as entrada:
                linhas = list(csv.reader(entrada, delimiter=";"))
            self.assertEqual(len(linhas), 13)
            self.assertEqual(linhas[0][0], "Mês")


if __name__ == "__main__":
    unittest.main()
