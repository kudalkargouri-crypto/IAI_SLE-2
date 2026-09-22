# SLE-2: Empirical Performance Analysis of BFS vs DFS

## 1. Experiment Title

**Empirical Performance Analysis: Comparison of BFS and DFS**

## 2. Objective

The objective of this experiment is to compare the empirical performance of Breadth First Search (BFS) and Depth First Search (DFS) using:

* Execution time
* Number of nodes expanded
* Goal-finding result
* Runtime profiling using `py-spy`

## 3. Problem Description

A directed graph with **800 nodes** is created.

The experiment uses:

* **Start Node:** 0
* **Goal Node:** 799
* **Number of Nodes:** 800
* **Runs per execution:** 3
* **Number of executions:** 10

Each node is connected to up to the next four nodes.

For example:

```text
0 → 1, 2, 3, 4
1 → 2, 3, 4, 5
2 → 3, 4, 5, 6
...
```

## 4. Algorithms Used

### Breadth First Search (BFS)

BFS uses a queue implemented using Python's `deque`.

The algorithm:

1. Starts from node 0.
2. Adds the start node to the queue.
3. Removes nodes from the front of the queue.
4. Marks nodes as visited.
5. Expands their neighbouring nodes.
6. Continues until the goal node is found.

### Depth First Search (DFS)

DFS uses a Python list as a stack.

The algorithm:

1. Starts from node 0.
2. Pushes the start node onto the stack.
3. Removes the last node from the stack.
4. Marks the node as visited.
5. Adds unvisited neighbours to the stack.
6. Continues until the goal node is found.

## 5. Computational Workload

To make the execution measurable, both BFS and DFS perform an additional computation for every expanded node:

```python
checksum = 0

for k in range(2000):
    checksum += (k * current) % 97
```

This computation is executed equally by both algorithms.

Therefore, the experiment measures the runtime of both search algorithms under the same computational workload.

## 6. Performance Measurement

Python's `timeit` module is used to measure execution time.

The measured time is converted from seconds to milliseconds:

```python
execution_time = result[0] * 1000
```

Each algorithm is executed **3 times per experiment**.

The average time is calculated as:

```python
average_time = sum(times) / RUNS
```

## 7. Experimental Configuration

| Parameter                  |           Value |
| -------------------------- | --------------: |
| Number of Nodes            |             800 |
| Start Node                 |               0 |
| Goal Node                  |             799 |
| Neighbours per Node        |         Up to 4 |
| Runs per Execution         |               3 |
| Total Executions           |              10 |
| Workload per Expanded Node | 2000 iterations |
| Search Algorithms          |     BFS and DFS |

## 8. Actual Experimental Results

The program was executed multiple times.

The recorded results showed that:

* BFS successfully found the goal.
* DFS successfully found the goal.
* BFS expanded 800 nodes.
* DFS expanded 800 nodes.
* Execution time varied between different executions.
* In several executions BFS had a lower average execution time.
* In some executions DFS had a lower average execution time.

### Sample Recorded Result

One of the recorded executions produced:

| Metric                 |       BFS |       DFS |
| ---------------------- | --------: | --------: |
| Run 1 Time (ms)        | 199.16290 | 239.01670 |
| Run 2 Time (ms)        | 200.62450 | 209.55760 |
| Run 3 Time (ms)        | 170.41510 | 219.19510 |
| Average Time (ms)      | 190.06750 | 222.58980 |
| Average Nodes Expanded |    800.00 |    800.00 |
| Goal Found             |      True |      True |

Another recorded execution produced:

| Metric                 |       BFS |       DFS |
| ---------------------- | --------: | --------: |
| Average Time (ms)      | 201.54920 | 192.64657 |
| Average Nodes Expanded |    800.00 |    800.00 |
| Goal Found             |      True |      True |

This demonstrates that execution time can vary between repeated measurements.

## 9. Nodes Expanded

In the recorded experiments, both algorithms expanded all 800 nodes:

```text
BFS Average Nodes Expanded = 800.00
DFS Average Nodes Expanded = 800.00
```

The program's comparison section may display:

```text
Fewer Nodes Expanded     : DFS
```

when the values are equal because of the `if/else` logic:

```python
if bfs_avg_nodes < dfs_avg_nodes:
    print("Fewer Nodes Expanded     : BFS")
else:
    print("Fewer Nodes Expanded     : DFS")
```

Since:

```text
800.00 < 800.00
```

is false, the `else` statement prints DFS.

Therefore, this output does **not** mean DFS actually expanded fewer nodes. Both expanded 800 nodes.

## 10. Goal Test

The program checks whether both algorithms find the goal:

```python
bfs_found, _ = bfs()
dfs_found, _ = dfs()
```

The recorded output was:

```text
Goal Found:
BFS : True
DFS : True
```

Therefore, both algorithms successfully reached node 799.

## 11. py-spy Profiling

Runtime profiling was performed using:

```text
py-spy top -- python bfs_vs_dfs.py
```

The profiler reported:

```text
Collecting samples from '"python" bfs_vs_dfs.py' (python v3.14.6)
Total Samples 2500
GIL: 0.00%, Active: 0.00%, Threads: 0
```

The profiler displayed Python interpreter and module-loading functions such as:

* `_get_data`
* `spec_from_file_location`
* `convert_class`
* `namedtuple`
* `find_spec`
* `_find_and_load`
* `exec_module`

The profiling command successfully monitored the Python program during execution.

## 12. Observation

The experiment demonstrates that empirical execution times are not necessarily identical across repeated executions.

Possible reasons for variation include:

* Operating-system scheduling
* Background processes
* CPU activity
* Python interpreter overhead
* Memory activity
* System load

Therefore, multiple runs were performed instead of relying on a single measurement.

## 13. Conclusion

The SLE-2 experiment successfully compared BFS and DFS on an 800-node graph.

The main observations are:

1. Both BFS and DFS successfully found the goal node 799.
2. Both algorithms expanded 800 nodes in the recorded experiments.
3. Execution times varied between different runs.
4. BFS had a lower average time in several executions.
5. DFS had a lower average time in some executions.
6. The experiment used the same additional computational workload for both algorithms.
7. `timeit` was used for execution-time measurement.
8. `py-spy` was used for runtime profiling.

The experiment demonstrates how empirical performance can be evaluated through repeated measurements and runtime profiling.

## 14. Technologies Used

* Pyth
