# 🤖 AI Algorithms Collection

This repository is a collection of classical Artificial Intelligence algorithms implemented in Python and Prolog. It's designed for learning and demonstration purposes, showcasing various problem-solving approaches in AI such as search strategies, game playing, heuristics, expert systems, and production systems.

## 📁 Contents

### Python Implementations
- `4_queens.py` – N-Queens problem using backtracking
- `bfs.py` – Breadth-First Search
- `dfs.py` – Depth-First Search
- `dijkstra.py` – Dijkstra’s shortest path algorithm
- `8_puzzle.py` – 8 Puzzle Solver using heuristic (A* or similar)
- `alpha_beta.py` – Alpha-Beta Pruning for game tree search
- `tictactoe_minmax.py` – Tic Tac Toe game with Minimax AI
- `tsp.py` – Travelling Salesman Problem (TSP) using heuristics

### Prolog Implementations
- `books.pl` – Production system for book classification
- `disease.pl` – Expert system for disease diagnosis

## 🧠 Topics Covered

| Topic               | Algorithms / Files                         |
|---------------------|--------------------------------------------|
| Search Strategies   | BFS, DFS, Dijkstra, 8 Puzzle               |
| Constraint Problems | N-Queens                                   |
| Game Playing        | Tic Tac Toe (Minimax), Alpha-Beta Pruning |
| Optimization        | Travelling Salesman Problem (TSP)          |
| Logic Programming   | Expert System (`disease.pl`), Production System (`books.pl`) |

## 🚀 How to Run

### Python Scripts
Make sure you have Python 3 installed.

```bash
python bfs.py
python dfs.py
python dijkstra.py
python 4_queens.py
python 8_puzzle.py
python alpha_beta.py
python tictactoe_minmax.py
python tsp.py

###Prolog
Make sure you have SWI-Prolog installed.

```bash
swipl
?- consult('disease.pl').
?- start. % or appropriate predicate for starting diagnosis

?- consult('books.pl').
?- classify. % or appropriate predicate for classification
