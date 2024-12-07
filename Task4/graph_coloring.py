# inpiration for backtraccking algorithm: https://www.geeksforgeeks.org/graph-coloring-algorithm-in-python/
# recurcively call untill minimum number of colors is found

class GraphColoring:
    def __init__(self, space_graph):
        """
        Initializes the graph coloring class.
        :param space_graph: Instance of SpaceGraph (adjacency list format)
        """
        self.graph = space_graph.graph
        self.colors = {}
        self.nodes = list(self.graph.keys())

    def is_safe(self, node, color):
        """
        Check if assigning a specific color to a node is safe.
        :param node: Current node being colored
        :param color: Color to assign
        :return: True if safe, False otherwise
        """
        for neighbor in self.graph[node]:
            neighbor_node = neighbor['destination']
            if self.colors.get(neighbor_node) == color:
                return False
        return True

    def graph_coloring_util(self, node_index, max_colors):
        """
        Utility function to solve the graph coloring problem using backtracking.
        :param node_index: Current node index in self.nodes
        :param max_colors: Maximum colors allowed
        :return: True if successful, False otherwise
        """
        if node_index == len(self.nodes):  # All nodes are colored
            return True

        node = self.nodes[node_index]

        for color in range(1, max_colors + 1):
            if self.is_safe(node, color):
                self.colors[node] = color  # Assign the color
                if self.graph_coloring_util(node_index + 1, max_colors):  # Recursive call
                    return True
                del self.colors[node]  # Backtrack

        return False

    def find_min_colors(self):
        """
        Finds the minimum number of colors required to color the graph.
        :return: Minimum number of colors and the coloring solution.
        """
        low, high = 1, len(self.nodes)
        best_solution = None

        while low <= high:
            mid = (low + high) // 2
            self.colors.clear()  # Reset coloring for each attempt

            if self.graph_coloring_util(0, mid):  # Check if coloring is possible with 'mid' colors
                best_solution = self.colors.copy()
                high = mid - 1  # Try fewer colors
            else:
                low = mid + 1  # Try more colors

        return len(set(best_solution.values())), best_solution
