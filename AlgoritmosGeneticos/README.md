# Algoritmo Genético — Demonstração

Web app + apresentação demonstrando o funcionamento de um algoritmo genético clássico aplicado à evolução de strings.

**Trabalho da disciplina Fundamentos de Inteligência Artificial** — Prof. Jackson Gomes.

## Sobre

O algoritmo evolui uma população de strings aleatórias de 20 caracteres até atingir uma string-alvo configurável (padrão: `"Algoritmos Geneticos"`). Implementa:

- Seleção por torneio (k configurável)
- Cruzamento de 1 ponto
- Mutação bit-a-bit
- Elitismo opcional

Espaço de busca: **53²⁰ ≈ 9×10⁶⁸ estados possíveis**. O algoritmo converge tipicamente em **20-40 gerações**.

## Como executar

Abra `index.html` em qualquer navegador moderno. Não tem build, não tem dependências.

```bash
# Opção 1: dois cliques
open index.html

# Opção 2: servidor local
python3 -m http.server 8000
# acesse http://localhost:8000
```

## Como usar

1. (Opcional) Mude os parâmetros no painel esquerdo — string-alvo, tamanho da população, taxa de mutação, etc.
2. Clique em **▶ Iniciar**.
3. Acompanhe a evolução no painel principal: melhor indivíduo, gráfico de fitness, top 12 da população.
4. Use **⏸ Pausar** para inspecionar o estado, **↺ Reiniciar população** para recomeçar com população nova.

### Parâmetros recomendados

| Parâmetro          | Valor padrão | Observação                                   |
|--------------------|:------------:|----------------------------------------------|
| População          | 200          | Maior = mais rápido em gerações, mas mais lento em tempo |
| Taxa de mutação    | 3%           | Baixa demais estagna, alta demais destrói boas soluções |
| Torneio (k)        | 5            | Maior = mais pressão seletiva                |
| Elitismo           | Ligado       | Garante que o melhor nunca é perdido         |

## Arquivos do projeto

- `index.html` — Web app (arquivo único, autocontido)
- `Algoritmo_Genetico.pptx` — Slides da apresentação
- `Roteiro_Apresentacao.md` — Roteiro para apresentar em ~5 minutos
- `Prompts.md` — Prompts utilizados com a IA generativa

## Referência

RUSSELL, S. J.; NORVIG, P. **Inteligência Artificial: Uma Abordagem Moderna**. 4ª ed. Rio de Janeiro: LTC, 2022.
