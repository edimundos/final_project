import os
import networkx as nx
from Graphs.utils import build_directed_graph

def mf_dfs(graph, current_node, target_node, path_flow, flow_graph, visited=None):
    if visited is None:
        visited = set()

    if current_node == target_node:
        return path_flow
    visited.add(current_node)

    #loops through neighbours to calculate residual capacity which then is used to cehck flow
    for neighborEntry in graph.get_neighbors(current_node):
        # initializing actual values
        neighbor =  neighborEntry["destination"]
        capacity =  neighborEntry["hyperflowSpiceMegaTons"]

        #In case node is not in flow graph
        if neighbor not in flow_graph[current_node]:
            flow_graph[current_node][neighbor] = 0
        if current_node not in flow_graph[neighbor]:
            flow_graph[neighbor][current_node] = 0

        residual_capacity = capacity - flow_graph[current_node][neighbor]
        if neighbor not in visited and residual_capacity > 0:
            min_capacity = min(path_flow, residual_capacity)

            #recursively search for the target node
            result = mf_dfs(graph, neighbor, target_node, min_capacity, flow_graph, visited)
            if result > 0:
                flow_graph[current_node][neighbor] += result
                flow_graph[neighbor][current_node] -= result
                return result
    return 0

def ford_fulkerson_max_flow(space_graph, source, sink, doPrint=True, export=True):

    #initilize flow graph and set the capacity of edges to zero
    flow_graph = {node: {} for node in space_graph.graph}
    for u in space_graph.graph:
        for v in space_graph.graph[u]:
            v=v["destination"]
            flow_graph[u][v] = 0

    max_flow = 0

    #While havent looped through all of the proper paths to Target
    while True:
        path_flow = mf_dfs(space_graph, source, sink, float('Inf'), flow_graph, visited=set())
        if path_flow == 0:
            break
        max_flow += path_flow
    
    # Clean the flow graph to show only forward flows for readability
    cleaned_flow_graph = {
        u: {v: max(flow, 0) for v, flow in neighbors.items()}
        for u, neighbors in flow_graph.items()
    }

    if doPrint:
        print_flow(cleaned_flow_graph, max_flow)
    if export:
        write_flow_graph(cleaned_flow_graph)

def print_flow(flow_graph, max_flow):
    print("===============================================================")
    print(f"Maximum flow: {max_flow}")
    print(flow_graph)
    print("===============================================================")

def write_flow_graph(flow_graph):
    # Create a directed graph
    nx_graph = nx.DiGraph()

    # Add nodes and edges with weights
    for node, edges in flow_graph.items():
        nx_graph.add_node(node, label=node)  # Add node labels
        for key, weight in edges.items():
            if weight > 0:  # Only add edges with non-zero weights
                nx_graph.add_edge(
                    node,
                    key,
                    weight=weight  # Assign distance as edge attribute
                )

    # Save the GEXF file
    gexf_filename = "max_flow.gexf"
    os.makedirs("Exports", exist_ok=True)
    path = os.path.join("Exports", gexf_filename)
    nx.write_gexf(nx_graph, path)
    print(f"Max flow exported to {path}")
