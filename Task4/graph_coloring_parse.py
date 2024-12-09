from Task4.graph_coloring import GraphColoring
import os
import networkx as nx


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


def scale_edge_weights(space_graph, scale_range=(1, 10)):
    """
    Scales edge weights proportionally for visualization purposes.

    Parameters:
        space_graph (SpaceGraph): The graph object with adjacency list representation.
        scale_range (tuple): Range to scale edge weights, default is (1, 10).

    Returns:
        dict: A dictionary of scaled weights with (source, destination) as keys.
    """
    min_scale, max_scale = scale_range
    all_distances = [
        edge['distanceLY'] for edges in space_graph.graph.values() for edge in edges
    ]

    min_distance = min(all_distances)
    max_distance = max(all_distances)

    scaled_weights = {}
    for src, edges in space_graph.graph.items():
        for edge in edges:
            dest = edge['destination']
            original_weight = edge['distanceLY']
            # Scale the weight proportionally
            scaled_weight = (
                min_scale
                + (max_scale - min_scale)
                * (original_weight - min_distance)
                / (max_distance - min_distance)
            )
            scaled_weights[(src, dest)] = scaled_weight

    return scaled_weights


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

    Edge Attributes in GraphML:
        - weight: Scaled edge weight.

    Outputs:
        - Saves the colored graph to "Exports/colored_nodes.graphml".
    """
    graph_coloring = GraphColoring(space_graph)

    # Step 1: Find the minimum colors required and the coloring solution
    min_colors, solution = graph_coloring.find_min_colors()

    # Step 2: Map numerical colors to actual color codes
    color_mapping = map_colors()
    node_colors = {node: color_mapping[color - 1] for node, color in solution.items()}

    # Step 3: Print the solution if required
    if doPrint:
        print(f"Minimum number of colors required: {min_colors}")
        print("Coloring solution:")
        for node, color in solution.items():
            print(f"{node}: Color {color} ({node_colors[node]})")


    if export:
        # Step 4: Scale edge weights for visualization
        scaled_weights = scale_edge_weights(space_graph)

        # Step 5: Create NetworkX graph with correct attributes
        nx_graph = nx.Graph()

        for node, edges in space_graph.graph.items():
            # Add nodes with color and label attributes
            nx_graph.add_node(node, label=node, color=node_colors[node])

            # Add edges with scaled weights
            for edge in edges:
                dest = edge['destination']
                nx_graph.add_edge(
                    node,
                    dest,
                    weight=scaled_weights[(node, dest)],  # Scaled weight
                )

        # Save the GraphML file
        os.makedirs("Exports", exist_ok=True)
        output_path = os.path.join("Exports", "colored_nodes.graphml")
        nx.write_graphml(nx_graph, output_path)

