"""
Пример представления графа через список смежности.
"""

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}


# Обход в глубину (DFS)
def dfs(node, visited=set()):
    if node not in visited:
        print(node)  # Вывод: порядок обхода
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)


dfs(0)
