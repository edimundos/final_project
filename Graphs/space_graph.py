class Space_graph:
    def __init__(self):
        """
        Initialize the SpaceGraph with a dictionary of edges.
        Each edge is a tuple (source, destination) with attributes distanceLY and hyperflowSpiceMegaTons.
        """
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node]=[]

    def add_edge(self, from_node, to_node, flow, distance):
        self.add_node(from_node)
        self.add_node(to_node)

        self.graph[from_node].append({
            'destination': to_node,
            'distanceLY': distance,
            'hyperflowSpiceMegaTons': flow
        })


    def get_neighbors(self, node):
        """
        Get all neighbors of a node along with edge attributes.
        """
        return self.graph.get(node, [])
    
    def __str__(self):
        str =""
        for node, edges in self.graph.items():
            str +=(f"{node}:\n")
            for edge in edges:
                str += (f"  -> {edge['destination']} (distance: {edge['distanceLY']} LY, hyperflow: {edge['hyperflowSpiceMegaTons']} MT)\n")
        return str