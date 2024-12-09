
# Final Project

This repository contains the implementation of a series of graph-based tasks for analyzing and solving various problems in space graph networks. The project is modular and follows a structured organization for clarity and scalability.

## **Project Structure**

```
final_project/
│
├── Exports/                       # Output directory for exported results
│   ├── colored_nodes.graphml      # GraphML file with colored nodes for Gephi visualization
│   ├── colored_space_graph.png    # PNG of the colored space graph
│   ├── longest_loop_graph.gexf    # GEXF file of the longest loop for Gephi
│   ├── longest_loop_graph.png     # PNG of the longest loop graph visualization
│   ├── mst_graph.txt              # Text representation of the MST graph
│
├── Graphs/                        # Utility functions and graph structure
│   ├── space_graph.py             # Class for creating and managing graph structures
│   ├── utils.py                   # Helper functions for graph operations
│
├── Task1/                         # Placeholder for Task 1 (future expansion)
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

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
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

### **Task 1: Placeholder**
- This folder is reserved for future project extensions.

### **Task 2: Maximum Flow**
- Calculates the maximum flow between nodes in the space graph.
- Includes:
  - **Core Algorithm**: `maximum_flow_graph.py`
  - **Results Parsing and Exporting**: `maximum_flow_parse.py`

### **Task 3: Cosmic Diameter**
- Computes the largest shortest path between any two nodes in the space graph (cosmic diameter).
- Implementation: `cosmic_diameter.py`

### **Task 4: Graph Coloring**
- Assigns colors to nodes such that no two adjacent nodes share the same color, minimizing the number of colors.
- Includes:
  - **Core Algorithm**: `graph_coloring.py`
  - **Results Parsing and Exporting**: `graph_coloring_parse.py`

### **Task 5: Longest Loop**
- Detects the longest cycle (loop) in the graph and computes its total weight.
- Includes:
  - **Core Algorithm**: `longest_loop.py`
  - **Results Parsing and Exporting**: `longest_loop_parse.py`

---

## **Exports Directory**
The `Exports` folder contains all outputs for visualization and analysis, such as:
- **GraphML and GEXF Files**: For importing into Gephi or other visualization tools.
- **PNGs**: Pre-rendered visualizations of graphs.
- **Text Files**: Simplified representations of graph structures.

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

## **Future Improvements**
- Extend Task 1 for additional graph analysis.
- Add dynamic graph visualizations.
- Optimize algorithms for larger datasets.
