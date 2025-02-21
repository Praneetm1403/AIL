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
def recursive_dfs_tree(graph, node, visited=None, depth=0):
    if visited is None:
        visited = set()

    # Mark the node as visited
    visited.add(node)

    # Print the current node with proper indentation
    print(" " * (2 * depth) + node)

    # Recurse through the neighbors in sorted order
    for neighbor in sorted(graph.neighbors(node)):
        if neighbor not in visited:
            recursive_dfs_tree(graph, neighbor, visited, depth + 1)

# Iterative DFS with Tree Format
def iterative_dfs_tree(graph, start_node):
    visited = set()
    stack = [(start_node, 0)]  # Stack stores (node, depth)

    while stack:
        node, depth = stack.pop()
        if node not in visited:
            # Mark the node as visited and print it with proper indentation
            visited.add(node)
            print(" " * (2 * depth) + node)

            # Add neighbors to the stack with increased depth, sorted for consistent order
            for neighbor in sorted(graph.neighbors(node), reverse=True):
                stack.append((neighbor, depth + 1))

# Visualize the graph
nx.draw(graph, with_labels=True, node_color='pink', edge_color='black')
plt.show()

# Perform Recursive DFS
print("Recursive DFS (Tree Format):")
recursive_dfs_tree(graph, 'A')

# Perform Iterative DFS
print("\nIterative DFS (Tree Format):")
iterative_dfs_tree(graph, 'A')
