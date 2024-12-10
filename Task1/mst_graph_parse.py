import random
import heapq
import os
from Graphs.utils import build_undirected_graph_hyperflow
from Graphs.space_graph import Space_graph
import networkx as nx


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




def develop_mst(graph, doPrint=False, export=False ):
    undirected_graph = build_undirected_graph_hyperflow(graph)
    mst_graph =prims_MST(undirected_graph)
    if doPrint:
        print_mst(mst_graph)
    if export:
        write_mst(mst_graph)


def print_mst(mst_graph):
    print("===============================================================")
    print("Quantum Minimum Spanning Tree")
    print(mst_graph)
    print("===============================================================")


def write_mst(mst_graph):

    nx_graph = nx.Graph()

    for node, edges in mst_graph.graph.items():
        nx_graph.add_node(node, label=node)  # Add node labels
        for edge in edges:
            nx_graph.add_edge(
                node,
                edge['destination'],
                weight=edge['hyperflowSpiceMegaTons']  # Assign distance as edge attribute
            )

    # Save the GEXF file
    gexf_filename = "mst.gexf"
    os.makedirs("Exports", exist_ok=True)
    path = os.path.join("Exports", gexf_filename)
    nx.write_gexf(nx_graph, path)
    print(f"MST exported to {path}")


    