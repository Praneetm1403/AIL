# Function to take graph input from user
# Non-Recursive DFS – Read undirected unweighted graph from user
def input_graph():
    graph = {}
    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        graph[node] = neighbors
    return graph

# Non-recursive DFS using stack
def dfs_non_recursive(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add neighbors in reverse to mimic recursion order
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

# Run the code
graph = input_graph()
start_node = input("Enter start node: ")
print("DFS Traversal:")
dfs_non_recursive(graph, start_node)
