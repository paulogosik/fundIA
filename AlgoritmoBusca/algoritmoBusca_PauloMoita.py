"""
Algoritmos de Busca em Grafos
Fundamentos de Inteligência Artificial

Problema: Encontrar o menor caminho entre cidades brasileiras
          representadas em um grafo ponderado.

Algoritmos implementados:
  - Busca em Largura (BFS)
  - Busca em Profundidade (DFS)
  - Dijkstra (Busca de Custo Uniforme)
  - A* (A Estrela)
"""

import heapq
from collections import deque
import math


# ===========================================================
# DEFINIÇÃO DO GRAFO (Mapa de cidades com distâncias em km)
# ===========================================================

# Grafo não-ponderado (para BFS e DFS — apenas conexões)
grafo_nao_ponderado = {
    "Brasília":    ["Goiânia", "Belo Horizonte", "Palmas"],
    "Goiânia":     ["Brasília", "Cuiabá", "Campo Grande"],
    "Belo Horizonte": ["Brasília", "Rio de Janeiro", "São Paulo"],
    "Palmas":      ["Brasília", "Belém", "São Luís"],
    "Rio de Janeiro": ["Belo Horizonte", "São Paulo"],
    "São Paulo":   ["Belo Horizonte", "Rio de Janeiro", "Curitiba", "Campo Grande"],
    "Curitiba":    ["São Paulo", "Porto Alegre"],
    "Porto Alegre":["Curitiba"],
    "Campo Grande":["Goiânia", "São Paulo", "Cuiabá"],
    "Cuiabá":      ["Goiânia", "Campo Grande", "Porto Velho"],
    "Porto Velho": ["Cuiabá", "Manaus"],
    "Manaus":      ["Porto Velho", "Belém"],
    "Belém":       ["Manaus", "Palmas", "São Luís"],
    "São Luís":    ["Belém", "Palmas", "Fortaleza"],
    "Fortaleza":   ["São Luís", "Recife"],
    "Recife":      ["Fortaleza", "Salvador"],
    "Salvador":    ["Recife", "Belo Horizonte"],
}

# Grafo ponderado (distâncias aproximadas em km — para Dijkstra e A*)
grafo_ponderado = {
    "Brasília":    [("Goiânia", 209), ("Belo Horizonte", 741), ("Palmas", 973)],
    "Goiânia":     [("Brasília", 209), ("Cuiabá", 694), ("Campo Grande", 839)],
    "Belo Horizonte": [("Brasília", 741), ("Rio de Janeiro", 434), ("São Paulo", 586), ("Salvador", 1372)],
    "Palmas":      [("Brasília", 973), ("Belém", 1317), ("São Luís", 1165)],
    "Rio de Janeiro": [("Belo Horizonte", 434), ("São Paulo", 429)],
    "São Paulo":   [("Belo Horizonte", 586), ("Rio de Janeiro", 429), ("Curitiba", 408), ("Campo Grande", 987)],
    "Curitiba":    [("São Paulo", 408), ("Porto Alegre", 710)],
    "Porto Alegre":  [("Curitiba", 710)],
    "Campo Grande":  [("Goiânia", 839), ("São Paulo", 987), ("Cuiabá", 694)],
    "Cuiabá":      [("Goiânia", 694), ("Campo Grande", 694), ("Porto Velho", 1450)],
    "Porto Velho": [("Cuiabá", 1450), ("Manaus", 904)],
    "Manaus":      [("Porto Velho", 904), ("Belém", 2329)],
    "Belém":       [("Manaus", 2329), ("Palmas", 1317), ("São Luís", 802)],
    "São Luís":    [("Belém", 802), ("Palmas", 1165), ("Fortaleza", 1069)],
    "Fortaleza":   [("São Luís", 1069), ("Recife", 800)],
    "Recife":      [("Fortaleza", 800), ("Salvador", 839)],
    "Salvador":    [("Recife", 839), ("Belo Horizonte", 1372)],
}

# Coordenadas aproximadas das cidades (latitude, longitude) — usadas pela heurística A*
coordenadas = {
    "Brasília":       (-15.78, -47.93),
    "Goiânia":        (-16.69, -49.25),
    "Belo Horizonte": (-19.92, -43.94),
    "Palmas":         (-10.25, -48.36),
    "Rio de Janeiro": (-22.91, -43.17),
    "São Paulo":      (-23.55, -46.63),
    "Curitiba":       (-25.43, -49.27),
    "Porto Alegre":   (-30.03, -51.23),
    "Campo Grande":   (-20.47, -54.62),
    "Cuiabá":         (-15.60, -56.10),
    "Porto Velho":    (-8.76,  -63.90),
    "Manaus":         (-3.10,  -60.01),
    "Belém":          (-1.46,  -48.50),
    "São Luís":       (-2.53,  -44.30),
    "Fortaleza":      (-3.72,  -38.54),
    "Recife":         (-8.05,  -34.88),
    "Salvador":       (-12.97, -38.50),
}


def distancia_linha_reta(cidade_a, cidade_b):
    """Calcula distância em linha reta entre duas cidades (heurística admissível para A*)."""
    lat1, lon1 = coordenadas[cidade_a]
    lat2, lon2 = coordenadas[cidade_b]
    # Aproximação em km (1 grau ≈ 111 km)
    dlat = (lat2 - lat1) * 111
    dlon = (lon2 - lon1) * 111 * math.cos(math.radians((lat1 + lat2) / 2))
    return math.sqrt(dlat**2 + dlon**2)


# ===========================================================
# ALGORITMO 1: BUSCA EM LARGURA (BFS)
# ===========================================================

def bfs(grafo, inicio, meta):
    """
    Busca em Largura (Breadth-First Search).
    Garante encontrar o caminho com MENOR NÚMERO DE ARESTAS.
    Usa fila FIFO.
    """
    if inicio == meta:
        return [inicio], 0

    fronteira = deque([(inicio, [inicio])])   # (nó_atual, caminho_até_aqui)
    alcancados = {inicio}
    nos_expandidos = 0

    while fronteira:
        no, caminho = fronteira.popleft()
        nos_expandidos += 1

        for vizinho in grafo.get(no, []):
            if vizinho == meta:
                return caminho + [vizinho], nos_expandidos
            if vizinho not in alcancados:
                alcancados.add(vizinho)
                fronteira.append((vizinho, caminho + [vizinho]))

    return None, nos_expandidos  # Sem solução


# ===========================================================
# ALGORITMO 2: BUSCA EM PROFUNDIDADE (DFS)
# ===========================================================

def dfs(grafo, inicio, meta):
    """
    Busca em Profundidade (Depth-First Search).
    Não garante o caminho ótimo. Usa pilha LIFO.
    """
    if inicio == meta:
        return [inicio], 0

    fronteira = [(inicio, [inicio])]   # pilha: (nó_atual, caminho)
    alcancados = {inicio}
    nos_expandidos = 0

    while fronteira:
        no, caminho = fronteira.pop()
        nos_expandidos += 1

        for vizinho in grafo.get(no, []):
            if vizinho == meta:
                return caminho + [vizinho], nos_expandidos
            if vizinho not in alcancados:
                alcancados.add(vizinho)
                fronteira.append((vizinho, caminho + [vizinho]))

    return None, nos_expandidos


# ===========================================================
# ALGORITMO 3: DIJKSTRA (Busca de Custo Uniforme)
# ===========================================================

def dijkstra(grafo, inicio, meta):
    """
    Algoritmo de Dijkstra (Busca de Custo Uniforme).
    Garante o caminho de MENOR CUSTO em grafos ponderados.
    Usa fila de prioridade (min-heap).
    """
    # (custo_acumulado, nó_atual, caminho)
    fronteira = [(0, inicio, [inicio])]
    alcancados = {}   # {nó: menor_custo_encontrado}
    nos_expandidos = 0

    while fronteira:
        custo, no, caminho = heapq.heappop(fronteira)
        nos_expandidos += 1

        if no == meta:
            return caminho, custo, nos_expandidos

        if no in alcancados:
            continue
        alcancados[no] = custo

        for vizinho, peso in grafo.get(no, []):
            novo_custo = custo + peso
            if vizinho not in alcancados:
                heapq.heappush(fronteira, (novo_custo, vizinho, caminho + [vizinho]))

    return None, float('inf'), nos_expandidos


# ===========================================================
# ALGORITMO 4: A* (A Estrela)
# ===========================================================

def a_estrela(grafo, inicio, meta):
    """
    Busca A* (A Estrela).
    Usa f(n) = g(n) + h(n):
      g(n) = custo real do caminho até n
      h(n) = heurística admissível (distância em linha reta até a meta)
    Garante o caminho ÓTIMO se a heurística for admissível.
    """
    h_inicial = distancia_linha_reta(inicio, meta)
    # (f(n), g(n), nó_atual, caminho)
    fronteira = [(h_inicial, 0, inicio, [inicio])]
    alcancados = {}
    nos_expandidos = 0

    while fronteira:
        f, g, no, caminho = heapq.heappop(fronteira)
        nos_expandidos += 1

        if no == meta:
            return caminho, g, nos_expandidos

        if no in alcancados:
            continue
        alcancados[no] = g

        for vizinho, peso in grafo.get(no, []):
            novo_g = g + peso
            if vizinho not in alcancados:
                h = distancia_linha_reta(vizinho, meta)
                novo_f = novo_g + h
                heapq.heappush(fronteira, (novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf'), nos_expandidos


# ===========================================================
# EXECUÇÃO E COMPARAÇÃO DOS ALGORITMOS
# ===========================================================

def formatar_caminho(caminho):
    return " → ".join(caminho) if caminho else "SEM SOLUÇÃO"


def executar_comparacao():
    casos = [
        ("Manaus", "Porto Alegre"),
        ("Brasília", "Recife"),
        ("Cuiabá", "Fortaleza"),
    ]

    print("=" * 70)
    print("  RESOLUÇÃO DE PROBLEMAS POR BUSCA — CIDADES BRASILEIRAS")
    print("=" * 70)

    for origem, destino in casos:
        print(f"\n{'─'*70}")
        print(f"  ORIGEM: {origem}  →  DESTINO: {destino}")
        print(f"{'─'*70}")

        # --- BFS ---
        caminho_bfs, exp_bfs = bfs(grafo_nao_ponderado, origem, destino)
        print(f"\n[1] BFS (Busca em Largura)")
        print(f"    Caminho : {formatar_caminho(caminho_bfs)}")
        print(f"    Arestas : {len(caminho_bfs)-1 if caminho_bfs else 'N/A'}")
        print(f"    Nós expandidos: {exp_bfs}")

        # --- DFS ---
        caminho_dfs, exp_dfs = dfs(grafo_nao_ponderado, origem, destino)
        print(f"\n[2] DFS (Busca em Profundidade)")
        print(f"    Caminho : {formatar_caminho(caminho_dfs)}")
        print(f"    Arestas : {len(caminho_dfs)-1 if caminho_dfs else 'N/A'}")
        print(f"    Nós expandidos: {exp_dfs}")

        # --- Dijkstra ---
        caminho_dijk, custo_dijk, exp_dijk = dijkstra(grafo_ponderado, origem, destino)
        print(f"\n[3] Dijkstra (Busca de Custo Uniforme)")
        print(f"    Caminho : {formatar_caminho(caminho_dijk)}")
        print(f"    Custo   : {custo_dijk} km")
        print(f"    Nós expandidos: {exp_dijk}")

        # --- A* ---
        caminho_ast, custo_ast, exp_ast = a_estrela(grafo_ponderado, origem, destino)
        print(f"\n[4] A* (A Estrela)")
        print(f"    Caminho : {formatar_caminho(caminho_ast)}")
        print(f"    Custo   : {custo_ast:.0f} km")
        print(f"    Nós expandidos: {exp_ast}")

    print(f"\n{'='*70}\n")


if __name__ == "__main__":
    executar_comparacao()
