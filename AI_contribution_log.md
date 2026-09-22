# Contribution Log

## Project
SLE-2: Empirical Performance Analysis

## Student Work

### Step 1: Problem Selection
Selected BFS and DFS for empirical performance comparison.

### Step 2: Graph Setup
Created a graph containing 800 nodes.

- Start Node: 0
- Goal Node: 799

The same graph was used for both BFS and DFS.

### Step 3: Algorithm Implementation
Implemented:

1. Breadth First Search (BFS)
2. Depth First Search (DFS)

Both algorithms record the number of nodes expanded and whether
the goal was found.

### Step 4: Performance Measurement
Execution time was measured in milliseconds.

Each algorithm was executed 3 times in one measurement cycle.

The following values were recorded:

- Run 1 time
- Run 2 time
- Run 3 time
- Average execution time
- Number of nodes expanded

### Step 5: Repeated Measurements
The measurement process was repeated multiple times to observe
variation in execution time.

The collected results showed that BFS and DFS both expanded
800 nodes.

### Step 6: Result Analysis
From the collected measurements:

- BFS average time across the repeated measurement cycles:
  approximately 102.08 ms
- DFS average time across the repeated measurement cycles:
  approximately 102.04 ms
- Average nodes expanded by BFS: 800
- Average nodes expanded by DFS: 800
- Goal found by BFS: True
- Goal found by DFS: True

The execution times were very close and varied slightly between
different runs.

### Step 7: Profiling Tool Attempt
py-spy was installed successfully and tested.

However, while running py-spy, the following error was received:

"Failed to find python version from target process"

Therefore, py-spy profiling data was not used as experimental
result data.

The final performance comparison is based on the actual execution
time measurements produced by the Python program.

## AI Contribution

AI was used for:

- Understanding the SLE-2 requirements
- Explaining BFS and DFS profiling
- Helping with terminal commands
- Helping organize experimental results
- Preparing the README file
- Preparing the contribution log
- Explaining errors encountered while setting up py-spy

AI did not generate or claim any untested experimental result.
The performance values reported in this project were obtained from
the student's local execution of the program.