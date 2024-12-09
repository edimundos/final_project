from Task2.maximum_flow_graph import MF_graph

def mf_dfs(graph, current_node, target_node, path_flow, flow_graph, visited=None):
    if visited is None:
        visited = set()

    if current_node == target_node:
        return path_flow
    visited.add(current_node)

    for neighbor, capacity in graph.get_neighbours(current_node):
        if neighbor not in flow_graph[current_node]:
            flow_graph[current_node][neighbor] = 0
        if current_node not in flow_graph[neighbor]:
            flow_graph[neighbor][current_node] = 0

        residual_capacity = capacity - flow_graph[current_node][neighbor]
        if neighbor not in visited and residual_capacity > 0:
            min_capacity = min(path_flow, residual_capacity)
            result = mf_dfs(graph, neighbor, target_node, min_capacity, flow_graph, visited)
            if result > 0:
                flow_graph[current_node][neighbor] += result
                flow_graph[neighbor][current_node] -= result
                return result
    return 0

def ford_fulkerson(graph, source, sink):
    flow_graph = {node: {} for node in graph.adjacency_list}
    for u in graph.adjacency_list:
        for v, _ in graph.adjacency_list[u]:
            flow_graph[u][v] = 0

    max_flow = 0

    while True:
        path_flow = mf_dfs(graph, source, sink, float('Inf'), flow_graph, visited=set())
        if path_flow == 0:
            break
        max_flow += path_flow

    return max_flow

def read_graph(graph):
    """
    Takes in graph dictionary as read in utils.py file and transforms it into MST graph
    """

    mf_graph=MF_graph()

    for key in graph:
        from_node =key[0]
        to_node=key[1]

    
    return mf_graph



def print_mf():
    graph = read_graph("canadian_cities.txt")
    print(ford_fulkerson(graph, "Argentia", "Inuvik"))

#main()