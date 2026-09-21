# AI Contribution Log

## SLE-2: Empirical Performance Analysis


## 1. AI Tool Used :

**AI Tool:** ChatGPT 

ChatGPT was used as a supporting tool during the development, profiling, and documentation of the SLE-2 experiment.

---

## 2. Purpose of AI Assistance :

AI assistance was used to support the preparation of the BFS and DFS profiling implementation and to organize the experimental results and report.

---

## 3. Contribution of AI :

### Code Preparation

ChatGPT assisted with preparing the Python code for:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Graph creation
- Node counting
- Execution-time measurement
- Multiple experimental runs
- Average execution-time calculation

### Profiling Setup

ChatGPT assisted in setting up Python execution timers time.perf_counter for measuring the execution time of BFS and DFS.

Manual node counting was also included to measure the number of nodes expanded by each algorithm.

### Result Organization

ChatGPT helped organize the output into a comparison table containing:

- Run 1 execution time
- Run 2 execution time
- Run 3 execution time
- Average execution time
- Average nodes expanded
- Goal-found status

### Report Preparation

ChatGPT assisted in organizing the SLE-2 report into the required sections:

1. Algorithms / Versions Profiled
2. Profiling Method
3. Results
4. Justification & Analysis
5. AI Contribution Note
6. Conclusion

---

## 4. Student's Own Contribution :

The student:

- Understood the BFS and DFS algorithms.
- Reviewed and used the profiling code.
- Executed the program in VS Code.
- Ran both algorithms three times.
- Collected the actual execution results.
- Checked the goal-found status.
- Compared the measured execution times.
- Used the actual results for the final analysis.
- Prepared the final submission files.

---

## 5. Actual Experimental Results :

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | 7.21220 | 7.22400 |
| Run 2 Time (ms) | 6.41380 | 6.44370 |
| Run 3 Time (ms) | 5.53470 | 5.94520 |
| Average Time (ms) | 6.38690 | 6.53763 |
| Average Nodes Expanded | 1200 | 1200 |
| Goal Found | True | True |

---

## 6. Result Interpretation :

For the given graph and experimental setup, BFS had a lower average execution time than DFS.

The average execution time of BFS was 6.38690 ms, while DFS took 6.53763 ms.

Both algorithms expanded 1200 nodes and successfully found the goal node.

Therefore, the measured difference in this experiment was mainly in execution time.

---

## 7. AI Usage Statement :

AI was used as an assistance tool for code preparation, profiling setup, explanation, and report organization.

The actual program execution and collection of performance results were performed by the student.

The final comparison and analysis were based on the actual measured experimental results.

---

## 8. Declaration :

> I have used AI assistance transparently for the tasks mentioned above and have verified the experimental results obtained from my program.