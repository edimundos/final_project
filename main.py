import csv
from space_graph import SpaceGraph
from graph_coloring import GraphColoring
from longest_loop import LongestLoopDetector

def main():

    data_dict = readFile("actual_distances_space_graph.csv")

    # Create a graph object
    space_graph = SpaceGraph(data_dict)

    # Display the graph
    # space_graph.display_graph()

    findColoring(space_graph, doPrint = True)

    findLongestPath(space_graph, doPrint=False)


def readFile(fileName):
    data_dict = {} #build dictionary in the format {(source, dest):{'distanceLY': 1.6e-05, 'hyperflowSpiceMegaTons': 131}}

    with open(fileName, mode='r') as file:
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
    return data_dict

def findLongestPath(space_graph, doPrint = False):
        # Create the LongestLoopDetector
    detector = LongestLoopDetector(space_graph.graph)

    # Find the longest loop
    max_weight, longest_loop_graph = detector.find_longest_loop()

    if doPrint:
        print(f"Sum of distances in the longest loop: {max_weight}")
        print("Longest loop as a graph:")
        for node, edges in longest_loop_graph.items():
            print(f"{node}: {edges}")

def findColoring(space_graph, doPrint = False):
    
    # Create the GraphColoring object
    graph_coloring = GraphColoring(space_graph)

    # Find the minimum colors required
    min_colors, solution = graph_coloring.find_min_colors()

    if doPrint:
        print(f"Minimum number of colors required: {min_colors}")
        print("Coloring solution:")
        for node, color in solution.items():
            print(f"{node}: Color {color}")



if __name__ == "__main__":
    main()