from Task5.longest_loop import LongestLoopDetector
import os
import networkx as nx

def findLongestPath(space_graph, doPrint=False, export=False):
    """
    Finds the longest loop in the graph, optionally prints it, and exports the result as a GEXF file.

    Parameters:
        space_graph (SpaceGraph): The input graph in adjacency list format.
        doPrint (bool): If True, prints the longest loop and its total weight. Default is False.
        export (bool): If True, exports the longest loop as a GEXF file. Default is False.

    Outputs:
        - Prints the longest loop and its weight if doPrint=True.
        - Exports the longest loop graph to "Exports/longest_loop_graph.gexf" if export=True.

    GEXF Attributes:
        - Nodes:
            * label: Name of the node.
        - Edges:
            * distanceLY: Distance (weight) of the edge.
    """

    detector = LongestLoopDetector(space_graph.graph)
    max_weight, longest_loop_graph = detector.find_longest_loop()

    # Print the results if required.
    if doPrint:
        print(f"Sum of distances in the longest loop: {max_weight}")
        print("Longest loop as a graph:")
        for node, edges in longest_loop_graph.items():
            print(f"{node}: {edges}")

    # Export the graph as a GEXF file if required.
    if export:

        nx_graph = nx.Graph()

        # Add nodes and edges with attributes to the NetworkX graph.
        for node, edges in longest_loop_graph.items():
            nx_graph.add_node(node, label=node)
            for edge in edges:
                nx_graph.add_edge(
                    node,
                    edge['destination'],
                    weight=edge['distanceLY'] 
                )

        os.makedirs("Exports", exist_ok=True)
        gexf_filename = "longest_loop_graph.gexf"
        path = os.path.join("Exports", gexf_filename)
        
        nx.write_gexf(nx_graph, path)
        print(f"Longest loop graph exported to {path}")
