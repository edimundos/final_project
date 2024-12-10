from Task5.longest_loop import LongestLoopDetector
import os
import networkx as nx

def findLongestPath(space_graph, doPrint=False, export=False):
 
    detector = LongestLoopDetector(space_graph.graph)

    # Find the longest loop
    max_weight, longest_loop_graph = detector.find_longest_loop()

    total_loop_length = 0
    visited_edges = set()  # To avoid counting the same edge twice

    for node, edges in longest_loop_graph.items():
        for edge in edges:
            # Use a tuple (source, destination) to identify unique edges
            edge_key = tuple(sorted([node, edge['destination']]))
            if edge_key not in visited_edges:
                total_loop_length += edge['distanceLY']
                visited_edges.add(edge_key)

    if doPrint:
        print(f"Total loop length (edge sum): {total_loop_length}")
        print("Longest loop as a graph:")
        for node, edges in longest_loop_graph.items():
            print(f"{node}: {edges}")
    if export:
        # Export the longest loop graph to GEXF
        nx_graph = nx.Graph()

        for node, edges in longest_loop_graph.items():
            nx_graph.add_node(node, label=node)  # Add node labels
            for edge in edges:
                nx_graph.add_edge(
                    node,
                    edge['destination'],
                    weight=edge['distanceLY']  # Assign distance as edge attribute
                )

        # Save the GEXF file
        gexf_filename = "longest_loop_graph.gexf"
        os.makedirs("Exports", exist_ok=True)
        path = os.path.join("Exports", gexf_filename)
        nx.write_gexf(nx_graph, path)
        print(f"Longest loop graph exported to {path}")

        nx.draw(nx_graph, with_labels=True)
        