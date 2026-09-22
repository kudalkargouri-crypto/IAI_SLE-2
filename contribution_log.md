# AI CONTRIBUTION LOG

## SLE-2: Empirical Performance Analysis of BFS vs DFS

### Student Information

| Field                | Details                                    |
| -------------------- | ------------------------------------------ |
| Student Name         | Vaishnavi Punde                            |
| Experiment           | SLE-2                                      |
| Topic                | Empirical Performance Analysis: BFS vs DFS |
| Programming Language | Python                                     |
| Number of Nodes      | 800                                        |
| Start Node           | 0                                          |
| Goal Node            | 799                                        |

---

## 1. Purpose of AI Assistance

AI was used as an educational and development assistant during the SLE-2 experiment.

The purpose of AI assistance was to help understand:

* BFS implementation
* DFS implementation
* Graph representation
* Node expansion
* Execution-time measurement
* Repeated experimental runs
* `timeit` usage
* `py-spy` profiling
* Experimental result interpretation
* README preparation
* Contribution-log preparation

---

## 2. Student Contribution

The student performed the following activities:

* Understood the SLE-2 problem statement.
* Implemented/used the BFS algorithm.
* Implemented/used the DFS algorithm.
* Created the 800-node graph.
* Set the start node as 0.
* Set the goal node as 799.
* Ran the Python program in PowerShell.
* Performed multiple executions.
* Recorded the actual execution-time results.
* Checked the number of nodes expanded.
* Verified the goal-found result.
* Executed the `py-spy` profiling command.
* Reviewed the profiler output.
* Prepared the final project files.

---

## 3. AI-Assisted Activities

| Activity         | Contribution of AI                             |
| ---------------- | ---------------------------------------------- |
| BFS              | Explained BFS logic and queue-based traversal  |
| DFS              | Explained DFS logic and stack-based traversal  |
| Graph            | Explained graph creation and node connections  |
| Performance      | Explained execution-time measurement           |
| `timeit`         | Explained how `timeit` measures runtime        |
| Node Expansion   | Explained how expanded nodes are counted       |
| Repeated Runs    | Explained why multiple measurements are useful |
| `py-spy`         | Explained profiler command and output          |
| Documentation    | Helped organize README content                 |
| Contribution Log | Helped document AI-assisted activities         |

---

## 4. Actual Program Execution

The program was executed using:

```text
py bfs_vs_dfs.py
```

The program configuration was:

```text
Number of Nodes = 800
Start Node      = 0
Goal Node       = 799
Number of Runs  = 3
```

The `execute_profiling()` function was called 10 times:

```python
for _ in range(10):
    execute_profiling()
```

Therefore, the output contained 10 experimental sections.

---

## 5. Experimental Verification

The actual output was checked after running the program.

The recorded experiments showed:

```text
BFS : True
DFS : True
```

for the goal test.

The recorded node expansion values were:

```text
BFS = 800
DFS = 800
```

Therefore, both algorithms expanded 800 nodes in the recorded experiments.

---

## 6. Important Code Observation

The program contains:

```python
if bfs_avg_nodes < dfs_avg_nodes:
    print("Fewer Nodes Expanded     : BFS")
else:
    print("Fewer Nodes Expanded     : DFS")
```

When both values are 800, the condition:

```python
800 < 800
```

is false.

Therefore, the program prints:

```text
Fewer Nodes Expanded : DFS
```

even though both algorithms actually expanded the same number of nodes.

This was identified while interpreting the actual output.

---

## 7. Timing Measurement

The program uses Python's `timeit` module:

```python
result = timeit.repeat(
    stmt="bfs()",
    globals=globals(),
    number=1,
    repeat=1
)
```

and similarly for DFS.

The measured execution time is converted into milliseconds:

```python
execution_time = result[0] * 1000
```

The student observed that execution times varied between different runs.

---

## 8. Computational Workload

Both algorithms perform the same additional computation for every expanded node:

```python
checksum = 0

for k in range(2000):
    checksum += (k * current) % 97
```

This provides additional workload during the experiment.

The same workload is used for BFS and DFS to make the comparison consistent.

---

## 9. py-spy Contribution

The student executed:

```text
py-spy top -- python bfs_vs_dfs.py
```

The profiler reported:

```text
Python v3.14.6
Total Samples 2500
GIL: 0.00%
Active: 0.00%
Threads: 0
```

The profiler displayed interpreter and module-loading functions.

AI assistance was used to explain the meaning of the profiling output.

---

## 10. Learning Outcomes

The experiment helped the student understand:

1. BFS traversal using a queue.
2. DFS traversal using a stack.
3. Graph traversal using a visited set.
4. Counting expanded nodes.
5. Measuring execution time.
6. Performing repeated experiments.
7. Understanding runtime variation.
8. Using the `timeit` module.
9. Using `py-spy` for Python profiling.
10. Documenting empirical experimental results.
11. Using AI as an educational assistant.

---

## 11. AI Usage Statement

AI was used to support learning, explanation, debugging guidance, result interpretation, and documentation.

The actual program was executed by the student, and the experimental output was checked before being included in the project documentation.

The recorded timing and node-expansion values in the README are based on the actual program output.

---

## 12. Final Summary

The SLE-2 experiment was conducted using an 800-node graph to compare BFS and DFS.

The student executed the program multiple times, measured execution time, checked nodes expanded, verified goal finding, and used `py-spy` for runtime profiling.

AI assistance was used to understand the algorithms, performance measurement, profiling output, and documentation process.
