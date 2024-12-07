import random
import heapq
import os
from Task1.mst_graph import MST_graph
    
    
def read_graph(graph):
    """
    Takes in graph dictionary as read in utils.py file and transforms it into MST graph
    """

    undirected_mst_graph=MST_graph()

    for key in graph:
        from_node =key[0]
        to_node=key[1]

        flipped_key =(to_node,from_node)
        if flipped_key in graph:

            #We take the minimum flow because it is the maximum that can be sent in both directions
            maxHyperFlow= min(graph[key]["hyperflowSpiceMegaTons"], graph[flipped_key]["hyperflowSpiceMegaTons"])

            #distance is the same in both directions, thus it doesnt matter which we choose
            distance =graph[key]["distanceLY"]

            # Cost is hyperflow and distance touple, since in prims algorithm uses priority queue, 
            # then elements will be evaluated by hyperflow first and then distance (if hyperflow is the same)
            undirected_mst_graph.add_edge(from_node, to_node, (maxHyperFlow, distance))
    
    return undirected_mst_graph


def prims_MST(current_graph):
    """
    Uses Prims algorithm to develop the MST graph
    """

    # Initialize a dictionary to track visited nodes
    visited = set()

    # Create a new Graph instance to hold the MST
    mst_graph = MST_graph()

    # Start with a random node, since MST doesnt require 
    start = random.choice(list(current_graph.adjacency_list.keys()))
    visited.add(start)
    priority_queue = []

    #Append random nodes neighbours to priority queue
    for neighbor, cost in current_graph.get_neighbours(start):
        heapq.heappush(priority_queue, (cost, start, neighbor))

    while priority_queue:
        cost, from_node, to_node =heapq.heappop(priority_queue)

        if to_node in visited:
            continue

        mst_graph.add_edge(from_node,to_node,cost)
        visited.add(to_node)

        # Append our latest nodes neighbours to priority queue
        for neighbor, cost in current_graph.get_neighbours(to_node):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost, to_node, neighbor))

    return mst_graph



def develop_mst(graph):
    undirected_graph = read_graph(graph)
    mst_graph =prims_MST(undirected_graph)
    return mst_graph


def print_mst(mst_graph):
    print("Quantum Minimum Spanning Tree")
    print("\"From-To\" \"Hyperflow cost\" \"Distance cost\"")
    for key in mst_graph.adjacency_list:
        connections =mst_graph.adjacency_list.get(key)
        for connection in connections:
            print(f"{key}-{connection[0]}: {connection[1][0]} {connection[1][1]}")

def write_mst(mst_graph):
    filename ="mst_graph.txt"
    os.makedirs("Exports", exist_ok=True)
    path = os.path.join("Exports", filename)
    with open(path, "w") as file:
        file.write(mst_graph.__str__())


    