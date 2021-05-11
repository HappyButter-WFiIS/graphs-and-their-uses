import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.graph_generators import get_graph_with_probability, get_graph_by_vertices_and_edges
from utils.graph_plotter import plot_graph
from utils.Graph import Graph, RepresentationType

def print_graph(G: Graph) -> None:
    """
    Printing given Graph to console.
    """
    print("\nCurrent graph representation type is: ")
    if G.repr_type == RepresentationType.ADJACENCY_MATRIX:
        print("Adjancency matrix")
    elif G.repr_type == RepresentationType.ADJACENCY_LIST:
        print("Adjacency list")
    elif G.repr_type == RepresentationType.INCIDENCE_MATRIX:
        print("Incidence matrix")

    print()
    print(G)


def handle_read_from_file(G: Graph, repr_type: int, file_name: str = "") -> None:
    """
    Reading graph from file. File must be inside the folder where Lab01_console.py is.
    """
    if repr_type == 1 or repr_type == 2 or repr_type == 3:
        G.create_representation(os.path.dirname(
            __file__) + "/" + file_name, RepresentationType(repr_type))
    else:
        print("\nInvalid file type have been chosen.")


def display_welcome() -> None:
    """
    Welcome information printed in console.
    """
    print(50*'-')
    print("\tWelcome to graph destroyer 3000")
    print(50*'-' + '\n')


def handle_convert(G: Graph) -> None:
    """
    Graph representation type convert handler.
    """
    convert_repr_type = ''

    print("\nPick representation type:")
    print("[1] Adjancency matrix")
    print("[2] Adjacency list")
    print("[3] Incidence matrix")
    convert_repr_type = input()

    if convert_repr_type == '1':
        G.to_adjacency_matrix()
        print_graph(G)
    elif convert_repr_type == '2':
        G.to_adjacency_list()
        print_graph(G)
    elif convert_repr_type == '3':
        G.to_incidence_matrix()
        print_graph(G)
    else:
        print("\nPut a valid option.")


def display_submenu(G: Graph) -> None:
    """
	Submenu of main menu. Let user to go to convert handler or
	plot graph or print current graph or go back to main menu.
	"""
    operations_choice = ''

    while operations_choice != 'q':
        print()
        print(50*'-')
        print("[1] Convert")
        print("[2] Plot")
        print("[3] Print current graph")
        print("[b] Go back to menu")

        operations_choice = input("Pick the option:\n")

        if operations_choice == 'b':
            return

        if operations_choice == '1':
            handle_convert(G)
        elif operations_choice == '2':
            plot_graph(G)
        elif operations_choice == '3':
            print_graph(G)


def load_graph_from_file_menu(G: Graph) -> None:
    """
	Loading graph from file.
	"""
    print("What representation type is in the file?")
    print("\n[1] Adjancency matrix")
    print("[2] Adjacency list")
    print("[3] Incidence matrix")

    representation_type = input("Pick the type:\n")

    print("Ok. Now put the file name.")
    file_name = input("File name:\n")

    if representation_type and file_name:
        handle_read_from_file(G, int(representation_type), file_name)

    display_submenu(G)


def generate_with_probability_menu(G: Graph) -> None:
    num_of_nodes = input("Put number of nodes:\n")
    probability = input("Put probability from range: (0;1):\n")

    data = get_graph_with_probability(int(num_of_nodes), float(probability))
    G.load_data(
        data=data, representation_type=RepresentationType.ADJACENCY_MATRIX)

    display_submenu(G)


def generate_with_vertices_and_edges_menu(G: Graph) -> None:
    num_of_vertices = input("Put number of vertices:\n")
    num_of_edges = input("Put number of edges:\n")

    data = get_graph_by_vertices_and_edges(
        int(num_of_vertices), int(num_of_edges))
    G.load_data(
        data=data, representation_type=RepresentationType.INCIDENCE_MATRIX)

    display_submenu(G)


if __name__ == "__main__":
    main_choice = ''
    G = Graph()

    try:
        while main_choice != 'q':
            display_welcome()
            print("[1] Load graph from file")
            print("[2] Generate with probability")
            print("[3] Generate with vertices and edges")
            print("[q] Quit\n")

            main_choice = input("What would you like to do?\n")

            if main_choice == 'q':
                print("\nThanks for playing. Bye.")

            elif main_choice == '1':
                load_graph_from_file_menu(G)

            elif main_choice == '2':
                generate_with_probability_menu(G)

            elif main_choice == '3':
                generate_with_vertices_and_edges_menu(G)
            else:
                print("\nI didn't understand that choice.\n")
    except:
        print("Something went wrong.")
