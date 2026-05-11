# Roteiro de Apresentação — Algoritmo Genético

**Duração total: ~5 minutos**
**Slides: 7**

Cada bloco abaixo corresponde a um slide. O tempo é uma sugestão — mantenha um ritmo natural. Os trechos em *itálico* são deixas/transições. Os trechos em **negrito** são pontos-chave para enfatizar com a voz.

---

## Slide 1 — Capa (~20 segundos)

> Bom dia/boa tarde, pessoal. Hoje eu vou mostrar uma demonstração de **algoritmo genético** — uma técnica de busca local inspirada na evolução biológica. A ideia é construir um web app que mostra, em tempo real, como uma população aleatória pode evoluir até resolver um problema. *Vamos começar entendendo o que é, exatamente, um algoritmo genético.*

---

## Slide 2 — O que é (~40 segundos)

> Um algoritmo genético é uma **técnica de busca local**. Diferente da busca tradicional, aqui o caminho não importa — só interessa o estado final, ou seja, a solução.
>
> Ele funciona assim: a gente cria uma **população de candidatos a solução**. A cada geração, os mais aptos têm maior chance de gerar descendentes, e esses descendentes herdam as características dos pais com pequenas variações aleatórias. Com o tempo, a população **evolui** em direção a soluções cada vez melhores.
>
> *Como qualquer algoritmo, ele segue um ciclo bem definido — vamos ver.*

---

## Slide 3 — O ciclo evolutivo (~45 segundos)

> O AG sempre repete essas cinco etapas:
>
> 1. **População inicial**: a gente cria N indivíduos aleatórios.
> 2. **Fitness**: avalia cada indivíduo segundo uma função objetivo. Quanto maior o fitness, melhor a solução.
> 3. **Seleção**: escolhe os pais que vão se reproduzir — geralmente quem tem fitness mais alto tem mais chance.
> 4. **Cruzamento**: combina dois pais para gerar filhos que misturam características dos dois.
> 5. **Mutação**: aplica pequenas alterações aleatórias para manter diversidade.
>
> *Isso se repete até a gente encontrar a solução ou atingir um limite de tempo.*

---

## Slide 4 — O problema (~40 segundos)

> Pro nosso experimento, escolhi um problema bem visual: **evoluir uma população de strings aleatórias até chegar exatamente na frase "Algoritmos Geneticos"**.
>
> Cada indivíduo é uma sequência de 20 caracteres, com 53 símbolos possíveis — letras maiúsculas, minúsculas e espaço.
>
> *E aqui vem o ponto interessante:* o espaço de busca é **53 elevado a 20** — isso dá aproximadamente **9 vezes 10 elevado a 68 estados possíveis**.
>
> Pra dar contexto: isso é mais que o número de átomos no universo observável. **Busca exaustiva seria impossível** — mas o AG resolve em segundos.

---

## Slide 5 — Web app em ação (~70 segundos)

> *Aqui está o web app rodando.* Do lado esquerdo eu controlo os parâmetros: tamanho da população, taxa de mutação, tamanho do torneio, elitismo, velocidade.
>
> No centro vocês veem o **melhor indivíduo da geração atual** — os caracteres em **verde** já estão na posição correta, os caracteres em **vermelho** ainda não.
>
> *Neste momento da captura, estamos na geração 24, com fitness 18 de 20 — em apenas 2 segundos.*
>
> Embaixo tem dois elementos importantes:
>
> - O **gráfico de fitness** — a linha verde é o melhor indivíduo, a laranja é a média da população. A média sobe junto com o melhor: isso é a **evolução acontecendo**.
> - A **lista dos 12 melhores indivíduos** — repare como vários já são quase idênticos. A população **converge** em torno das boas soluções.

---

## Slide 6 — Resultados (~50 segundos)

> Rodando com 200 indivíduos por geração, taxa de mutação de 3% e elitismo ativo, o algoritmo encontrou a solução exata em **36 gerações** — **3 segundos e 3 décimos**.
>
> *Olhem a comparação:* a gente avaliou apenas **7200 indivíduos** — isso é 36 gerações vezes 200 — de um universo de **9 vezes 10 elevado a 68 possibilidades**.
>
> Por que funciona tão bem?
> - O **elitismo** garante que o melhor indivíduo nunca é perdido.
> - A **mutação de 3%** mantém diversidade sem destruir bons indivíduos.
> - O **torneio** combina pressão seletiva com exploração.

---

## Slide 7 — Conclusão (~30 segundos)

> Pra fechar, três pontos:
>
> 1. **AGs resolvem o que busca exaustiva não consegue.** Espaços de busca enormes deixam de ser um problema.
> 2. **Os parâmetros importam muito.** Mutação alta demais destrói soluções boas; baixa demais estagna. Achar o equilíbrio é parte do projeto.
> 3. **Aplicações reais** vão muito além disso: projeto de circuitos, escalonamento de tarefas, otimização de rotas, ajuste de hiperparâmetros em machine learning...
>
> *É isso. Obrigado!*

---

## Dicas de apresentação

- **Pratique uma vez cronometrando.** Se passar de 5 minutos, corte o slide 2 ou abrevie o slide 5.
- **No slide 5, se possível, abra o web app de verdade** e mostre ao vivo em vez de só falar do screenshot — é muito mais impactante. Clique em "Iniciar" no início da apresentação para terminar na hora certa.
- **Vocabulário:** use "indivíduo" e "solução" como sinônimos, "geração" como uma iteração, "fitness" como pontuação.
- Se alguém perguntar **por que o AG e não outra técnica**: responda que AG é particularmente bom quando o espaço de busca é muito grande, descontínuo ou difícil de modelar matematicamente — coisas que dificultam métodos como gradiente descendente.
