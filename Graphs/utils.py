import csv
import os

from Graphs.space_graph import Space_graph

def build_directed_graph(data_dict):
    """
    Build the graph from the dictionary.
    The graph is stored as an adjacency list.
    """

    graph = Space_graph()
    for (source, destination), attributes in data_dict.items():
        graph.add_edge(source, destination, attributes['hyperflowSpiceMegaTons'], attributes['distanceLY'] )

    return graph


def build_undirected_graph(data_dict):
    """
    Takes in graph dictionary and transforms it into undirected graph for MST graph development
    """

    undirected_mst_graph=Space_graph()

    for key in data_dict:
        from_node =key[0]
        to_node=key[1]

        flipped_key =(to_node,from_node)
        if flipped_key in data_dict:

            #We take the minimum flow because it is the maximum that can be sent in both directions
            maxHyperFlow= min(data_dict[key]["hyperflowSpiceMegaTons"], data_dict[flipped_key]["hyperflowSpiceMegaTons"])

            #distance is the same in both directions, thus it doesnt matter which we choose
            distance =data_dict[key]["distanceLY"]

            # Cost is hyperflow and distance touple, since in prims algorithm uses priority queue, 
            # then elements will be evaluated by hyperflow first and then distance (if hyperflow is the same)
            undirected_mst_graph.add_edge(from_node, to_node, maxHyperFlow, distance)
            undirected_mst_graph.add_edge(to_node, from_node, maxHyperFlow, distance)
    
    return undirected_mst_graph

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
