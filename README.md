# Gerador de Orçamento de Aluguel - R.M.

Projeto acadêmico da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**. A aplicação calcula o aluguel de apartamentos, casas e estúdios, acrescenta o contrato imobiliário parcelado e exporta um planejamento de 12 mensalidades em CSV.

## Funcionalidades

- cálculo conforme o tipo e as características do imóvel;
- desconto de 5% em apartamentos para clientes sem crianças;
- contrato de R$ 2.000,00 parcelado de 1 a 5 vezes;
- interface gráfica feita com Tkinter;
- exportação das 12 mensalidades para CSV;
- validação dos dados e testes automatizados;
- invalidação automática do resultado quando qualquer escolha é alterada;
- uso de herança, abstração, encapsulamento e polimorfismo.

## Valores utilizados no cálculo

| Categoria ou regra | Valor |
|---|---:|
| Apartamento com 1 quarto | R$ 700,00 |
| Segundo quarto do apartamento | + R$ 200,00 |
| Casa com 1 quarto | R$ 900,00 |
| Segundo quarto da casa | + R$ 250,00 |
| Estúdio | R$ 1.200,00 |
| Garagem de casa ou apartamento | + R$ 300,00 |
| Duas vagas do estúdio | + R$ 250,00 |
| Cada vaga adicional do estúdio | + R$ 60,00 |
| Apartamento para pessoa sem crianças | 5% de desconto |
| Contrato imobiliário | R$ 2.000,00 em até 5 vezes |

O enunciado cita metragem somente na apresentação geral de uma aplicação
imobiliária. Ele não fornece preço por metro quadrado nem exige que a área seja
usada no orçamento. Por isso, a aplicação calcula apenas as regras objetivas
listadas acima.

## Como executar

1. Instale o Python 3.10 ou superior.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python main.py
```

No Windows, se `python` não funcionar, tente `py main.py`.

## Como executar os testes

```bash
python -m unittest discover -s testes -v
```

## Organização

```text
modelos/              Classes Imovel, Apartamento, Casa e Estudio
servicos/             Cálculo do orçamento e geração do CSV
testes/               Testes automatizados
documentos/           Parte teórica e roteiro de apresentação
main.py               Interface gráfica e ponto de entrada
```

## Decisão sobre o contrato

O contrato imobiliário é cobrado nos primeiros meses, conforme a quantidade de parcelas escolhida. Assim, em cinco parcelas, R$ 400,00 são somados aos cinco primeiros aluguéis. Depois disso, permanece apenas o aluguel mensal. Quando a divisão produz diferença de centavos, a última parcela é ajustada para que a soma seja exatamente R$ 2.000,00. Em três vezes, por exemplo: R$ 666,67, R$ 666,67 e R$ 666,66.

## Vídeo de apresentação

Assista à apresentação do projeto no YouTube:

[Vídeo de apresentação — Gerador de Orçamento R.M.]

(https://youtu.be/4btf0StisUQ)

## Autor

Jhonatan Franco - Engenharia da Computação

