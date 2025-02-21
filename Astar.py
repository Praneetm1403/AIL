#  A* Algorithm
import csv
import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Function to read the graph from CSV file
def read_graph_from_csv(file_path):
    graph = nx.DiGraph()
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            source, target, weight = row[0], row[1], int(row[2])
            graph.add_edge(source, target, weight=weight)
    return graph

# A* Algorithm Implementation
def a_star_search(graph, start, goal, heuristic):
    priority_queue = [(0, start)]  # Min-heap with (cost, node)
    g_costs = {start: 0}  # Cost from start to node
    came_from = {}  # Parent tracking

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, g_costs[goal]  # Return path and cost

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            new_g_cost = g_costs[current_node] + weight

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                f_cost = new_g_cost + heuristic.get(neighbor, float('inf'))
                heapq.heappush(priority_queue, (f_cost, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')  # No path found

# Function to visualize the graph
def visualize_graph(graph, title):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='black')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

# Define heuristic values (Modify for different cases)
heuristic1 = {'A': 7, 'B': 6, 'C': 4, 'D': 5, 'E': 2, 'F': 3, 'G': 0}  # Admissible heuristic
heuristic2 = {'A': 10, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 4, 'G': 3}  # Non-optimal heuristic

# Read graph and perform A* Search
file_path = r'C:\Users\Praneet\Desktop\AIL\Assignment3\edges.csv'
graph = read_graph_from_csv(file_path)

# Run A* with optimal heuristic
start_node, goal_node = 'A','G'
visualize_graph(graph, "Original Graph")
path, cost = a_star_search(graph, start_node, goal_node, heuristic1)
print(f"Optimal Path (Correct Heuristic): {path}, Cost: {cost}")

# Run A* with non-optimal heuristic
path, cost = a_star_search(graph, start_node, goal_node, heuristic2)
print(f"Non-Optimal Path (Wrong Heuristic): {path}, Cost: {cost}")
