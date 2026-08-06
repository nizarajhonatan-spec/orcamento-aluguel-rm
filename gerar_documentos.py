"""Gera o PDF teórico com fluxograma e conteúdo acadêmico."""

from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageBreak, PageTemplate, Paragraph,
    Spacer, Table, TableStyle
)

BASE = Path(__file__).resolve().parent
SAIDA = BASE / "documentos" / "parte_teorica_orcamento_rm.pdf"


def cabecalho_rodape(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#d7e1ea"))
    canvas.line(2 * cm, 1.55 * cm, 19 * cm, 1.55 * cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#607487"))
    canvas.drawString(2 * cm, 1.05 * cm, "Jhonatan Franco | Engenharia da Computação")
    canvas.drawRightString(19 * cm, 1.05 * cm, f"Página {doc.page}")
    canvas.restoreState()


def caixa(texto, cor="#eaf2f8"):
    return Table([[Paragraph(texto, estilos["Corpo"])]], colWidths=[16.4 * cm], style=[
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor(cor)),
        ("BOX", (0, 0), (-1, -1), 0.7, colors.HexColor("#9db4c6")),
        ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ])


def fluxograma():
    itens = [
        ("INÍCIO", "#16324f", "#ffffff"),
        ("Ler tipo, características e parcelas", "#eaf2f8", "#16324f"),
        ("Validar os dados", "#eaf2f8", "#16324f"),
        ("Selecionar a classe do imóvel", "#d9edf7", "#16324f"),
        ("Calcular aluguel e adicionais", "#d9edf7", "#16324f"),
        ("Apartamento sem crianças? Aplicar 5%", "#fff3cd", "#5f4b00"),
        ("Somar parcela do contrato", "#d9edf7", "#16324f"),
        ("Exibir resultado e permitir CSV", "#eaf2f8", "#16324f"),
        ("FIM", "#16324f", "#ffffff"),
    ]
    linhas = []
    for i, (texto, fundo, fonte) in enumerate(itens):
        linhas.append([Paragraph(f"<b>{texto}</b>", ParagraphStyle("fc", parent=estilos["Corpo"], alignment=TA_CENTER, textColor=colors.HexColor(fonte)))])
        if i < len(itens) - 1:
            linhas.append([Paragraph("↓", ParagraphStyle("seta", alignment=TA_CENTER, fontSize=15, leading=16, textColor=colors.HexColor("#607487")))])
    tabela = Table(linhas, colWidths=[12.5 * cm])
    comandos = [("ALIGN", (0, 0), (-1, -1), "CENTER")]
    for i, (_, fundo, _) in enumerate(itens):
        linha = i * 2
        comandos.extend([
            ("BACKGROUND", (0, linha), (0, linha), colors.HexColor(fundo)),
            ("BOX", (0, linha), (0, linha), 0.8, colors.HexColor("#6f8ba1")),
            ("TOPPADDING", (0, linha), (0, linha), 7),
            ("BOTTOMPADDING", (0, linha), (0, linha), 7),
        ])
    tabela.setStyle(TableStyle(comandos))
    return tabela


estilos = getSampleStyleSheet()
estilos.add(ParagraphStyle("TituloCapa", parent=estilos["Title"], fontName="Helvetica-Bold", fontSize=25, leading=30, textColor=colors.HexColor("#16324f"), alignment=TA_CENTER, spaceAfter=18))
estilos.add(ParagraphStyle("Subtitulo", parent=estilos["Normal"], fontSize=13, leading=18, textColor=colors.HexColor("#607487"), alignment=TA_CENTER))
estilos.add(ParagraphStyle("H1x", parent=estilos["Heading1"], fontSize=17, leading=21, textColor=colors.HexColor("#16324f"), spaceBefore=8, spaceAfter=10))
estilos.add(ParagraphStyle("H2x", parent=estilos["Heading2"], fontSize=12.5, leading=16, textColor=colors.HexColor("#24557a"), spaceBefore=9, spaceAfter=6))
estilos.add(ParagraphStyle("Corpo", parent=estilos["BodyText"], fontSize=9.5, leading=14, textColor=colors.HexColor("#263746"), spaceAfter=7))
estilos.add(ParagraphStyle("Codigo", parent=estilos["Code"], fontName="Courier", fontSize=8.2, leading=11, leftIndent=10, backColor=colors.HexColor("#f3f6f8"), borderPadding=7, spaceAfter=8))


def gerar():
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(str(SAIDA), pagesize=A4, rightMargin=2.2*cm, leftMargin=2.2*cm, topMargin=1.8*cm, bottomMargin=2*cm, title="Parte Teórica - Orçamento R.M.", author="Jhonatan Franco")
    doc.addPageTemplates(PageTemplate(id="padrao", frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="conteudo")], onPage=cabecalho_rodape))
    story = [Spacer(1, 3.5*cm), Paragraph("GERADOR DE ORÇAMENTO<br/>DE ALUGUEL R.M.", estilos["TituloCapa"]), Paragraph("Parte Teórica - Fluxograma, lógica e pensamento algorítmico", estilos["Subtitulo"]), Spacer(1, 2.3*cm), caixa("<b>Disciplina:</b> Algorithmic Thinking & Introduction to Object-Oriented Programming<br/><b>Aluno:</b> Jhonatan Franco<br/><b>Curso:</b> Engenharia da Computação<br/><b>Data:</b> Agosto de 2026"), Spacer(1, 4.5*cm), Paragraph("Aplicação desenvolvida em Python com orientação a objetos, interface gráfica e exportação CSV.", estilos["Subtitulo"]), PageBreak()]

    story += [Paragraph("1. Objetivo e requisitos", estilos["H1x"]), Paragraph("O projeto automatiza a geração de orçamentos da imobiliária R.M. O usuário informa o tipo de imóvel, suas características e a quantidade de parcelas do contrato. O sistema valida os dados, calcula o aluguel, apresenta o resultado e gera um arquivo CSV com doze mensalidades.", estilos["Corpo"])]
    dados = [["Imóvel/regra", "Valor aplicado"], ["Apartamento - 1 quarto", "R$ 700,00"], ["Apartamento - 2 quartos", "+ R$ 200,00"], ["Casa - 1 quarto", "R$ 900,00"], ["Casa - 2 quartos", "+ R$ 250,00"], ["Estúdio", "R$ 1.200,00"], ["Garagem para casa/apartamento", "+ R$ 300,00"], ["Estúdio - 2 vagas", "+ R$ 250,00"], ["Vaga adicional do estúdio", "+ R$ 60,00"], ["Apartamento sem crianças", "5% de desconto"], ["Contrato imobiliário", "R$ 2.000,00 em 1 a 5 vezes"]]
    t = Table(dados, colWidths=[10.2*cm, 6.2*cm], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#16324f")), ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"), ("GRID", (0,0), (-1,-1), .4, colors.HexColor("#b7c7d3")), ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f3f6f8")]), ("FONTSIZE", (0,0), (-1,-1), 8.5), ("TOPPADDING", (0,0), (-1,-1), 5), ("BOTTOMPADDING", (0,0), (-1,-1), 5)]))
    story += [t, Spacer(1, 8), Paragraph("Delimitação do escopo: o texto introdutório cita metragem como exemplo de dado que uma imobiliária pode cadastrar, mas não fornece preço por metro quadrado nem exige área no cálculo. Portanto, o orçamento usa somente as regras objetivas da tabela acima.", estilos["Corpo"]), Paragraph("Decisão adotada: a parcela do contrato é somada aos primeiros meses. Se o cliente escolher cinco parcelas, cada um dos cinco primeiros meses recebe R$ 400,00; os demais contêm apenas o aluguel. Essa interpretação torna explícita a cobrança e preserva o total exato de R$ 2.000,00.", estilos["Corpo"]), Paragraph("2. Pensamento algorítmico", estilos["H1x"]), Paragraph("O problema foi decomposto em entrada, validação, processamento e saída. A abstração separa os dados relevantes de cada imóvel. O reconhecimento de padrões identifica elementos comuns, como aluguel mensal e contrato. A lógica condicional aplica apenas as regras correspondentes às escolhas do cliente, enquanto a repetição gera os doze meses.", estilos["Corpo"]), caixa("<b>Entrada:</b> tipo, quartos, garagem, crianças, vagas e parcelas.<br/><b>Processamento:</b> validar, calcular adicionais/desconto e distribuir o contrato.<br/><b>Saída:</b> aluguel mensal, primeira mensalidade, total anual e CSV."), PageBreak(), Paragraph("3. Fluxograma", estilos["H1x"]), Paragraph("O fluxo abaixo representa o caminho principal da aplicação. Em caso de dado inválido, o sistema informa o erro e solicita a correção antes de calcular.", estilos["Corpo"]), Spacer(1, 6), fluxograma(), PageBreak()]

    pseudo = """INÍCIO<br/>LER tipo do imóvel e características<br/>LER quantidade de parcelas do contrato<br/>SE parcelas &lt; 1 OU parcelas &gt; 5: informar erro<br/>CRIAR objeto Apartamento, Casa ou Estudio<br/>valor_aluguel ← objeto.calcular_aluguel()<br/>parcela_contrato ← 2000 / quantidade_parcelas<br/>PARA mês de 1 ATÉ 12:<br/>    SE mês &lt;= quantidade_parcelas:<br/>        total ← valor_aluguel + parcela_contrato<br/>    SENÃO:<br/>        total ← valor_aluguel<br/>    REGISTRAR mês, aluguel, contrato e total<br/>EXIBIR orçamento<br/>SE usuário solicitar: GERAR arquivo CSV<br/>FIM"""
    matriz = [["Teste", "Resultado esperado"], ["Apartamento básico sem crianças", "R$ 665,00"], ["Apartamento completo sem crianças", "R$ 1.140,00"], ["Casa: 2 quartos + garagem", "R$ 1.450,00"], ["Estúdio com 4 vagas", "R$ 1.570,00"], ["Contrato em 5 parcelas", "5 x R$ 400,00"], ["Contrato em 3 parcelas", "666,67 + 666,67 + 666,66"], ["Opções de 1 a 5 parcelas", "Total exato de R$ 2.000,00"], ["Exportação anual", "12 mensalidades"], ["Entradas inválidas", "Exceção controlada"]]
    mt = Table(matriz, colWidths=[9.5*cm, 6.9*cm], repeatRows=1)
    mt.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), colors.HexColor("#16324f")), ("TEXTCOLOR", (0,0), (-1,0), colors.white), ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"), ("GRID", (0,0), (-1,-1), .4, colors.HexColor("#b7c7d3")), ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#f3f6f8")]), ("FONTSIZE", (0,0), (-1,-1), 8.5), ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6)]))
    story += [Paragraph("4. Pseudocódigo", estilos["H1x"]), Paragraph(pseudo, estilos["Codigo"]), Paragraph("5. Orientação a objetos", estilos["H1x"]), Paragraph("A classe abstrata <b>Imovel</b> define o método calcular_aluguel(). As classes <b>Apartamento</b>, <b>Casa</b> e <b>Estudio</b> herdam essa obrigação e fornecem implementações próprias. Isso representa herança e polimorfismo: o serviço Orcamento recebe qualquer Imovel e solicita o mesmo método, sem precisar conhecer todos os detalhes internos.", estilos["Corpo"]), Paragraph("O encapsulamento aparece na separação das responsabilidades. As classes dos imóveis cuidam dos valores de locação; Orcamento distribui o contrato e monta os meses; gerar_csv apenas grava o arquivo; e a interface coleta entradas e apresenta saídas.", estilos["Corpo"]), Paragraph("6. Fórmulas e exemplo", estilos["H1x"]), Paragraph("Para um apartamento de dois quartos, com garagem e cliente sem crianças:", estilos["Corpo"]), caixa("Valor antes do desconto = 700 + 200 + 300 = R$ 1.200,00<br/>Desconto = 1.200 x 5% = R$ 60,00<br/><b>Aluguel mensal = 1.200 - 60 = R$ 1.140,00</b><br/>Contrato em 5 vezes = 2.000 / 5 = R$ 400,00<br/><b>Primeira mensalidade = 1.140 + 400 = R$ 1.540,00</b><br/><b>Total anual = (12 x 1.140) + 2.000 = R$ 15.680,00</b>"), Paragraph("7. Validação e testes", estilos["H1x"]), Paragraph("Foram aprovados dez testes automatizados para valores básicos e adicionais, desconto, estúdio com vagas, rejeição de uma vaga, todas as opções de uma a cinco parcelas, ajuste de centavos, total anual e geração das treze linhas do arquivo CSV (cabeçalho mais doze meses). As validações impedem quartos fora das opções, uma vaga isolada no estúdio e contrato fora do intervalo permitido. A interface também descarta o resultado anterior quando o usuário altera uma escolha, evitando exportar um CSV desatualizado.", estilos["Corpo"]), Paragraph("8. Conclusão", estilos["H1x"]), Paragraph("A solução atende aos requisitos do enunciado e demonstra pensamento algorítmico por meio de decomposição, condições, repetição e validação. A arquitetura orientada a objetos reduz duplicação, facilita testes e permite incluir novos tipos de imóvel futuramente.", estilos["Corpo"]), PageBreak(), Paragraph("9. Matriz de testes", estilos["H1x"]), Paragraph("A tabela resume os principais cenários conferidos automaticamente antes da entrega.", estilos["Corpo"]), mt, Spacer(1, 14), Paragraph("10. Referências", estilos["H1x"]), Paragraph("PYTHON SOFTWARE FOUNDATION. <i>Python Documentation</i>. Disponível em: https://docs.python.org/3/. Acesso em: 5 ago. 2026.<br/><br/>PYTHON SOFTWARE FOUNDATION. <i>tkinter - Python interface to Tcl/Tk</i>. Disponível em: https://docs.python.org/3/library/tkinter.html. Acesso em: 5 ago. 2026.<br/><br/>PYTHON SOFTWARE FOUNDATION. <i>csv - CSV File Reading and Writing</i>. Disponível em: https://docs.python.org/3/library/csv.html. Acesso em: 5 ago. 2026.", estilos["Corpo"])]
    doc.build(story)
    print(SAIDA)


if __name__ == "__main__":
    gerar()
