import pygame
import random
from enum import Enum
from heapq import heappop, heappush
import time

# === Constantes de cor ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)

# === Dimensões ===
CELL_SIZE = 20
MARGIN = 1

# === Enum para facilitar a leitura ===
class MazeBlocks(Enum):
    WALL = 0
    PASSAGE = 1

# === Gerar labirinto ===
def gen(tamanho: int) -> list[list[int]]:
    def get_neighbors(r, c):
        _n = []
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            x, y = r + dx, c + dy
            if 0 <= x < tamanho and 0 <= y < tamanho and maze_map[x][y] != MazeBlocks.PASSAGE:
                _n.append((x, y))
        return _n

    tamanho = tamanho * 2 + 1
    maze_map = [[MazeBlocks.WALL for _ in range(tamanho)] for _ in range(tamanho)]

    stack = [(1, 1)]
    maze_map[1][1] = MazeBlocks.PASSAGE

    while stack:
        i, j = stack[-1]
        neighbors = get_neighbors(i, j)

        if neighbors:
            neighbor = random.choice(neighbors)
            mid_x = (i + neighbor[0]) // 2
            mid_y = (j + neighbor[1]) // 2
            maze_map[mid_x][mid_y] = MazeBlocks.PASSAGE
            maze_map[neighbor[0]][neighbor[1]] = MazeBlocks.PASSAGE
            stack.append(neighbor)
        else:
            stack.pop()

    maze_map[0][1] = MazeBlocks.PASSAGE
    maze_map[tamanho - 1][tamanho - 2] = MazeBlocks.PASSAGE
    return maze_map

# === Converter labirinto para grafo ===
def maze_to_graph(maze):
    g = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == MazeBlocks.PASSAGE:
                g[(i, j)] = []
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]):
                        if maze[ni][nj] == MazeBlocks.PASSAGE:
                            g[(i, j)].append((ni, nj))
    return g

# === Algoritmo A* ===
def astar(g, start_node, goal_node):
    def heuristica(no, objetivo):
        return abs(no[0] - objetivo[0]) + abs(no[1] - objetivo[1])

    def rebuild_path(n):
        p = [n]
        while n in came_from:
            n = came_from[n]
            p.append(n)
        return p[::-1]

    open_set = [(0, start_node)]      # Fila de prioridade com (prioridade, nó)
    came_from = {}                    # Dicionário que guarda o caminho (quem veio antes)
    cost_so_far = {start_node: 0}     # Custo acumulado desde o início até cada nó
    visitados = set()                 # Conjunto de nós já visitados

    while open_set:
        _, curr_node = heappop(open_set)
        if curr_node in visitados:
            continue
        visitados.add(curr_node)

        if curr_node == goal_node:
            return rebuild_path(goal_node), len(visitados)

        for neighbor in g[curr_node]:
            new_cost = cost_so_far[curr_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                prioridade = new_cost + heuristica(neighbor, goal_node)
                heappush(open_set, (prioridade, neighbor))
                came_from[neighbor] = curr_node
    return None, len(visitados)

# === Algoritmo DFS ===
def dfs(g, start_node, goal_node):
    stack = [(start_node, [start_node])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal_node:
            visited.add(node)
            return path, len(visited)
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(g[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None, len(visited)

# === Visualização com pygame ===
def show_maze(maze, path):
    pygame.init()
    rows, cols = len(maze), len(maze[0])
    screen = pygame.display.set_mode(((CELL_SIZE + MARGIN) * cols, (CELL_SIZE + MARGIN) * rows))
    pygame.display.set_caption("Labirinto com A*")

    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(GRAY)
        for i in range(rows):
            for j in range(cols):
                color = WHITE if maze[i][j] == MazeBlocks.PASSAGE else BLACK
                if path and (i, j) in path:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + CELL_SIZE) * j,
                                  (MARGIN + CELL_SIZE) * i,
                                  CELL_SIZE,
                                  CELL_SIZE])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# === Execução principal ===
if __name__ == "__main__":
    tamanho_logico = 15
    maze = gen(tamanho_logico)
    grafo = maze_to_graph(maze)
    inicio = (0, 1)
    fim = (len(maze) - 1, len(maze[0]) - 2)

    # Teste A*
    inicio_tempo = time.time()
    caminho_astar, visitados_astar = astar(grafo, inicio, fim)
    tempo_astar = time.time() - inicio_tempo

    # Teste DFS
    inicio_tempo = time.time()
    caminho_dfs, visitados_dfs = dfs(grafo, inicio, fim)
    tempo_dfs = time.time() - inicio_tempo

    # Resultados
    print("\n=== Comparação ===")
    print(f"A*:  Tempo = {tempo_astar:.5f}s | Nós visitados = {visitados_astar}")
    print(f"DFS: Tempo = {tempo_dfs:.5f}s | Nós visitados = {visitados_dfs}")

    # Mostrar labirinto com caminho encontrado (A* por padrão)
    caminho_exibicao = caminho_astar or caminho_dfs
    if caminho_exibicao:
        show_maze(maze, caminho_exibicao)
    else:
        print("Nenhum caminho encontrado por qualquer algoritmo!")
