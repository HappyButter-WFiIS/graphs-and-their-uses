import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from utils.graph_generators import gen_random_conn_graph_weighted, randomize
from algorithms.mst import kruskal, prim
from algorithms.components import get_components, print_sorted_components
from algorithms.dijkstra import find_shortest_path
from algorithms.hamilton import hamilton
from lab03.lab03_04 import get_graph_centre, get_minimax_centre


def display_welcome() -> None:
    """
    Displaying welcome information
    """
    print(50 * '-')
    print("Welcome to graph destroyer 3000 vol.2")
    print(50 * '-' + '\n')


class MissingGraphException(Exception):
    pass


def display_menu() -> None:
    """
    Displaying main menu
    """
    print('\n[1] Generate a random consistent simple graph')
    print('[2] Use Djikstra algorithm')
    print('[3] Get a distance matrix')
    print('[4] Find the center')
    print('[5] Find the MinMax center')
    print('[6] Find the minimal spanning tree')
    print('[p] Plot the graph')
    print('[0] Load graph from file')
    print('[q] Quit\n')


def handle_read_from_file(G: Graph, repr_type: int, file_name: str = ""):
    """
    Reading graph from file. File must be inside the folder where Lab01_console.py is.
    """
    try:
        G.create_representation(os.path.dirname(
            __file__) + "/" + file_name, RepresentationType(repr_type))
        print("----Your graph has been successfully loaded!----")
    except:
        print("\nInvalid file type have been chosen.")


def load_graph_from_file_menu(G: Graph) -> None:
    """
    Loading graph from file.
    """
    representation_type = -1
    while representation_type != 5 and representation_type != 6:
        print("What representation type is in the file?")
        print("\n[1] Adjancency matrix")
        print("[2] Adjacency list")
        print("[3] Incidence matrix")

        try:
            representation_type = int(input("Pick the type:\n")) + 4
        except:
            representation_type = -1

    print("Ok. Now put the file name.")
    file_name = input("File name:\n")

    if file_name:
        handle_read_from_file(G, int(representation_type), file_name)


def present_conn_simple_graph_generation(G: Graph):
    size = -1
    while size <= 0:
        try:
            size = int(input("What's the size of your graph?\n"))
            if size <= 0:
                raise Exception
        except Exception:
            print("The size has to be a number greater than 0")
            size = -1
    G.load_data(data=gen_random_conn_graph_weighted(size),
                representation_type=RepresentationType.ADJACENCY_MATRIX_WITH_WEIGHTS)
    print("----Your graph has been successfully created!----")


def present_djikstra_algorithm(G: Graph):
    if not G.repr:
        raise MissingGraphException
    end = start = -1
    max_node = np.shape(G.repr)[0]
    while start < 1 or start > max_node:
        try:
            start = int(input("Insert number of start node.\n"))
            if start < 1 or start > max_node:
                raise Exception
        except:
            print(f"Node number has to be chosen from 1 to {max_node}")
            start = -1
    while end < 1 or start > max_node:
        try:
            end = int(input("Insert number of destination node.\n"))
            if end < 1 or end > max_node:
                raise Exception
        except:
            print(f"Node number has to be chosen from 1 to {max_node}")
            end = -1
    print(f"---- {find_shortest_path(G.get_weighted_adjacency_list(), start, end, verbose=True)} ----")


def present_distance_matrix(G: Graph):
    if not G.repr:
        raise MissingGraphException
    matrix = G.get_distance_matrix()
    print("----Distance Matrix----")
    for line in matrix:
        print(line)


def present_minimal_spanning_tree(G: Graph, main_choice):
    if not G.repr:
        raise MissingGraphException
    print("[1] Use Kruskal algorithm.")
    print("[2] Use Prim algorithm.")
    print("[Any other key] Go back.")
    choice = input('Chose algorithm to find a minimal spanning tree.\n')
    if choice == '1':
        kruskal(G.repr)
    elif choice == '2':
        prim(G.repr)


if __name__ == '__main__':
    main_choice = ''
    G = Graph()
    while main_choice != 'q':
        display_menu()
        main_choice = input("What would you like to do?\n")
        try:
            if main_choice == '1':
                present_conn_simple_graph_generation(G)
            elif main_choice == '2':
                present_djikstra_algorithm(G)
            elif main_choice == '3':
                present_distance_matrix(G)
            elif main_choice == '4':
                if not G.repr:
                    raise MissingGraphException
                central_node = get_graph_centre(dist_matrix=G.get_distance_matrix())
                print(f'The center of the graph is located in the node number {central_node}')
            elif main_choice == '5':
                if not G.repr:
                    raise MissingGraphException
                central_node = get_minimax_centre(dist_matrix=G.get_distance_matrix())
                print(f'The MinMax center of the graph is located in the node number {central_node}')
            elif main_choice == '6':
                if not G.repr:
                    raise MissingGraphException
                present_minimal_spanning_tree(G, main_choice)
            elif main_choice == 'p':
                if not G.repr:
                    raise MissingGraphException
                GraphPlotter.plot_graph(G)
            elif main_choice == '0':
                load_graph_from_file_menu(G)
            else:
                print("I dont know what do you mean :)")
        except MissingGraphException:
            print("First you need to load or generate a graph.")
        except KeyError:
            print("Check If your data is OK")
        except:
            print("Something went wrong. Try again!")

    print("\nThanks for playing. Bye.")
