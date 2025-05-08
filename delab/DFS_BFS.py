from collections import deque

graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['E', 'C']
}

def dfs(graph, node, visited =None, path = None):
    if visited is None:
        visited = set()
    if path is None:
        path =[]
    visited.add(node)
    path.append(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited, path)
    return path


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    path = []

    while queue:
        node= queue.popleft()
        if node not in visited:
            visited.add(node)
            path.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return path

dfs_path = dfs(graph, 'A')
bfs_path = bfs(graph, 'A')

print("DFS Traversal Order: ", '->'.join(dfs_path))
print("BFS Traversal Order: ", '->'.join(bfs_path))
