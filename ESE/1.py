# 1. Recursive Depth First Search (DFS) – Read undirected unweighted graph from a CSV file
import pandas as pd

# Read the adjacency matrix from CSV file
df = pd.read_csv('graph.csv', index_col=0)

# Convert DataFrame to dictionary for adjacency list
graph = {node: [] for node in df.columns}
for i in df.columns:
    for j in df.columns:
        if df.loc[i, j] == 1:
            graph[i].append(j)

# DFS Function (Recursive)
def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# Run DFS
start_node = input("Enter start node: ")
print("DFS Traversal:")
dfs_recursive(graph, start_node, set())
