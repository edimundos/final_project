import random
import heapq
import os
from Graphs.utils import build_undirected_graph
from Graphs.space_graph import Space_graph


def prims_MST(current_graph):
    """
    Uses Prims algorithm to develop the MST graph
    """

    # Initialize a dictionary to track visited nodes
    visited = set()

    # Create a new Graph instance to hold the MST
    mst_graph = Space_graph()

    # Start with a random node, since MST doesnt require 
    start = random.choice(list(current_graph.graph.keys()))
    visited.add(start)
    priority_queue = []

    #Append random nodes neighbours to priority queue
    for node in current_graph.get_neighbors(start):
        neighbor=node["destination"]
        cost=(node["hyperflowSpiceMegaTons"], node["distanceLY"])
        heapq.heappush(priority_queue, (cost, start, neighbor))

    while priority_queue:
        cost, from_node, to_node =heapq.heappop(priority_queue)

        if to_node in visited:
            continue

        #since we construct undirected graph we need edges going both ways
        mst_graph.add_edge(from_node,to_node,cost[0], cost[1])
        mst_graph.add_edge(to_node,from_node,cost[0], cost[1])

        visited.add(to_node)

        # Append our latest nodes neighbours to priority queue
        for node in current_graph.get_neighbors(to_node):
            neighbor=node["destination"]
            cost=(node["hyperflowSpiceMegaTons"], node["distanceLY"])

            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost, to_node, neighbor))

    return mst_graph



def develop_mst(graph):
    undirected_graph = build_undirected_graph(graph)
    mst_graph =prims_MST(undirected_graph)
    return mst_graph


def print_mst(mst_graph):
    print("===============================================================")
    print("Quantum Minimum Spanning Tree")
    print(mst_graph)
    print("===============================================================")


#TODO save in GEFX
def write_mst(mst_graph):

    filename ="mst_graph.txt"
    os.makedirs("Exports", exist_ok=True)
    path = os.path.join("Exports", filename)
    with open(path, "w") as file:
        file.write(mst_graph.__str__())


    