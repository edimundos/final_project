import csv
from graphing import SpaceGraph

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

    # Example: Get neighbors of 'Earth'
    neighbors = space_graph.get_neighbors('Earth')
    print("\nNeighbors of Earth:")
    for neighbor in neighbors:
        print(neighbor)

if __name__ == "__main__":
    main()