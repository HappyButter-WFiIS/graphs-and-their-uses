import logging

from rich.console import Console
from rich import print
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.DirectedGraph import DirectedGraph
from utils.Graph import Graph, RepresentationType
from utils.graph_generators import get_directed_graph_with_probability
from algorithms.kosaraju import kosaraju
from utils.graph_plotter import GraphPlotter
from algorithms.bellman_ford import bellman_ford
from utils.graph_generators import get_connected_digraph
from algorithms.johnson import johnson_algorithm


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
            "1": "Random directed graph",
            "2": "Find strongly consistent components (Kosaraju)",
            "3": "Strongly consistent digraph",
            "4": "Shortest paths (Bellman-Ford)",
            "5": "All distances (Johnson)",
            "p": "Print graph",
            "t": "Plot graph",
            "q": "Quit",
        }

    def newline(self):
        self.console.print()

    def err(self, err_msg=""):
        self.console.print(f"[bold red]Error[/bold red] {err_msg}.")

    def print_options(self) -> None:
        for option in self.options:
            self.console.print(f"[[bold green]{option}[/bold green]]: {self.options[option]}")

    def run(self) -> None:
        self.console.print("[bold]Hello, fellow user!")
        self.newline()

        G = DirectedGraph()
        groups = None

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
                    groups = None
                    n_nodes = int(input("Number of nodes: "))
                    prob = float(input("Probability (0-1): "))
                    result = get_directed_graph_with_probability(num_of_nodes=n_nodes,
                                                                 probability=prob,
                                                                 lowest_weight=-5,
                                                                 highest_weight=10)
                    G.load_data(result, RepresentationType.ADJACENCY_MATRIX)

                elif main_choice == '2':
                    groups = kosaraju(G)
                    GraphPlotter.plot_graph(G, draw_wages=False,
                                            draw_arrows=True,
                                            nodes_color_modes=groups)

                elif main_choice == '3':
                    groups = None
                    n_nodes = int(input("Number of nodes: "))
                    prob = float(input("Probability (0-1): "))
                    G = get_connected_digraph(num_of_nodes=n_nodes,
                                              probability=prob,
                                              lowest_weight=-5,
                                              highest_weight=10)
                    GraphPlotter.plot_graph(G, draw_wages=True, draw_arrows=True)

                elif main_choice == '4':
                    start = int(input("Start from: "))
                    try:
                        print(f"\nShortest paths from node [{start}]:")
                        self.console.print(bellman_ford(G, start))
                    except Exception as e:
                        print(e)

                elif main_choice == '5':
                    G = get_connected_digraph(5, 0.2, -5, 10)
                    G.to_adjacency_matrix()
                    johnson_algorithm(G)

                elif main_choice == 'p':
                    print_graph(G)

                elif main_choice == 't':
                    GraphPlotter.plot_graph(G, draw_wages=True,
                                            draw_arrows=True,
                                            nodes_color_modes=groups)

                else:

                    self.err("I didn't understand that choice.")
                    self.newline()
        except:
            self.err("Something went wrong.")
            self.newline()


if __name__ == "__main__":
    program = Program()
    program.run()
