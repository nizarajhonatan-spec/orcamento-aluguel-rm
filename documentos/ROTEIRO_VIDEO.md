# Roteiro do vídeo pitch - duração aproximada: 3min30s

## 0:00 a 0:25 - Apresentação

“Olá, meu nome é Jhonatan Franco e este é o projeto Gerador de Orçamento de Aluguel da imobiliária R.M., desenvolvido para a disciplina Algorithmic Thinking & Introduction to Object-Oriented Programming. O objetivo é automatizar o cálculo de aluguel de casas, apartamentos e estúdios.”

## 0:25 a 1:05 - Organização do projeto

“Separei o projeto em três partes. Na pasta modelos estão as classes dos imóveis. A classe Imovel é abstrata e serve como base. Apartamento, Casa e Estudio herdam dela e implementam seu próprio cálculo, demonstrando herança e polimorfismo. Na pasta serviços estão o orçamento e o gerador de CSV. O arquivo main.py contém apenas a interface e conecta a tela às regras de negócio.”

Mostre rapidamente a árvore de pastas e abra `modelos/imovel.py`.

## 1:05 a 1:45 - Regras e pensamento algorítmico

“O algoritmo começa com um valor-base. Depois avalia as escolhas do usuário por meio de condições. Por exemplo, um apartamento parte de setecentos reais; o segundo quarto soma duzentos, a garagem soma trezentos e, se o cliente não possui crianças, o desconto de cinco por cento é aplicado sobre o aluguel configurado. O contrato de dois mil reais pode ser parcelado de uma a cinco vezes.”

Mostre `calcular_aluguel()` e `gerar_mensalidades()`.

## 1:45 a 2:55 - Demonstração

1. Execute `python main.py`.
2. Escolha **Apartamento**, **2 quartos**, **garagem**, desmarque “possui crianças” e selecione **5 parcelas**.
3. Clique em “Calcular orçamento”.
4. Explique o resultado esperado:
   - aluguel: `(700 + 200 + 300) x 0,95 = R$ 1.140,00`;
   - contrato: `5 x R$ 400,00`;
   - primeira mensalidade: `R$ 1.540,00`;
   - total anual: `12 x R$ 1.140,00 + R$ 2.000,00 = R$ 15.680,00`.
5. Exporte o CSV e abra o arquivo para mostrar as 12 mensalidades.

## 2:55 a 3:25 - Testes e encerramento

“Também criei testes automatizados para validar os valores, as entradas inválidas, o parcelamento e as doze linhas do CSV. Isso reduz erros e facilita a manutenção. Dessa forma, o sistema atende aos requisitos, aplica pensamento algorítmico e utiliza orientação a objetos de maneira organizada. Obrigado.”

Execute `python -m unittest discover -s testes -v` e mostre os testes aprovados.

## Antes de publicar

- Grave em 1080p e deixe o zoom do editor legível.
- Não ultrapasse 4 minutos.
- Publique como “não listado” no YouTube, se preferir.
- Cole o link do vídeo e o link do GitHub no ambiente da faculdade.
