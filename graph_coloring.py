# Graph Coloring Algorithm
# Inspired by: https://www.geeksforgeeks.org/graph-coloring-algorithm-in-python/
# Description:
# This algorithm solves the graph coloring problem by finding the minimum number of colors required 
# to color a graph such that no two adjacent nodes share the same color. It uses a backtracking 
# approach with binary search optimization to minimize the number of colors.

# Total Complexity:
# Time Complexity: O(V * log(V) * max_colors), where V is the number of nodes. The binary search 
# runs log(V) times, and each call to the backtracking algorithm takes O(V * max_colors). 
# Space Complexity: O(V), due to storing the colors and recursion stack.

class GraphColoring:
    def __init__(self, space_graph):
        """
        Initializes the graph coloring class.
        Ensures the graph is treated as undirected by adding reverse edges if missing,
        and represents all nodes, including isolated ones.
        
        :param space_graph: Instance of SpaceGraph with adjacency list representation.
        """
        self.graph = space_graph.graph

        # Collect all nodes and ensure the graph is undirected.
        all_nodes = set(self.graph.keys())
        for src, edges in list(self.graph.items()):
            for edge in edges:
                dest = edge['destination']
                all_nodes.add(dest)

                # Add reverse edge if missing.
                if dest not in self.graph:
                    self.graph[dest] = []
                if not any(e['destination'] == src for e in self.graph[dest]):
                    self.graph[dest].append({
                        'destination': src,
                        'distanceLY': edge['distanceLY'],
                        'hyperflowSpiceMegaTons': edge['hyperflowSpiceMegaTons']
                    })

        # Ensure all nodes, including isolated ones, are represented in the graph.
        for n in all_nodes:
            if n not in self.graph:
                self.graph[n] = []

        self.colors = {}  # Dictionary to store assigned colors for nodes.
        self.nodes = list(all_nodes)  # List of all nodes in the graph.

    def is_safe(self, node, color):
        """
        Checks if assigning a specific color to a node is valid.
        
        :param node: The current node being colored.
        :param color: The color to assign.
        :return: True if the color assignment is valid (no adjacent nodes share the color), False otherwise.
        
        Time Complexity: O(d), where d is the degree of the node (number of neighbors).
        Space Complexity: O(1), as it only checks the neighbors.
        """
        for neighbor in self.graph[node]:
            neighbor_node = neighbor['destination']
            if self.colors.get(neighbor_node) == color:
                return False
        return True

    def graph_coloring_util(self, node_index, max_colors):
        """
        Backtracking utility function to assign colors to nodes.
        
        :param node_index: Index of the current node in the list of nodes.
        :param max_colors: Maximum number of colors allowed.
        :return: True if the graph can be colored with the given number of colors, False otherwise.
        
        Time Complexity: O(V * max_colors), where V is the number of nodes.
        Space Complexity: O(V), due to the recursion stack and storing colors.
        """
        if node_index == len(self.nodes):  # All nodes are colored.
            return True

        node = self.nodes[node_index]

        for color in range(1, max_colors + 1):
            if self.is_safe(node, color):
                self.colors[node] = color  # Assign the color.
                if self.graph_coloring_util(node_index + 1, max_colors):  # Recur for the next node.
                    return True
                del self.colors[node]  # Backtrack if the color doesn't work.

        return False  # Return False if no color can be assigned.

    def find_min_colors(self):
        """
        Finds the minimum number of colors required to color the graph.
        Uses binary search to optimize the number of colors.

        :return: Tuple containing the minimum number of colors and the coloring solution.
        
        Time Complexity: O(V * log(V) * max_colors), where V is the number of nodes.
        Space Complexity: O(V), for recursion stack and storing node colors.
        """
        # Initialize the binary search range for the number of colors.
        low, high = 1, len(self.nodes)
        best_solution = None

        while low <= high:
            mid = (low + high) // 2  # Midpoint of the current color range.
            self.colors.clear()  # Clear previous color assignments.

            if self.graph_coloring_util(0, mid):  # Check if the graph can be colored with 'mid' colors.
                best_solution = self.colors.copy()  # Save the current valid coloring solution.
                high = mid - 1  # Try to minimize the number of colors.
            else:
                low = mid + 1  # Increase the number of colors.

        return len(set(best_solution.values())), best_solution  # Return the minimum colors and the solution.
