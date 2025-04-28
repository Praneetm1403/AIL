# 3. Breadth First Search (BFS) – Read undirected unweighted graph from user
from collections import deque

# Input graph
def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        graph[node] = neighbors
    return graph

# BFS Function
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Run BFS
graph = input_graph()
start_node = input("Enter start node: ")
print("BFS Traversal:")
bfs(graph, start_node)
