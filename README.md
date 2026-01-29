# Maze Solver with A* and DFS

This repository contains an academic project developed for the Artificial Intelligence course in my Bachelor’s degree in Computer Science.  
The project focuses on applying classical search algorithms to solve a maze problem and analyzing their performance.

---

## Project Overview

The application generates a random maze, models it as a graph, and applies different search algorithms to find a path from the entrance to the exit.

Two algorithms are implemented and compared:
- A* Search (informed search)
- Depth-First Search (DFS) (uninformed search)

The solution path can be visualized through a graphical interface built with Pygame.

---

## Objectives

- Apply Artificial Intelligence search algorithms in a practical scenario
- Represent a maze as a graph structure
- Compare informed and uninformed search strategies
- Measure algorithm performance based on execution time and visited nodes
- Reinforce algorithmic reasoning and structured programming

---

## Features

- Random maze generation using recursive backtracking
- Conversion of the maze into a graph
- Implementation of A* Search with Manhattan distance heuristic
- Implementation of Depth-First Search (DFS)
- Performance comparison between algorithms
- Visualization of the maze and the solution path using Pygame
- Modular and readable code structure

---

## Technologies Used

- Python
- Pygame
- Graph-based data structures
- Priority Queue (heapq)
- Object-Oriented Programming concepts

---

## Algorithms

### A* Search

A* is an informed search algorithm that uses a heuristic function to guide the search process.  
In this project, the Manhattan distance heuristic is used, ensuring efficient exploration and guaranteeing the shortest path in the maze.

### Depth-First Search (DFS)

DFS is an uninformed search algorithm that explores paths deeply before backtracking.  
Although it does not guarantee the shortest path, it serves as a useful baseline for comparison.

---

## Performance Evaluation

The program measures and displays the following metrics:
- Execution time
- Number of visited nodes

Example output:

=== Comparison ===
A*: Time = 0.00231s | Visited nodes = 214
DFS: Time = 0.00487s | Visited nodes = 623

---

## How to Run

1. Clone this repository
2. Install the required dependency: pip install pygame
3. Run the project: python Labirinto.py

---

## Academic Context

This project was developed as part of an undergraduate Artificial Intelligence course in Computer Science.

It demonstrates the ability to:
- Apply theoretical AI concepts in practice
- Design and analyze search algorithms
- Work with graph representations
- Evaluate computational efficiency

---

## Project Relevance

Search algorithms are fundamental in areas such as:
- Game development
- Robotics
- Pathfinding systems
- Optimization problems
- Decision-making systems

This project reflects my interest in Artificial Intelligence, algorithmic problem-solving, and efficient system design.

---

## Author

Laura Tamarozzi  
Bachelor’s Degree in Computer Science
