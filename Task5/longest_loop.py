class LongestLoopDetector:
    def __init__(self, graph):
        """
        Initializes the LongestLoopDetector.
        :param graph: Adjacency list representation of the graph.
        """
        self.graph = graph
        self.visited = set()
        self.longest_loop = []
        self.max_weight = 0

    def dfs(self, current, parent, path, path_weight):
        """
        Depth-First Search to detect cycles and find the longest loop.
        :param current: Current node in DFS.
        :param parent: Parent node to avoid revisiting the immediate predecessor.
        :param path: List of nodes in the current path.
        :param path_weight: Total weight of the current path.
        """
        # Mark the current node as visited
        path.append(current)
        self.visited.add(current)

        for neighbor in self.graph[current]:
            neighbor_node = neighbor['destination']
            edge_weight = neighbor['distanceLY']  # Use 'distanceLY' as the weight

            if neighbor_node == parent:
                continue  # Skip the edge leading back to the parent

            if neighbor_node in path:  # Cycle detected
                # Extract the cycle from the path
                cycle_start_index = path.index(neighbor_node)
                cycle = path[cycle_start_index:] + [neighbor_node]
                cycle_weight = path_weight + edge_weight - self.get_path_weight(cycle[:-1])

                # Update the longest loop if this one is heavier
                if cycle_weight > self.max_weight:
                    self.max_weight = cycle_weight
                    self.longest_loop = cycle
            else:
                # Recursive DFS
                self.dfs(neighbor_node, current, path, path_weight + edge_weight)

        # Backtrack
        path.pop()

    def get_path_weight(self, path):
        """
        Calculate the total weight of a given path.
        :param path: List of nodes in the path.
        :return: Total weight of the path.
        """
        weight = 0
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i + 1]
            for neighbor in self.graph[current]:
                if neighbor['destination'] == next_node:
                    weight += neighbor['distanceLY']
                    break
        return weight

    def find_longest_loop(self):
        """
        Finds the longest loop in the graph.
        :return: Tuple of (sum of weights in the longest loop, longest loop as a graph).
        """
        for node in self.graph:
            if node not in self.visited:
                self.dfs(node, None, [], 0)

        # Convert the longest loop into a subgraph representation
        longest_loop_graph = self.loop_to_subgraph(self.longest_loop)

        return self.max_weight, longest_loop_graph

    def loop_to_subgraph(self, loop):
        """
        Converts a loop into a subgraph representation.
        :param loop: List of nodes in the loop.
        :return: Subgraph of the longest loop.
        """
        subgraph = {}
        for i in range(len(loop) - 1):
            node = loop[i]
            next_node = loop[i + 1]
            weight = self.get_edge_weight(node, next_node)

            if node not in subgraph:
                subgraph[node] = []
            if next_node not in subgraph:
                subgraph[next_node] = []

            subgraph[node].append({'destination': next_node, 'distanceLY': weight})
            subgraph[next_node].append({'destination': node, 'distanceLY': weight})
        return subgraph

    def get_edge_weight(self, node1, node2):
        """
        Retrieves the weight of the edge between two nodes.
        :param node1: First node.
        :param node2: Second node.
        :return: Weight of the edge.
        """
        for neighbor in self.graph[node1]:
            if neighbor['destination'] == node2:
                return neighbor['distanceLY']
        return 0
