
# Final Project

This repository contains the implementation of a series of graph-based tasks for analyzing and solving various problems in space graph networks. The project is modular and follows a structured organization for clarity and scalability.

## **Project Structure**

```
final_project/
│
├── Exports/                       # Output directory for exported results
│
├── Graphs/                        # Utility functions and graph structure
│   ├── space_graph.py             # Class for creating and managing the graph structure
│   ├── utils.py                   # Helper functions for graph operations, file input
│
├── Task1/                         # Placeholder for Task 1
│
├── Task2/                         # Maximum Flow Graph Analysis
│   ├── maximum_flow_graph.py      # Core algorithm for maximum flow computation
│   ├── maximum_flow_parse.py      # Parsing and exporting maximum flow results
│
├── Task3/                         # Cosmic Diameter Calculation
│   ├── cosmic_diameter.py         # Algorithm for computing the cosmic diameter of the graph
│
├── Task4/                         # Graph Coloring
│   ├── graph_coloring.py          # Algorithm for finding the minimum graph coloring
│   ├── graph_coloring_parse.py    # Parsing and exporting graph coloring results
│
├── Task5/                         # Longest Loop Detection
│   ├── longest_loop.py            # Algorithm for detecting the longest loop in a graph
│   ├── longest_loop_parse.py      # Parsing and exporting longest loop results
│
├── actual_distances_space_graph.csv  # Input data representing the space graph with distances and hyperflow
│
├── main.py                        # Main entry point for running all tasks
│
├── report.md                      # Detailed project report
│
├── requirements.txt               # List of Python dependencies
│
└── .gitignore                     # Git ignore file for excluding unnecessary files
```

---

## **How to Run**

This structure ensures clarity, modularity, and reusability by separating tasks, centralizing shared utilities, and organizing outputs, making the project scalable and easy to manage.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/edimundos/final_project.git
   cd final_project
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Project**
   Execute the main script to perform all tasks:
   ```bash
   python main.py
   ```

   Individual tasks can also be executed by running specific modules within their respective directories.

---

## **Tasks Overview**

### **Task 1: Qunatum Maximum Flow**
- Creates Minimum spanning tree, by converting the given graph to undirected graph. It uses
- **Prims algorithm**: uses dijkstra/greedy type algorithm to loop through the nodes and edges to add to MST
- **Undirected graph development**: If edge exists both ways, take minimum of hyperflow, add edge both ways to undirected graph.
- Time complexity O(ElogE) - E - edges

### **Task 2: Maximum Flow**
- Uses Ford Fulkerson to get the Maximum Hyperflow - 724. It uses
- **Ford Fulkerson**: Assumes that every edge has capacity 0, uses dfs to loop until all the paths are found
- **Depth first search**: For every single neighbouring node, calculate residual capacity, If neighbour has not been visited and capacity is above 0, take minimum flow, recursively call dfs to get the result
- Time complexity: O(V*E^2) v- vertices, e - edges

### **Task 3: Cosmic Diameter**
- Calculates the longest shortest path by running dijkstra on all nodes and checking their path length. Diameter - 2537642.6. It uses:
- **Vertice loops**: For every vertice, get shortest paths using dijkstra, for every path check if it is the longest
- **Dijkstra**
- Time complexity dense graphs: O(V^3logV) 
- Time complexity sparse graphs: O(V^2logV) 

---

### **Task 4: Graph Coloring**

#### **Algorithm Analysis**
The graph coloring algorithm determines the minimum number of colors required to color a graph such that no two adjacent nodes share the same color. It uses:
- **Binary Search Optimization**: The algorithm efficiently narrows the search space for the minimum number of colors.
- **Backtracking**: Checks each possible coloring configuration recursively and ensures that no two adjacent nodes have the same color.

**Complexity:**
- **Time Complexity**: \( O(V * log(V) * max\_colors) \), where \( V \) is the number of nodes. The binary search narrows the range of colors, while the backtracking algorithm validates configurations.
- **Space Complexity**: \( O(V) \), for storing colors and the recursion stack.

#### **Output Analysis**
- **Output**: The minimum amount of colors needed for this exercise specifically is 4, with only 1 planet being colored in the color 4 (Earth) and 1 planet in color 3 (Mars). This result makes sense, because both of these planet nodes many have children some of which are also connected, as well as Earth and Mars are interconnected. 

- **Visualization**: The solution is exported as a **GraphML** file instead of a **GEXF** file as it support coloring for nodes:
  - **Node Attributes**: Each node has a unique color represented by a hex code.

---

### **Task 5: Longest Loop**

#### **Algorithm Analysis**
This algorithm identifies the longest cycle (loop) in an undirected graph, computing the total weight of the cycle:
- **Depth-First Search (DFS)**: Traverses the graph recursively, keeping track of visited nodes, paths, and weights.
- **Cycle Detection**: Uses a path-tracking mechanism to detect cycles and calculate their weights.

**Complexity:**
- **Time Complexity**: \( O(V * (V + E)) \), where \( V \) is the number of nodes and \( E \) is the number of edges. Each node and edge is explored multiple times to identify all possible cycles.
- **Space Complexity**: \( O(V + E) \), for storing the recursion stack, adjacency list, and the longest path.

#### **Output Analysis**
- **Output**: The longest cycle in this case is Earth - Arcturus - Andromeda, which could have also been found by manual search since the distance to Andromeda is over 2.5 million.
- **Visualization**: The solution is exported as a **GEXF** file:
  - **Node Attributes**: Nodes involved in the longest cycle.
  - **Edge Attributes**: Includes distances as weights. **Remark**: since the distance to Andromeda is so large, it is very hard to see with distances to scale

---

## **Exports Directory**
The `Exports` folder contains all outputs for visualization and analysis, such as:
- **GraphML and GEXF Files**: For importing into Gephi or other visualization tools.
- **PNGs**: Pre-rendered visualizations of graphs.

---

## **Data File**
The project uses the file `actual_distances_space_graph.csv` as the primary input, which contains:
- **Nodes**: Space entities like planets or stars.
- **Edges**: Connections with:
  - `distanceLY`: Distance in light-years.
  - `hyperflowSpiceMegaTons`: Flow capacity in MegaTons.

---

## **Dependencies**
The project uses the following Python libraries:
- `networkx`: For graph manipulation and export.
- `matplotlib`: For graph visualization.
- `gephi`: Recommended for detailed graph visualization (not directly used in the code).
- Additional utilities listed in `requirements.txt`.

---