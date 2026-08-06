# Revisão das exigências do trabalho

## Regras do orçamento

| Item do enunciado | Implementação | Situação |
|---|---|---|
| Apartamento com 1 quarto: R$ 700,00 | Classe `Apartamento` | Atendido |
| Segundo quarto do apartamento: + R$ 200,00 | Classe `Apartamento` | Atendido |
| Casa com 1 quarto: R$ 900,00 | Classe `Casa` | Atendido |
| Segundo quarto da casa: + R$ 250,00 | Classe `Casa` | Atendido |
| Estúdio: R$ 1.200,00 | Classe `Estudio` | Atendido |
| Garagem de casa/apartamento: + R$ 300,00 | Classes `Casa` e `Apartamento` | Atendido |
| Duas vagas do estúdio: + R$ 250,00 | Classe `Estudio` | Atendido |
| Vaga adicional do estúdio: + R$ 60,00 | Classe `Estudio` | Atendido |
| Apartamento sem crianças: desconto de 5% | Classe `Apartamento` | Atendido |
| Contrato de R$ 2.000,00 em até 5 vezes | Classe `Orcamento` | Atendido |
| Exibir o aluguel mensal com o contrato | Memória de cálculo da interface | Atendido |
| Gerar CSV com 12 parcelas | Serviço `gerador_csv` | Atendido |
| Manter tela e CSV coerentes após alterações | Resultado é invalidado até novo cálculo | Atendido |

Foram aprovados 10 testes automatizados, incluindo todas as opções de 1 a 5
parcelas e o ajuste de centavos para o contrato dividido em 3 vezes.

## Delimitação sobre área ou metragem

A metragem é citada somente no parágrafo introdutório como exemplo de informação
que aplicações imobiliárias costumam cadastrar. O enunciado não define preço por
metro quadrado e não inclui área entre as regras obrigatórias do orçamento. Assim,
não seria correto inventar um cálculo por área. O sistema utiliza apenas os valores
e critérios expressamente fornecidos pelo professor.

## Entregáveis

| Entregável obrigatório | Conteúdo preparado | Situação |
|---|---|---|
| PDF teórico (25%) | Fluxograma, lógica, pensamento algorítmico, pseudocódigo e explicações | Preparado |
| Projeto prático (50%) | Código Python funcional, orientação a objetos, interface e CSV | Preparado |
| Link do GitHub | Deve ser inserido pelo aluno após publicar o projeto | Pendente do aluno |
| Vídeo de até 4 minutos (25%) | Roteiro pronto para gravação e demonstração | Pendente do aluno |
| Link do vídeo publicado | Deve ser informado pelo aluno após a publicação | Pendente do aluno |

Observação: arquivos HTML/CSS são exigidos apenas se a interface utilizar essas
tecnologias. Como a interface foi desenvolvida com Tkinter, eles não se aplicam.
