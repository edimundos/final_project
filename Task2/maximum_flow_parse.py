from Task2.maximum_flow_graph import MF_graph

def mf_dfs(graph, current_node, target_node, path_flow, flow_graph, visited=None):
    if visited is None:
        visited = set()

    if current_node == target_node:
        return path_flow
    visited.add(current_node)

    for neighborEntry in graph.get_neighbors(current_node):
        neighbor =  neighborEntry["destination"]
        capacity =  neighborEntry["hyperflowSpiceMegaTons"]

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

def ford_fulkerson_max_flow(space_graph, source, sink):
    flow_graph = {node: {} for node in space_graph.graph}
    for u in space_graph.graph:
        for v in space_graph.graph[u]:
            v=v["destination"]
            flow_graph[u][v] = 0

    max_flow = 0

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

    return cleaned_flow_graph, max_flow