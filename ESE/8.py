# A* Algorithm – Directed Weighted Graph + Heuristic (CSV File)
import pandas as pd
import heapq

# Read graph and heuristic from CSV files
graph_df = pd.read_csv('graph.csv', index_col=0)
heuristic_df = pd.read_csv('heuristic.csv', index_col=0)

def build_graph(df):
    graph = {}
    for i in df.index:
        graph[i] = {}
        for j in df.columns:
            if df.loc[i, j] != 0:
                graph[i][j] = df.loc[i, j]
    return graph

def build_heuristic(df):
    return {i: int(df.loc[i][0]) for i in df.index}

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
                heapq.heappush(open_list, (cost_so_far + weight + heuristic[neighbor], cost_so_far + weight, neighbor))

graph = build_graph(graph_df)
heuristic = build_heuristic(heuristic_df)
start = input("Enter start node: ")
goal = input("Enter goal node: ")
print("A* Traversal:")
a_star(graph, heuristic, start, goal)
