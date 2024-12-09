class SpaceGraph:
    def __init__(self, data_dict):
        """
        Initializes the SpaceGraph with a dictionary of edges.
        Each edge is a tuple (source, destination) with attributes distanceLY and hyperflowSpiceMegaTons.

        :param data_dict: Dictionary containing the edge data in the format:
                          {(source, destination): {'distanceLY': ..., 'hyperflowSpiceMegaTons': ...}}

        Time Complexity: O(E), where E is the number of edges.
        Space Complexity: O(V + E), for storing the adjacency list representation.
        """
        self.graph = {}  # Initialize an empty graph (adjacency list).
        self.build_graph(data_dict)

    def build_graph(self, data_dict):
        """
        Builds the adjacency list representation of the graph from the input dictionary.
        :param data_dict: Dictionary containing the graph edges and attributes.

        Time Complexity: O(E), where E is the number of edges in the graph.
        Space Complexity: O(V + E), for storing the graph as an adjacency list.
        """
        for (source, destination), attributes in data_dict.items():
            if source not in self.graph:  # If the source node is not in the graph, add it.
                self.graph[source] = []
            # Add the edge with its attributes to the adjacency list.
            self.graph[source].append({
                'destination': destination,
                'distanceLY': attributes['distanceLY'],
                'hyperflowSpiceMegaTons': attributes['hyperflowSpiceMegaTons']
            })

    def get_neighbors(self, node):
        """
        Retrieves all neighbors of a given node along with edge attributes.
        :param node: The node whose neighbors are being queried.
        :return: List of neighbors with edge attributes, or an empty list if the node has no neighbors.

        Time Complexity: O(1), as adjacency list access is constant time.
        Space Complexity: O(1), as no additional storage is used.
        """
        return self.graph.get(node, [])

    def display_graph(self):
        """
        Prints the structure of the graph, displaying each node and its edges.

        Time Complexity: O(V + E), as all nodes and edges are traversed for display.
        Space Complexity: O(1), as no additional storage is required for this operation.
        """
        for node, edges in self.graph.items():
            print(f"{node}:")
            for edge in edges:
                print(f"  -> {edge['destination']} (distance: {edge['distanceLY']} LY, hyperflow: {edge['hyperflowSpiceMegaTons']} MT)")


def readFile(fileName):
    """
    Reads a CSV file and constructs a dictionary representing the space graph.
    Handles scientific notation and invalid data gracefully.

    :param fileName: Name of the CSV file containing the graph data.
    :return: Dictionary in the format:
             {(source, dest): {'distanceLY': ..., 'hyperflowSpiceMegaTons': ...}}

    Handles:
        - Missing columns (KeyError).
        - Invalid formats in numeric fields (ValueError).

    Time Complexity: O(N), where N is the number of rows in the file.
    Space Complexity: O(N), for storing the resulting dictionary.
    """
    data_dict = {} 

    with open(fileName, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Extract and validate row data.
                source = row['source']
                destination = row['destination']
                distanceLY = float(row['distanceLY'])  # Convert to float to handle scientific notation.
                hyperflowSpiceMegaTons = int(row['hyperflowSpiceMegaTons'])  # Convert to integer.

                # Add the edge data to the dictionary.
                data_dict[(source, destination)] = {
                    'distanceLY': distanceLY,
                    'hyperflowSpiceMegaTons': hyperflowSpiceMegaTons
                }
            except KeyError as e:
                print(f"Missing column in data: {e}")  
            except ValueError as e:
                print(f"Invalid data format in row: {row} - {e}") 

    return data_dict
