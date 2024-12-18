import heapq
import os
import networkx as nx

def dijkstra(start_node, space_graph):

    distances = {node: float('inf') for node in space_graph.graph.keys()} #Assume that 
    distances[start_node] = 0
    parents = {node: None for node in space_graph.graph.keys()}
    
    priority_queue = [(0, start_node)]  # Min-heap for shortest path; max-heap for longest path

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        for neighbor in space_graph.get_neighbors(current_node):
            weight = neighbor['distanceLY']
            
            new_distance = current_distance + weight
            if new_distance < distances[neighbor['destination']]:
                distances[neighbor['destination']] = new_distance
                parents[neighbor['destination']] = current_node
                heapq.heappush(priority_queue, (new_distance, neighbor['destination']))

    return distances, parents

def reconstruct_path( parents, end_node):
        """
        Reconstruct the path from start_node to end_node using the parent pointers.
        """
        path = []
        current = end_node
        while current is not None:
            path.append(current)
            current = parents[current]
        path.reverse()
        return path

def longest_shortest_path(space_graph, doPrint=True, export=True):

        max_distance = -float('inf')  # Start with the smallest possible value
        for start_node in space_graph.graph.keys():

            # Get all distances to all parents
            distances, parents = dijkstra(start_node, space_graph)
            
            for end_node in space_graph.graph.keys():
                if start_node != end_node and distances[end_node] != float('inf'):
                    # Check if this is the longest shortest path found so far
                    if distances[end_node] > max_distance:
                        max_distance = distances[end_node]
                        path = reconstruct_path(parents, end_node)
                        longest_path = {
                            'start_node': start_node,
                            'end_node': end_node,
                            'path': path,
                            'distance': distances[end_node]
                        }

        if doPrint:
             print_path(longest_path)
        
        if export:
             write_path(longest_path["path"])

def print_path(path):
    print("===============================================================")
    print(f"Path distance length: {round(path['distance'], 2)}")

    print(path)
    print("===============================================================")

def write_path(path):

    nx_graph = nx.Graph()
    previous=None

    for node in path:
        nx_graph.add_node(node, label=node)  # Add node labels
        if previous==None:
             previous=node
             continue
        
        nx_graph.add_edge(
            node,
            previous,
        )
        previous=node

    # Save the GEXF file
    gexf_filename = "cosmic_diameter.gexf"
    os.makedirs("Exports", exist_ok=True)
    path = os.path.join("Exports", gexf_filename)
    nx.write_gexf(nx_graph, path)
    print(f"Cosmic diameter exported to {path}")