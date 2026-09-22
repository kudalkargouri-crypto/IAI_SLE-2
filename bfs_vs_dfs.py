from collections import deque
import timeit

# ---------------------------------------------------------
# Create Graph
# ---------------------------------------------------------
NUM_NODES = 800
START = 0
GOAL = 799

graph = {}

for i in range(NUM_NODES):
    graph[i] = []

    for j in range(1, 5):
        if i + j < NUM_NODES:
            graph[i].append(i + j)


# ---------------------------------------------------------
# BFS
# ---------------------------------------------------------
def bfs():
    queue = deque([START])
    visited = {START}
    nodes_expanded = 0

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        # Actual computation
        checksum = 0

        for k in range(2000):
            checksum += (k * current) % 97

        if current == GOAL:
            return True, nodes_expanded

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False, nodes_expanded


# ---------------------------------------------------------
# DFS
# ---------------------------------------------------------
def dfs():
    stack = [START]
    visited = set()
    nodes_expanded = 0

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        # Actual computation
        checksum = 0

        for k in range(2000):
            checksum += (k * current) % 97

        if current == GOAL:
            return True, nodes_expanded

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append(neighbor)

    return False, nodes_expanded


# ---------------------------------------------------------
# Main Execution Strategy
# ---------------------------------------------------------
def execute_profiling():

    RUNS = 3

    print("=" * 70)
    print("SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
    print("Comparison: BFS vs DFS")
    print("=" * 70)

    print("\nProblem:")
    print("Number of Nodes =", NUM_NODES)
    print("Start Node      =", START)
    print("Goal Node       =", GOAL)
    print("Number of Runs  =", RUNS)


    # -----------------------------------------------------
    # BFS Profiling
    # -----------------------------------------------------

    print("\n" + "-" * 70)
    print("BFS - Breadth First Search")
    print("-" * 70)

    bfs_times = []
    bfs_nodes = []

    for i in range(RUNS):

        result = timeit.repeat(
            stmt="bfs()",
            globals=globals(),
            number=1,
            repeat=1
        )

        found, nodes = bfs()

        execution_time = result[0] * 1000

        bfs_times.append(execution_time)
        bfs_nodes.append(nodes)

        print(
            f"Run {i + 1}: Time = {execution_time:.5f} ms, "
            f"Nodes Expanded = {nodes}"
        )

    bfs_avg_time = sum(bfs_times) / RUNS
    bfs_avg_nodes = sum(bfs_nodes) / RUNS


    # -----------------------------------------------------
    # DFS Profiling
    # -----------------------------------------------------

    print("\n" + "-" * 70)
    print("DFS - Depth First Search")
    print("-" * 70)

    dfs_times = []
    dfs_nodes = []

    for i in range(RUNS):

        result = timeit.repeat(
            stmt="dfs()",
            globals=globals(),
            number=1,
            repeat=1
        )

        found, nodes = dfs()

        execution_time = result[0] * 1000

        dfs_times.append(execution_time)
        dfs_nodes.append(nodes)

        print(
            f"Run {i + 1}: Time = {execution_time:.5f} ms, "
            f"Nodes Expanded = {nodes}"
        )

    dfs_avg_time = sum(dfs_times) / RUNS
    dfs_avg_nodes = sum(dfs_nodes) / RUNS


    # -----------------------------------------------------
    # Final Comparison
    # -----------------------------------------------------

    print("\n" + "=" * 70)
    print("FINAL COMPARISON")
    print("=" * 70)

    print(
        f"{'Metric':40s}"
        f"{'BFS':>15s}"
        f"{'DFS':>15s}"
    )

    print("-" * 70)

    for i in range(RUNS):

        print(
            f"Run {i + 1} Time (ms)"
            f"{bfs_times[i]:>25.5f}"
            f"{dfs_times[i]:>15.5f}"
        )

    print(
        f"{'Average Time (ms)':40s}"
        f"{bfs_avg_time:>15.5f}"
        f"{dfs_avg_time:>15.5f}"
    )

    print(
        f"{'Average Nodes Expanded':40s}"
        f"{bfs_avg_nodes:>15.2f}"
        f"{dfs_avg_nodes:>15.2f}"
    )

    print("-" * 70)

    print("\nResult based on actual measurements:")

    if bfs_avg_time < dfs_avg_time:
        print("Better in Average Time   : BFS")
    else:
        print("Better in Average Time   : DFS")

    if bfs_avg_nodes < dfs_avg_nodes:
        print("Fewer Nodes Expanded     : BFS")
    else:
        print("Fewer Nodes Expanded     : DFS")


    # -----------------------------------------------------
    # Goal Test
    # -----------------------------------------------------

    bfs_found, _ = bfs()
    dfs_found, _ = dfs()

    print("\nGoal Found:")
    print("BFS :", bfs_found)
    print("DFS :", dfs_found)

    print("=" * 70)


# ---------------------------------------------------------
# Run Program
# ---------------------------------------------------------

if __name__ == "__main__":

    # Run multiple times for py-spy profiling
    for _ in range(10):
        execute_profiling()