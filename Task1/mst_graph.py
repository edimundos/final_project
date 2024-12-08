class MST_graph:
    def __init__(self):
        self.adjacency_list={}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node]=[]

    def add_edge(self, from_node, to_node, cost):
        self.add_node(from_node)
        self.add_node(to_node)

        #We append nodes and cost to both nodes since MST can be created only for undirected graphs
        self.adjacency_list[from_node].append((to_node,cost))
        self.adjacency_list[to_node].append((from_node, cost))

    def get_neighbours(self, node):
        return self.adjacency_list.get(node,[])

    def __str__(self):
        return str(self.adjacency_list)