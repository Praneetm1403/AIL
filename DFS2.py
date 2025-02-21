import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Load edges from the CSV file
filepath = r'C:\Users\Praneet\Desktop\AIL\Assignment1\edges.csv'
edges_df = pd.read_csv(filepath)
edges = list(zip(edges_df['source'], edges_df['target']))

# Create a graph
graph = nx.Graph()
graph.add_edges_from(edges)

# Recursive DFS with Tree Format
def recursive_dfs_tree(graph, node, visited=None, depth=0, tree_edges=[]):
    if visited is None:
        visited = set()

    visited.add(node)
    
    for neighbor in sorted(graph.neighbors(node)):
        if neighbor not in visited:
            tree_edges.append((node, neighbor))
            recursive_dfs_tree(graph, neighbor, visited, depth + 1, tree_edges)
    
    return tree_edges

# Iterative DFS with Tree Format
def iterative_dfs_tree(graph, start_node):
    visited = set()
    stack = [(start_node, 0)]  # Stack stores (node, depth)
    tree_edges = []

    while stack:
        node, depth = stack.pop()
        if node not in visited:
            visited.add(node)
            
            for neighbor in sorted(graph.neighbors(node), reverse=True):
                if neighbor not in visited:
                    tree_edges.append((node, neighbor))
                    stack.append((neighbor, depth + 1))
    
    return tree_edges

# Visualize the graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='pink', edge_color='black')
plt.title("Original Graph")
plt.show()

# Perform Recursive DFS and visualize
tree_edges_recursive = recursive_dfs_tree(graph, 'A')
dfs_tree_recursive = nx.Graph()
dfs_tree_recursive.add_edges_from(tree_edges_recursive)

plt.figure(figsize=(8, 6))
nx.draw(dfs_tree_recursive, pos, with_labels=True, node_color='lightblue', edge_color='red')
plt.title("Recursive DFS Tree")
plt.show()

# Perform Iterative DFS and visualize
tree_edges_iterative = iterative_dfs_tree(graph, 'A')
dfs_tree_iterative = nx.Graph()
dfs_tree_iterative.add_edges_from(tree_edges_iterative)

plt.figure(figsize=(8, 6))
nx.draw(dfs_tree_iterative, pos, with_labels=True, node_color='lightgreen', edge_color='blue')
plt.title("Iterative DFS Tree")
plt.show()

print("Recursive DFS (Tree Format):")
print(tree_edges_recursive)
print("\nIterative DFS (Tree Format):")
print(tree_edges_iterative)
