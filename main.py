import csv
from space_graph import SpaceGraph
from graph_coloring import GraphColoring

def main():

    data_dict = {} #build dictionary in the format {(source, dest):{'distanceLY': 1.6e-05, 'hyperflowSpiceMegaTons': 131}}

    with open("actual_distances_space_graph.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            source = row['source']
            destination = row['destination']
            distanceLY = float(row['distanceLY'])
            hyperflowSpiceMegaTons = int(row['hyperflowSpiceMegaTons'])
            # Add the data to the dictionary
            data_dict[(source, destination)] = {
                'distanceLY': distanceLY,
                'hyperflowSpiceMegaTons': hyperflowSpiceMegaTons
            }

    # Create a graph object
    space_graph = SpaceGraph(data_dict)

    # Display the graph
    space_graph.display_graph()

    # Create the GraphColoring object
    graph_coloring = GraphColoring(space_graph)

    # Find the minimum colors required
    min_colors, solution = graph_coloring.find_min_colors()

    # Print the result
    print(f"Minimum number of colors required: {min_colors}")
    print("Coloring solution:")
    for node, color in solution.items():
        print(f"{node}: Color {color}")


if __name__ == "__main__":
    main()