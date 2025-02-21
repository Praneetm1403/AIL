# Best First Search with Tree Format

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import heapq

# Read edges from CSV file
filepath = r'C:\Users\Praneet\Desktop\AIL\Assignment2\edges.csv'
edges_df = pd.read_csv(filepath)

# Create weighted edges as tuples of (source, target, weight)
edges = [(row['source'], row['target'], row['weight']) for _, row in edges_df.iterrows()]

# Create a weighted graph
graph = nx.Graph()
graph.add_weighted_edges_from(edges)

# Perform Best First Search in Tree Format
def best_first_search_tree(graph, start_node, goal_node):
    bfs_tree = nx.Graph()
    priority_queue = [(0, start_node)]
    visited = set()
    path = []
    parent = {start_node: None}  # Add parent dictionary to track path

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)
        path.append(node)

        if node == goal_node:
            # Reconstruct and print the actual path
            actual_path = []
            current = goal_node
            while current is not None:
                actual_path.append(current)
                current = parent.get(current)
            actual_path.reverse()
            print("Best First Search Path:", " -> ".join(actual_path))
            return bfs_tree

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                weight = graph[node][neighbor]['weight']
                heapq.heappush(priority_queue, (weight, neighbor))
                bfs_tree.add_edge(node, neighbor, weight=weight)
                parent[neighbor] = node  # Track parent for path reconstruction

    print("No path found")
    return bfs_tree

# Visualize the input graph
plt.figure(figsize=(9, 6))
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='Green', edge_color='Blue')
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.title("Input Graph")
plt.show()

# Wrap the visualization code in a try-except block
try:
    # Perform Best First Search and visualize the tree
    start_node = 'A'
    goal_node = 'K'
    bfs_result = best_first_search_tree(graph, start_node, goal_node)

    plt.figure(figsize=(10, 6))
    pos_tree = nx.spring_layout(bfs_result)
    nx.draw(bfs_result, pos_tree, with_labels=True, node_color='lightgreen', 
            node_size=500, font_size=12, font_weight='bold')
    edge_labels = nx.get_edge_attributes(bfs_result, 'weight')
    nx.draw_networkx_edge_labels(bfs_result, pos_tree, edge_labels=edge_labels)
    plt.title("Best First Search Tree")
    plt.show()
except Exception as e:
    print(f"An error occurred: {e}")
