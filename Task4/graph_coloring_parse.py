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

def findColoring(space_graph, doPrint=False, export=False):
    # Create the GraphColoring object
    graph_coloring = GraphColoring(space_graph)

    # Find the minimum colors required
    min_colors, solution = graph_coloring.find_min_colors()

    # Map numerical colors to actual color codes
    color_mapping = map_colors()
    node_colors = {node: color_mapping[color - 1] for node, color in solution.items()}

    if doPrint:
        print(f"Minimum number of colors required: {min_colors}")
        print("Coloring solution:")
        for node, color in solution.items():
            print(f"{node}: Color {color} ({node_colors[node]})")

    if export:
        # Export the colored graph to GEXF
        nx_graph = nx.Graph()

        for node, edges in space_graph.graph.items():
            # Add nodes with mapped colors as attributes
            nx_graph.add_node(
                node,
                label=node,  # Set node label as the node name
                color=node_colors.get(node, "#000000"),  # Default to black if no color assigned
            )

            # Add edges with distances
            for edge in edges:
                nx_graph.add_edge(
                    node,
                    edge['destination'],
                    distanceLY=edge['distanceLY'],  # Assign the distance attribute
                )

        # Save the GEXF file
        gexf_filename = "colored_space_graph.gexf"
        os.makedirs("Exports", exist_ok=True)
        path = os.path.join("Exports", gexf_filename)
        nx.write_gexf(nx_graph, path)
        print(f"Colored graph exported to {path}")

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
