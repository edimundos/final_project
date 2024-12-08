from utils import SpaceGraph, readFile
from Task4.graph_coloring_parse import findColoring
from Task5.longest_loop_parse import findLongestPath
from Task1.mst_graph_parse import develop_mst, print_mst, write_mst
from Task2.maximum_flow_parse import print_mf


def main():
    data_dict = readFile("actual_distances_space_graph.csv")
    # print(data_dict)

    mst_graph =develop_mst(data_dict)
    print_mst(mst_graph)
    write_mst(mst_graph)
    

    # Create a graph object
    space_graph = SpaceGraph(data_dict)

    # Display the graph
    # space_graph.display_graph()

    findColoring(space_graph, doPrint=True, export=True)

    findLongestPath(space_graph, doPrint=False, export=True)



if __name__ == "__main__":
    main()
