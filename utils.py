import csv
import os

class SpaceGraph:
    def __init__(self, data_dict):
        """
        Initialize the SpaceGraph with a dictionary of edges.
        Each edge is a tuple (source, destination) with attributes distanceLY and hyperflowSpiceMegaTons.
        """
        self.graph = {}
        self.build_graph(data_dict)

    def build_graph(self, data_dict):
        """
        Build the graph from the dictionary.
        The graph is stored as an adjacency list.
        """
        for (source, destination), attributes in data_dict.items():
            if source not in self.graph:
                self.graph[source] = []
            self.graph[source].append({
                'destination': destination,
                'distanceLY': attributes['distanceLY'],
                'hyperflowSpiceMegaTons': attributes['hyperflowSpiceMegaTons']
            })

    def get_neighbors(self, node):
        """
        Get all neighbors of a node along with edge attributes.
        """
        return self.graph.get(node, [])

    def display_graph(self):
        """
        Display the graph structure.
        """
        for node, edges in self.graph.items():
            print(f"{node}:")
            for edge in edges:
                print(f"  -> {edge['destination']} (distance: {edge['distanceLY']} LY, hyperflow: {edge['hyperflowSpiceMegaTons']} MT)")


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
