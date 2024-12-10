
from Graphs.space_graph import Space_graph
from Graphs.utils import readFile, build_undirected_graph_regular, build_directed_graph
from Task4.graph_coloring_parse import findColoring
from Task5.longest_loop_parse import findLongestPath
from Task1.mst_graph_parse import develop_mst, print_mst, write_mst
from Task2.maximum_flow_parse import ford_fulkerson_max_flow
from Task3.cosmic_diameter import longest_shortest_path


def main():
    data_dict = readFile("actual_distances_space_graph.csv")
    space_graph_directed = build_directed_graph(data_dict)
    space_graph_undirected = build_undirected_graph_regular(data_dict)

    #Task 1
    develop_mst(data_dict, True, True)

    #Task 2
    ford_fulkerson_max_flow(space_graph_directed, "Earth", "Betelgeuse")

    #Task 3
    longest_shortest_path(space_graph_directed)

    #Task 4
    findColoring(space_graph_undirected, doPrint=False, export=True)

    #Task 5
    findLongestPath(space_graph_undirected, doPrint=False, export=True)



if __name__ == "__main__":
    main()
