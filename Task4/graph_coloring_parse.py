from Task4.graph_coloring import GraphColoring
import os
import networkx as nx
import matplotlib.pyplot as plt


def map_colors():
    """
    Returns a list of color codes to map numerical color values to real colors.
    """
    return [
        "#FF0000",  # Red
        "#00FF00",  # Green
        "#0000FF",  # Blue
        "#FFFF00",  # Yellow
        "#FF00FF",  # Magenta
        "#00FFFF",  # Cyan
        "#800080",  # Purple
        "#FFA500",  # Orange
        "#A52A2A",  # Brown
        "#808080",  # Gray
    ]


def findColoring(space_graph, doPrint=False, export=False):
    """
    Colors a graph using the minimum number of colors such that no two adjacent nodes share the same color.
    Optionally prints the result and exports the graph to a GraphML file.

    Parameters:
        space_graph (SpaceGraph): The graph object with adjacency list representation.
        doPrint (bool): If True, prints the coloring solution. Default is False.
        export (bool): If True, exports the colored graph to "Exports/colored_nodes.graphml". Default is False.

    Node Attributes in GraphML:
        - label: Node name.
        - color: Hexadecimal color code.

    Outputs:
        - Saves the colored graph to "Exports/colored_nodes.graphml".
    """
    graph_coloring = GraphColoring(space_graph)

    # Find the minimum colors required and the coloring solution
    min_colors, solution = graph_coloring.find_min_colors()

    # Map numerical colors to actual color codes
    color_mapping = map_colors()
    node_colors = {node: color_mapping[color - 1] for node, color in solution.items()}

    # Print the solution if required
    if doPrint:
        print(f"Minimum number of colors required: {min_colors}")
        print("Coloring solution:")
        for node, color in solution.items():
            print(f"{node}: Color {color} ({node_colors[node]})")


    nx_graph = nx.Graph()

    for node, edges in space_graph.graph.items():
        # Add nodes with color and label attributes
        nx_graph.add_node(node, label=node, color=node_colors[node])

        # Add edges
        for edge in edges:
            dest = edge['destination']
            nx_graph.add_edge(
                node,
                dest,
            )

    # Save the GraphML file
    os.makedirs("Exports", exist_ok=True)
    output_path = os.path.join("Exports", "colored_nodes.graphml")
    nx.write_graphml(nx_graph, output_path)

    if export:
        print(f"Graph exported to {output_path}")
