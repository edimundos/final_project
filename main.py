from Graphs.utils import build_directed_graph, readFile
from Task4.graph_coloring_parse import findColoring
from Task5.longest_loop_parse import findLongestPath
from Task1.mst_graph_parse import develop_mst, print_mst, write_mst
from Task2.maximum_flow_parse import ford_fulkerson_max_flow
from Task3.cosmic_diameter import shortest_longest_path


def main():
    data_dict = readFile("actual_distances_space_graph.csv")
    # print(data_dict)

    # Create a graph object
    space_graph = build_directed_graph(data_dict)

    mst_graph =develop_mst(data_dict)
    print_mst(mst_graph)
    write_mst(mst_graph)
    

    # Display the graph
    print(space_graph)

    print(shortest_longest_path(space_graph))

    flow_graph, flow = ford_fulkerson_max_flow(space_graph,"Earth", "Betelgeuse")
    print(flow)
    print(flow_graph)

    findColoring(space_graph, doPrint=False, export=True)

    findLongestPath(space_graph, doPrint=False, export=True)



if __name__ == "__main__":
    main()
