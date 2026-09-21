import collections
import random
import time

# Standard seed for reproducible graph structure
random.seed(42)

def generate_graph(num_nodes=1200):
    # Generating a large connected graph with 1200 nodes
    adj_matrix = {i: [] for i in range(num_nodes)}
    for i in range(num_nodes):
        # Connect each node to multiple other nodes to ensure execution time > 1 ms
        neighbors = set(random.sample(range(num_nodes), k=min(120, num_nodes - 1)))
        if i in neighbors:
            neighbors.remove(i)
        adj_matrix[i] = list(neighbors)
    return adj_matrix

def run_bfs(graph, start, goal):
    visited = set([start])
    queue = collections.deque([start])
    nodes_expanded = 0
    goal_found = False

    while queue:
        curr = queue.popleft()
        nodes_expanded += 1
        
        if curr == goal:
            goal_found = True

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return nodes_expanded, goal_found

def run_dfs(graph, start, goal):
    visited = set([start])
    stack = [start]
    nodes_expanded = 0
    goal_found = False

    while stack:
        curr = stack.pop()
        nodes_expanded += 1

        if curr == goal:
            goal_found = True

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return nodes_expanded, goal_found

def main():
    num_nodes = 1200
    start_node = 0
    goal_node = 1199
    num_runs = 3

    graph = generate_graph(num_nodes)

    bfs_times = []
    bfs_nodes = []
    bfs_found = False

    dfs_times = []
    dfs_nodes = []
    dfs_found = False

    # Collect BFS Runs
    for _ in range(num_runs):
        t_start = time.perf_counter()
        nodes, found = run_bfs(graph, start_node, goal_node)
        t_end = time.perf_counter()
        bfs_times.append((t_end - t_start) * 1000) # convert to ms
        bfs_nodes.append(nodes)
        bfs_found = found

    # Collect DFS Runs
    for _ in range(num_runs):
        t_start = time.perf_counter()
        nodes, found = run_dfs(graph, start_node, goal_node)
        t_end = time.perf_counter()
        dfs_times.append((t_end - t_start) * 1000) # convert to ms
        dfs_nodes.append(nodes)
        dfs_found = found

    avg_bfs_time = sum(bfs_times) / num_runs
    avg_dfs_time = sum(dfs_times) / num_runs
    avg_bfs_nodes = sum(bfs_nodes) / num_runs
    avg_dfs_nodes = sum(dfs_nodes) / num_runs

    # Formatting and Printing the exact output structure
    print("=" * 70)
    print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
    print("Comparison: BFS vs DFS")
    print("=" * 70)
    print()
    print("Problem:")
    print(f"Number of Nodes = {num_nodes}")
    print(f"Start Node      = {start_node}")
    print(f"Goal Node       = {goal_node}")
    print(f"Number of Runs  = {num_runs}")
    print()
    print("-" * 70)
    print("BFS - Breadth First Search")
    print("-" * 70)
    for i in range(num_runs):
        print(f"Run {i+1}: Time = {bfs_times[i]:.5f} ms, Nodes Expanded = {bfs_nodes[i]}")

    print()
    print("-" * 70)
    print("DFS - Depth First Search")
    print("-" * 70)
    for i in range(num_runs):
        print(f"Run {i+1}: Time = {dfs_times[i]:.5f} ms, Nodes Expanded = {dfs_nodes[i]}")

    print()
    print("=" * 70)
    print("FINAL COMPARISON")
    print("=" * 70)
    print(f"{'Metric':<32} {'BFS':<15} {'DFS':<15}")
    print("-" * 70)
    for i in range(num_runs):
        print(f"Run {i+1} Time (ms)                {bfs_times[i]:<15.5f} {dfs_times[i]:<15.5f}")
    print(f"Average Time (ms)               {avg_bfs_time:<15.5f} {avg_dfs_time:<15.5f}")
    print(f"Average Nodes Expanded          {avg_bfs_nodes:<15.2f} {avg_dfs_nodes:<15.2f}")
    print("-" * 70)
    print()
    
    time_winner = "BFS" if avg_bfs_time < avg_dfs_time else "DFS"
    nodes_winner = "BFS" if avg_bfs_nodes < avg_dfs_nodes else "DFS"

    print("Result based on actual measurements:")
    print(f"Better in Average Time   : {time_winner}")
    print(f"Fewer Nodes Expanded     : {nodes_winner}")
    print()
    print("Goal Found:")
    print(f"BFS : {bfs_found}")
    print(f"DFS : {dfs_found}")
    print()
    print("=" * 70)
    print("Profiling completed successfully.")
    print("=" * 70)

if __name__ == "__main__":
    main()