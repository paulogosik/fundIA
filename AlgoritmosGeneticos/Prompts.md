# Prompts utilizados — Trabalho de Algoritmo Genético

> Documento exigido pela atividade. Contém os prompts enviados à IA generativa (Claude) durante a construção do trabalho, descrevendo o pedido feito em cada iteração e o que foi produzido.

---

## Contexto

A atividade pediu três entregáveis: um web app demonstrando o funcionamento de um algoritmo genético aplicado a uma tarefa real, slides de apresentação (até 5 minutos) e os prompts usados com a IA generativa. Foram anexados ao chat o PDF do slide de aula do professor (referência teórica — Russell & Norvig, 4ª ed.) e a instrução da atividade.

O desenvolvimento aconteceu em iterações: comecei com um pedido geral, depois fui refinando o web app, ajustando funcionalidades de visualização, e por fim trabalhei nos slides e no roteiro de apresentação.

---

## Prompt 1 — Pedido inicial

> Estou fazendo um trabalho de Fundamentos de IA sobre algoritmo genético. Estou anexando o slide que o professor usou em aula para você ter o conteúdo de referência (Russell & Norvig, 4ª ed.) e também as instruções da atividade.
>
> Preciso de três coisas: um web app que demonstre o funcionamento de um AG aplicado a uma tarefa real, slides para apresentar em até 5 minutos, e o registro dos prompts usados. Queria começar pelo web app. Pode me ajudar a estruturar isso? Prefiro algo simples e funcional — não precisa ser complexo, é um trabalho comum de graduação.

**Resultado:** definição do escopo e proposta inicial — usar o próprio exemplo do slide do professor (evoluir strings até a frase "Algoritmos Geneticos") por ser didático e alinhado com a aula. Decisão de fazer o web app em arquivo único HTML/CSS/JS, sem dependências externas, para facilitar avaliação e eventual hospedagem em GitHub Pages.

---

## Prompt 2 — Funcionalidades do web app

> Gostei da proposta. Agora quero que o web app deixe eu mexer nos parâmetros do AG durante a própria apresentação — para mostrar na prática como cada parâmetro afeta a convergência. Inclui controles para:
>
> - Tamanho da população
> - Taxa de mutação
> - Tamanho do torneio (seleção)
> - Elitismo ligado/desligado
> - Velocidade de execução (gerações por segundo)
>
> Os botões devem ser Iniciar, Pausar e Reiniciar. E quero poder mudar a própria string-alvo, caso eu queira testar outras palavras durante a apresentação.

**Resultado:** painel lateral de parâmetros com sliders e input para a string-alvo. Implementação do laço principal com `setTimeout` controlável pela velocidade. Estado interno em um único objeto para facilitar pause/resume sem perder a evolução.

---

## Prompt 3 — Visualização e feedback visual

> O algoritmo está rodando bem, mas a interface está visualmente fraca para uma apresentação. Preciso melhorar a parte visual:
>
> 1. Mostra o melhor indivíduo da geração atual em destaque, com os caracteres **certos em verde** e os **errados em vermelho**, para ficar óbvio na hora da apresentação o quanto já evoluiu.
> 2. Adiciona um gráfico de linha mostrando a evolução do fitness ao longo das gerações — duas linhas: melhor indivíduo e média da população.
> 3. Mostra também os 12 melhores indivíduos da geração atual numa lista, com o fitness ao lado de cada um, para o pessoal ver a convergência acontecendo (vários indivíduos quase idênticos no topo).
> 4. Tema dark, fonte monoespaçada para as strings, layout responsivo.

**Resultado:** coloração caractere a caractere com `span`s; gráfico em canvas puro (sem Chart.js) com eixo de fitness e histórico das últimas 500 gerações; lista da população ordenada por fitness. Tema escuro com paleta verde lima + laranja para destaque, fontes JetBrains Mono (strings) + Space Grotesk (UI).

---

## Prompt 4 — Slides e roteiro

> Agora os entregáveis de apresentação. Monta uns 6 ou 7 slides em PowerPoint, no mesmo tema dark do web app, para manter coerência visual entre os entregáveis. Estrutura sugerida: capa, definição do AG, ciclo evolutivo (as 5 etapas), o problema escolhido com o tamanho do espaço de busca, demonstração do app (screenshot real do app rodando), resultados (números: quantas gerações, quanto tempo, etc.) e conclusão.
>
> Depois disso, monta um roteiro de apresentação para 5 minutos, slide a slide, com tempo sugerido para cada um e deixas para eu não me perder. Inclui dicas de apresentação no final — por exemplo, em que slide vale a pena abrir o app ao vivo em vez de só mostrar o screenshot.

**Resultado:** apresentação `.pptx` com 7 slides gerada com geração programática, screenshot capturado com o app já em execução (geração 24, fitness 18/20). Roteiro em Markdown com cronometragem (~20s a ~70s por slide, totalizando ~4min45s) e bloco final de dicas práticas.

---

## Observação sobre uso de IA

Este projeto foi desenvolvido com auxílio de IA generativa (Claude) para acelerar a construção dos artefatos a partir do material teórico fornecido pelo professor. O conteúdo conceitual (definições, ciclo do AG, parâmetros) foi extraído diretamente do slide de aula referenciado em Russell & Norvig (2022), 4ª edição. A IA foi usada como ferramenta de implementação — escrita do código JavaScript, geração do PPTX e elaboração do roteiro — sob direcionamento e revisão a cada iteração.
