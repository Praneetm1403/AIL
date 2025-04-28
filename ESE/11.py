#A* Algorithm – Undirected Weighted Graph + Heuristic (User input)
import heapq

def input_graph_and_heuristic():
    graph = {}
    heuristic = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node: ")
        heuristic[node] = int(input(f"Enter heuristic for {node}: "))
        graph[node] = {}
        neighbors = int(input(f"Enter number of neighbors for {node}: "))
        for _ in range(neighbors):
            neighbor, weight = input("Enter neighbor and weight (e.g. B 3): ").split()
            graph[node][neighbor] = int(weight)
    return graph, heuristic

def a_star(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start)]
    visited = set()

    while open_list:
        est_total_cost, cost_so_far, node = heapq.heappop(open_list)
        if node in visited:
            continue
        print(node, end=' ')
        visited.add(node)
        if node == goal:
            break
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_cost = cost_so_far + weight
                heapq.heappush(open_list, (new_cost + heuristic[neighbor], new_cost, neighbor))

graph, heuristic = input_graph_and_heuristic()
start = input("Enter start node: ")
goal = input("Enter goal node: ")
print("A* Traversal:")
a_star(graph, heuristic, start, goal)
