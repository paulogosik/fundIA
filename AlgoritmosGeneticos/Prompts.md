# Prompts utilizados — Trabalho de Algoritmo Genético

> Documento exigido pela atividade. Contém o(s) prompt(s) enviados à IA generativa (Claude) durante a construção do trabalho, descrevendo o pedido feito e o que foi produzido.

---

## Contexto

A atividade pediu três entregáveis: um web app demonstrando o funcionamento de um algoritmo genético aplicado a uma tarefa real, slides de apresentação (até 5 minutos) e os prompts usados com a IA generativa. Foram anexados ao chat o PDF do slide de aula do professor (referência teórica — Russell & Norvig, 4ª ed.) e a instrução da atividade.

---

## Prompt principal

> Meu professor de Fundamentos de Inteligência Artificial me passou essa atividade, onde eu lhe enviei as instruções da atividade e também lhe enviei o slide que ele usou para passar o conteúdo nessa aula. O que eu quero é simples: eu quero o web app que ele pediu, também quero o roteiro para eu criar o slide ou o slide já, o arquivo pronto para eu poder só enviar. Além disso, quero um roteiro de apresentação desse slide, certo? Para recapitular, são três coisas:
>
> 1. Web app feito
> 2. O slide feito ou um briefing para eu poder fazer
> 3. Um roteiro de apresentação, sabendo que são até cinco minutos
>
> Outra coisa, também quero que seja algo simplório. Não precisa ser algo super produzido, algo muito complexo. Era o simplório e que funcione de fato. Então é bem simples, não é algo que é para ser hiper complexo. Eu só um trabalho comum, então só quero algo funcional e bom. Não precisa ser nada complexo, complicado, nada disso.

## Decisões tomadas a partir do prompt

Com base no material do professor, escolhi o **exemplo do próprio slide (página 29-31)**: evoluir uma população de strings aleatórias até chegar na string-alvo **"Algoritmos Geneticos"**. É didático, visualmente claro e demonstra todos os conceitos da aula (cromossomo, fitness, seleção, cruzamento, mutação) sem precisar de um problema externo complexo.

### Decisões técnicas

- **Web app em arquivo único HTML/CSS/JS** — sem build, sem dependências externas, sem framework. Abre direto no navegador, fácil de avaliar e hospedar (GitHub Pages, por exemplo).
- **Algoritmo:** seleção por torneio (k=5), cruzamento de 1 ponto, mutação bit-a-bit, elitismo opcional. Tudo configurável na interface.
- **Visualização:** geração atual, melhor fitness, média, gráfico de evolução em canvas puro, lista dos 12 melhores indivíduos com coloração caractere a caractere (verde = correto, vermelho = incorreto).
- **Validação:** o algoritmo foi replicado em Python com seed fixa para confirmar convergência — convergiu em ~27-36 gerações.

### Decisões de apresentação

- **7 slides** (incluindo capa e conclusão) — quantidade certa para 5 minutos.
- **Tema visual:** dark mode com acentos verde lima e laranja, alinhado com a estética do web app para criar coerência visual entre os entregáveis.
- **Estrutura narrativa:** o que é → como funciona → o problema → demonstração → resultados → conclusão.

---

## Observação sobre uso de IA

Este projeto foi desenvolvido com auxílio de IA generativa (Claude) para acelerar a construção dos artefatos a partir do material teórico fornecido pelo professor. O conteúdo conceitual (definições, ciclo do AG, parâmetros) foi extraído diretamente do slide de aula referenciado em Russell & Norvig (2022), 4ª edição. A IA foi usada como ferramenta de implementação — escrita do código JavaScript, geração do PPTX e elaboração do roteiro — sob direcionamento e revisão.
