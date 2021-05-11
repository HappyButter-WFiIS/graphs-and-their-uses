import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import GraphPlotter
from utils.graph_generators import randomize, get_graph_with_probability
from algorithms.euler import euler_cycle, generate_euler_graph_sequence
from algorithms.components import search, sort_groups
from algorithms.hamilton import isHamiltonian

def display_welcome():
    """
    Displaying welcome information
    """
    print(50*'-')
    print("Welcome to graph destroyer 3000 vol.2")
    print(50*'-' + '\n')	


def display_menu():
    """
    Displaying main menu
    """
    display_welcome()
    print('[1] Graphical sequence')
    print('[2] Graph randomization')
    print('[3] Graph components')
    print('[4] Eulerian graphs')
    print('[5] k-regular graphs')
    print('[6] Hamiltonian graphs')
    print('[q] Quit\n')


def present_graphical_sequence() -> list:
    """
    Presents graphical sequence inserting and checking [1].
    Returns sequence as a list if sequence is graphical.
    Otherwise - [] - empty list.
    """
    G = Graph()

    print('\nInsert sequence of integers')
    sequence = [int(x) for x in input('Your sequence: ').split()]

    if G.load_data(sequence, RepresentationType.GRAPH_SEQUENCE):
        print('Your sequence is graphical! Here is one of possible solutions\n')
        GraphPlotter.plot_graph(G)

    else:
        print('Sequence is not graphical\n')
        return []

    return sequence


def present_graph_randomization() -> None:
    """
    Presents graph randomization for graph using graphical sequence
    and randomizations parameter.
    """
    print('\nLet\'s start with Your own graphical sequence.\n')
    sequence = present_graphical_sequence()

    if sequence != []:
        randomizations = int(input('Number of randomizations: '))
        G = Graph()
        G.load_data(sequence, RepresentationType.GRAPH_SEQUENCE)
        G.to_adjacency_matrix()
        randomize(G, randomizations)
        GraphPlotter.plot_graph(G)


def present_components_finding() -> None:
    """
    Presents finding graph components for graph
    generated by 'get_graph_with_probability'
    with parameters given by user.
    """
    vertices = int(input('\nNumber of vertices: '))
    probability = float(input("Put probability (0;1):\n"))

    G = Graph()
    G.load_data(get_graph_with_probability(vertices, probability), RepresentationType.ADJACENCY_MATRIX)
    G.to_adjacency_list()

    groups = search(G)
    sort_groups(G, groups)
    GraphPlotter.plot_graph(G, groups)


def present_eulerian_graphs() -> None:
    """
    Generates Eulerian Graph sequence and finds Eulerian Cycle.
    """
    randomizations = 100
    v = int(input('\nNumber of vertices: '))

    G = Graph()

    if generate_euler_graph_sequence(G, v):
        print('Graphical sequence of graph: ' + str(G))
        G.to_adjacency_matrix()
        randomize(G, randomizations)
        print('Euler Cycle: ' + euler_cycle(G))
        GraphPlotter.plot_graph(G)

    else:
        print("Error while generating euler graph sequence")


def present_k_regular_graphs() -> None:
    """
    Finds k-regular graph for given k and vertices number.
    """
    vertices = int(input('\nNumber of vertices: '))
    k = int(input('Put k-parameter: '))
    number_of_randomizations = int(input("Put number of randomizations"))

    G = Graph()

    G.get_k_regular_with_n_vertices(k=k, vertices=vertices)
    randomize(G, number_of_randomizations)
    
    GraphPlotter.plot_graph(G)


def present_hamiltonian_graphs() -> None:
    """
    Chceck if graph generated by 'get_graph_with_probability'
    with parameters given by user is Hamiltonian.
    """
    vertices = int(input('\nNumber of vertices: '))
    probability = float(input("Put probability (0;1):\n"))

    G = Graph()
    G.load_data(get_graph_with_probability(vertices, probability), RepresentationType.ADJACENCY_MATRIX)
    G.to_adjacency_list()
    
    if isHamiltonian(G.repr) == 1:
        print('Graph is Hamiltonian')
    else:
        print('Graph is not Hamiltonian')

    GraphPlotter.plot_graph(G)


if __name__ == '__main__':
    main_choice = ''

    while main_choice != 'q':
        display_menu()
        main_choice = input("What would you like to do?\n")

        #try:

        if main_choice == '1':
            present_graphical_sequence()
        if main_choice == '2':
            present_graph_randomization()
        if main_choice == '3':
            present_components_finding()
        if main_choice == '4':
            present_eulerian_graphs()
        if main_choice == '5':
            present_k_regular_graphs()
        if main_choice == '6':
            present_hamiltonian_graphs()

        #except:
        #   print("Something went wrong. Try again!")
    print("\nThanks for playing. Bye.")
