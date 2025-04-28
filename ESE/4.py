# 4. Best First Search – Directed unweighted graph + heuristic from user
import heapq

# Input graph and heuristic
def input_graph_and_heuristic():
    graph = {}
    heuristic = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        graph[node] = neighbors
        heuristic[node] = int(input(f"Enter heuristic value for {node}: "))
    return graph, heuristic

# Best First Search
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

# Run the code
graph, heuristic = input_graph_and_heuristic()
start = input("Enter start node: ")
goal = input("Enter goal node: ")
print("Best First Search Path:")
best_first_search(graph, heuristic, start, goal)
