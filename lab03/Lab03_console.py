import os, sys

from algorithms.components import get_components, print_sorted_components
from algorithms.dijkstra import find_shortest_path
from algorithms.hamilton import hamilton

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from utils.graph_generators import gen_random_conn_graph_weighted, randomize
from algorithms.mst import kruskal, prim


def display_welcome() -> None:
    """
    Displaying welcome information
    """
    print(50 * '-')
    print("Welcome to graph destroyer 3000 vol.2")
    print(50 * '-' + '\n')


def display_menu() -> None:
    """
    Displaying main menu
    """
    print('\n[1] Generate a random consistent simple graph')
    print('[2] Use Djikstra algorithm')
    print('[3] Get a distance matrix')
    print('[4] Find the center and the MinMax center')
    print('[5] Find the minimal spanning tree')
    print('[0] Load graph from file')
    print('[q] Quit\n')


def present_conn_simple_graph_generation(G: Graph):
    size = int(input("What's the size of your graph?\n"))
    G.load_data(data=gen_random_conn_graph_weighted(size),
                representation_type=RepresentationType.ADJACENCY_MATRIX_WITH_WEIGHTS)


def present_djikstra_algorithm(G: Graph):
    start = int(input("Insert number of start node (indexing starts with 1).\n"))
    end = int(input("Insert number of destination node (indexing starts with 1).\n"))
    find_shortest_path(G.get_weighted_adjacency_list(), start, end, verbose=True)


def present_distance_matrix(G: Graph):
    matrix = G.get_distance_matrix()
    for line in matrix:
        print(line)


def present_minimal_spanning_tree(G: Graph, main_choice):
    print("[1] Use Kruskal algorithm.")
    print("[2] Use Prim algorithm.")
    print("[b] Go back.")
    choice = input('Chose algorithm to find a minimal spanning tree.\n')
    if choice == '1':
        kruskal(G.repr)
    elif choice == '2':
        prim(G.repr)
    elif choice == 'b':
        main_choice[:] = ''


if __name__ == '__main__':
    main_choice = ''

    G = Graph()
    while main_choice != 'q':
        display_menu()
        main_choice = input("What would you like to do?\n")

        try:

            if main_choice == '1':
                present_conn_simple_graph_generation(G)
            if main_choice == '2':
                present_djikstra_algorithm(G)
            if main_choice == '3':
                present_distance_matrix(G)
            if main_choice == '4':
                pass
            if main_choice == '5':
                present_minimal_spanning_tree(G, main_choice)
            if main_choice == '0':
                pass
                # load_graph_from_file_menu()
        except:
            print("Something went wrong. Try again!")

    print("\nThanks for playing. Bye.")
