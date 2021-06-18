import logging

from rich.console import Console
from rich import print
import os, sys
import copy

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.DirectedGraph import DirectedGraph

from utils.graph_generators import get_flow_network
from utils.FlowNetworkPlotter import FlowNetworkPlotter
from utils.Graph import Graph, RepresentationType

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


def exit_program() -> None:
    print("[bold]Thanks for playing. Bye!")


def print_graph(G: Graph) -> None:
    """
    Printing given Graph to console.
    """
    print("\nCurrent graph representation type is: ")
    if G.repr_type == RepresentationType.ADJACENCY_MATRIX:
        print("Adjacency matrix")
    elif G.repr_type == RepresentationType.ADJACENCY_LIST:
        print("Adjacency list")
    elif G.repr_type == RepresentationType.INCIDENCE_MATRIX:
        print("Incidence matrix")

    print()
    print(G)


class Program:
    def __init__(self):
        self.console = Console()
        self.options = {
            "1": "Generate random network",
            "2": "Generate 2-layer network from file",
            "3": "Count Maximum flow",
            "4": "Clear network",
            "p": "Print network",
            "q": "Quit",
        }

    def newline(self):
        self.console.print()

    def err(self, err_msg=""):
        self.console.print(f"[bold red]Error[/bold red]: {err_msg}.")

    def print_options(self) -> None:
        self.console.print(f"Available options:")
        for option in self.options:
            self.console.print(f"[[bold green]{option}[/bold green]] {self.options[option]}")



    def run(self) -> None:
        self.console.print("[bold]Hello, user!")
        is_generated = False
        G = DirectedGraph()
        groups = None
        network = get_flow_network(4)

        main_choice = ''

        try:
            while main_choice != 'q':
                self.newline()
                self.print_options()
                self.newline()

                main_choice = input("What would you like to do? ")

                if main_choice == 'q':
                    exit_program()

                elif main_choice == '1':
                    try:
                        n_layers = int(input("Number of layers: "))
                        network = get_flow_network(n=n_layers)
                        self.console.print("[bold green]Success:[/bold green] Graph generated.")
                        is_generated = True
                    except:
                        self.err("Something went wrong")
                    # GraphPlotter.plot_graph(G, draw_wages=True, draw_arrows=True)

                elif main_choice == '3':
                    if not is_generated:
                        self.err("Network not created. Generate it first")
                        continue
                    plotter = FlowNetworkPlotter()
                    plotter.load_network(network)
                    network_copy = copy.deepcopy(network)
                    print(network_copy.ford_fulkerson(network_copy.source_node, network_copy.target_node))

                elif main_choice == '4':
                    if not is_generated:
                        self.err("Can't clear non existing network! Generate it first")
                        continue
                    network.clear_flow_network()
                    is_generated = False

                elif main_choice == '2':
                    try:
                        self.console.print("generating graph from inputs/network.txt")
                        G = Graph()
                        G.create_representation(os.path.dirname(__file__) + '/inputs/network.txt',
                                                RepresentationType.ADJACENCY_MATRIX)
                        network = get_flow_network(n=2)
                        network.repr = G.repr
                        network.source_node = 0
                        network.target_node = 5
                        is_generated = True
                        self.console.print("[bold green]Success:[/bold green] Graph generated.")
                    except:
                        self.err("Something went wrong")

                elif main_choice == 'p':
                    plotter = FlowNetworkPlotter()
                    plotter.load_network(network)
                    plotter.plot(rand_offset_factor=0.6)

                else:
                    self.err("Unrecognized option")
                    self.newline()
        except:
            self.err("Critical error. Exiting..")
            self.newline()


if __name__ == "__main__":
    program = Program()
    program.run()
