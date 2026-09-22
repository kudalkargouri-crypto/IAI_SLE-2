# SLE-2: Empirical Performance Analysis

## Project Title
Empirical Performance Analysis of BFS and DFS

## Objective
The objective of this project is to compare the real performance of
Breadth First Search (BFS) and Depth First Search (DFS) by measuring
execution time and the number of nodes expanded.

## Problem Description
A graph containing 800 nodes was used for the experiment.

- Number of Nodes: 800
- Start Node: 0
- Goal Node: 799
- Algorithms Compared: BFS and DFS
- Runs per execution: 3

Both algorithms were tested on the same graph and with the same
start and goal nodes.

## Algorithms Used

### 1. Breadth First Search (BFS)
BFS explores the graph level by level. It uses a queue to store
nodes that have to be explored.

### 2. Depth First Search (DFS)
DFS explores a path as deeply as possible before backtracking.
It uses a stack to store nodes that have to be explored.

## Performance Measurement

The execution time of both algorithms was measured in milliseconds.
Each execution performed 3 runs for BFS and 3 runs for DFS.

The number of expanded nodes was also recorded.

The experiment was repeated multiple times to observe variation
in execution time.

## Results

The program consistently expanded:

| Metric | BFS | DFS |
|---|---:|---:|
| Nodes Expanded | 800 | 800 |
| Goal Found | True | True |

The average execution time varied slightly between repeated
measurements because execution time can change due to system
conditions.

Across the repeated measurements collected during the experiment,
the average of the reported 3-run averages was approximately:

| Algorithm | Average Time |
|---|---:|
| BFS | 102.08 ms |
| DFS | 102.04 ms |

These values are empirical measurements from the experiment.

## Observation

1. Both BFS and DFS successfully found the goal node.
2. Both algorithms expanded 800 nodes in this particular graph.
3. The execution time of BFS and DFS was very close.
4. The measured time changed slightly between repeated executions.
5. Therefore, the experimental results show that the two algorithms
   had very similar performance for this particular test case.

## Conclusion

The experiment successfully measured the real execution performance
of BFS and DFS on the same graph.

For this test case, both algorithms expanded the same number of nodes,
800, and both successfully found the goal node. Their measured
execution times were also very close.

The experiment shows that theoretical complexity and actual execution
time are different aspects of algorithm performance. Real execution
time can vary depending on the test case and system conditions.

## Tools and Technologies

- Python
- VS Code
- timeit / execution-time measurement
- py-spy was installed and tested, but profiling could not be
  completed because py-spy could not detect the Python version of
  the target process.

## AI Contribution

AI was used to understand the SLE-2 requirements, structure the
README and contribution log, explain the profiling process, and
assist in organizing the experimental results.

The BFS and DFS implementation and the reported performance values
were tested in the local Python environment.