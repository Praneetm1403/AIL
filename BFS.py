#BFS with Tree Format

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# edges from csv       

filepath = r'C:\Users\Praneet\Desktop\AIL\Assignment2\edges.csv'
edges_df = pd.read_csv(filepath)
# Create weighted edges as tuples of (source, target, weight)
edges = [(row['source'], row['target'], row['weight']) for _, row in edges_df.iterrows()]

# create a weighted graph
graph = nx.Graph()
# Add edges with weights
graph.add_weighted_edges_from(edges)


# perform BFS in tree Format

def bfs_tree(graph, start_node):
    # Create a new graph for the BFS tree
    bfs_tree = nx.Graph()
    
    visited = set()
    queue = [(None, start_node)]  # (parent, node)
    sequence = []  # Track BFS sequence
    
    while queue:
        parent, node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            sequence.append(node)  # Add node to sequence
            # Add edge to tree if there's a parent
            if parent is not None:
                weight = graph[parent][node]['weight']
                bfs_tree.add_edge(parent, node, weight=weight)
            
            # Add unvisited neighbors to queue
            for neighbor in sorted(graph.neighbors(node)):
                if neighbor not in visited:
                    queue.append((node, neighbor))
    
    print("BFS Sequence:", ' -> '.join(sequence))  # Print the sequence
    return bfs_tree


# visualize the graph with weights
plt.figure(figsize=(9,6))
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='Green', edge_color='Blue')
# Draw edge weights
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.title("Input Graph")
plt.show()

# Create and display the BFS tree
bfs_result = bfs_tree(graph, 'B')

# Visualize the BFS tree with weights
plt.figure(figsize=(10, 6))
pos_tree = nx.spring_layout(bfs_result)
nx.draw(bfs_result, pos_tree, with_labels=True, node_color='Green', edge_color='Blue')
edge_labels = nx.get_edge_attributes(bfs_result, 'weight')
nx.draw_networkx_edge_labels(bfs_result, pos_tree, edge_labels=edge_labels)
plt.title("BFS Tree")
plt.show()

# Perform BFS with Tree Format
print("BFS (Tree Format):")
bfs_result = bfs_tree(graph, 'B')  # Store the result

# Perform BFS with Graph Format

# print("\nBFS (Graph Format):")
# bfs_graph(graph, '')       

