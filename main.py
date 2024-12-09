
from Graphs.space_graph import Space_graph
from Graphs.utils import readFile, build_undirected_graph_regular
from Task4.graph_coloring_parse import findColoring
from Task5.longest_loop_parse import findLongestPath
from Task1.mst_graph_parse import develop_mst, print_mst, write_mst
# from Task2.maximum_flow_parse import print_mf


def main():
    data_dict = readFile("actual_distances_space_graph.csv")
    develop_mst(data_dict)

    # Create a graph object
    space_graph_undirected = build_undirected_graph_regular(data_dict)


    findColoring(space_graph_undirected, doPrint=False, export=True)

    findLongestPath(space_graph_undirected, doPrint=False, export=True)



if __name__ == "__main__":
    main()
