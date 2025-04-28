#Best First Search – Directed Weighted Graph + Heuristic (User)
import heapq

def input_graph_and_heuristic():
    graph = {}
    heuristic = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node: ")
        heuristic[node] = int(input(f"Enter heuristic for {node}: "))
        graph[node] = {}
        num_neighbors = int(input(f"Enter number of neighbors of {node}: "))
        for _ in range(num_neighbors):
            neighbor, weight = input("Enter neighbor and weight (e.g., B 2): ").split()
            graph[node][neighbor] = int(weight)
    return graph, heuristic

def best_first_search(graph, heuristic, start, goal):
    visited = set()
    pq = [(heuristic[start], start)]

    while pq:
        _, current = heapq.heappop(pq)
        if current in visited:
            continue
        print(current, end=' ')
        visited.add(current)
        if current == goal:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor))

graph, heuristic = input_graph_and_heuristic()
start = input("Enter start node: ")
goal = input("Enter goal node: ")
print("Best First Search Traversal:")
best_first_search(graph, heuristic, start, goal)
