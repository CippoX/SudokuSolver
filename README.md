# SUDOKU SOLVER USING BACKTRACKING AND SIMULATED ANNEALING

**Ca’ Foscari University of Venice**  
Master’s Degree in Computer Science and Information Technology  

[LM-18]  
Palmisano Tommaso, 886825  



## I. Abstract

Due to how it is formulated, solving a sudoku puzzle is a problem often used to explain Constraint Satisfaction Problems. Each cell represents a variable with specific constraints, such as ensuring no duplicate numbers in the same row, column, or 3x3 square. This projet illustrates how to solve sudoku using Constraint Satisfaction Problem solving techniques like Backtracking and Simulated Annealing.


## II. Introduction

Sudoku is a popular game where the goal is to fill a 9x9 grid with numbers from 1 to 9 such that each row, column, and 3x3 square contains no duplicate numbers.



## III. Solving a CSP

Each variable is treated as a node, and each constraint as an arc between states, allowing the use of constraint propagation. Ensuring arc-consistency between nodes helps solve CSPs.

- **X**: Sudoku cells, representing 81 variables.
- **D**: Possible values for each cell, {1, 2, ..., 9}.
- **C**: Constraints that ensure unique values in rows, columns, and 3x3 squares.

The AC-3 algorithm ensures arc-consistency and helps solve simple sudokus or reduce domain values for complex ones.

Backtracking involves Depth First Search to explore possible assignments, discarding inconsistent states, which improves performance and reduces memory usage.

Testing with various difficulty levels on a MacBook Air M1 demonstrated a significant performance gain using AC-3, reducing execution time across all levels.



## IV. Statistical Approach: Simulated Annealing

Simulated Annealing transforms a CSP into an optimization problem by minimizing an objective function.

Simulated Annealing uses:
- An objective function `f(x)` representing the cost of a state.
- A temperature function with a starting temperature and decay factor.
- A random starting state close to the solution.

The acceptance probability function allows for controlled randomness, aiding in escaping local optima. It is calculated as:

```math
P = e^{-\Delta / T}
```
\
where `Δ` is the difference in cost between the current and a candidate new current state, and `T` is the current temperature. The sudoku is represented by an array of arrays where empty cells are `0`, and the algorithm iteratively refines the state.

Simulated Annealing proved less efficient, heavily influenced by the number of empty cells in a puzzle.



## V. Conclusions

The study explored two approaches for solving Sudoku puzzles: backtracking and simulated annealing. Backtracking with constraint propagation demonstrated efficiency across all levels. Simulated annealing, while useful for CSPs with fewer constraints, was less effective for Sudoku due to the increased time requirements. In conclusion, backtracking with constraint propagation is the most effective approach for Sudoku puzzles.



## References

1. Stuart Russell and Peter Norvig. *Artificial Intelligence: A Modern Approach*. Prentice Hall, 3rd Edition, 201
2. Challenging Luck. Simulated annealing explained by solving sudoku - artificial intelligence.
3. Daniel Delahaye, Supatcha Chaimatanan, and Marcel Mongeau. Simulated an- nealing: From basics to applications. In Michel Gendreau and Jean-Yves Potvin, editors, Handbook of Metaheuristics, volume 272 of International Series in Op- erations Research & Management Science (ISOR), pages 1–35. Springer, 2019.
