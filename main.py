import csv
import networkx as nx
from space_graph import SpaceGraph
from graph_coloring import GraphColoring
from longest_loop import LongestLoopDetector
import os


def main():
    data_dict = readFile("actual_distances_space_graph.csv")
    # print(data_dict)

    # mst_graph = develop_mst(data_dict)
    #print_mst(mst_graph)
    #write_mst(mst_graph)
    

    # Create a graph object
    space_graph = SpaceGraph(data_dict)

    # Display the graph
    space_graph.display_graph()

    findColoring(space_graph, doPrint=True, export=True)

    findLongestPath(space_graph, doPrint=False, export=True)


def readFile(fileName):
    """
    Reads a CSV file and constructs a dictionary representing the space graph.
    Handles scientific notation and invalid data gracefully.
    """
    data_dict = {}  # Build dictionary in the format {(source, dest): {'distanceLY': ..., 'hyperflowSpiceMegaTons': ...}}

    with open(fileName, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                source = row['source']
                destination = row['destination']
                # Ensure distanceLY is parsed as a float
                distanceLY = float(row['distanceLY'])
                # Ensure hyperflowSpiceMegaTons is parsed as an integer
                hyperflowSpiceMegaTons = int(row['hyperflowSpiceMegaTons'])
                
                # Add the data to the dictionary
                data_dict[(source, destination)] = {
                    'distanceLY': distanceLY,
                    'hyperflowSpiceMegaTons': hyperflowSpiceMegaTons
                }
            except KeyError as e:
                print(f"Missing column in data: {e}")
            except ValueError as e:
                print(f"Invalid data format in row: {row} - {e}")
    
    return data_dict


def findLongestPath(space_graph, doPrint=False, export=False):
    # Create the LongestLoopDetector
    detector = LongestLoopDetector(space_graph.graph)

    # Find the longest loop
    max_weight, longest_loop_graph = detector.find_longest_loop()

    if doPrint:
        print(f"Sum of distances in the longest loop: {max_weight}")
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
                    distanceLY=edge['distanceLY']  # Assign distance as edge attribute
                )

        # Save the GEXF file
        gexf_filename = "longest_loop_graph.gexf"
        os.makedirs("Exports", exist_ok=True)
        path = os.path.join("Exports", gexf_filename)
        nx.write_gexf(nx_graph, path)
        print(f"Longest loop graph exported to {path}")

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




if __name__ == "__main__":
    main()
