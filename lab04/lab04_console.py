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
            "1": "Generate random directed graph",
            "2": "Generate strongly consistent digraph",
            "3": "Find strongly consistent components (Kosaraju algorithm)",
            "4": "Find shortest paths from one node to the rest (Bellman-Ford algorithm)",
            "5": "Find all distances between pairs (Johnson algorithm)",
            "p": "Print graph",
            "t": "Plot graph",
            "q": "Quit",
        }
        self.plotting_options = {
            "1": "Normal (all options on)",
            "2": "Without groups",
            "3": "Without wages",
            "4": "Nodes and edges only",
            "b": "Go back"
        }

    def newline(self):
        self.console.print()

    def err(self, err_msg=""):
        self.console.print(f"[bold red]Error[/bold red]: {err_msg}.")

    def print_options(self) -> None:
        self.console.print(f"Available options:")
        for option in self.options:
            self.console.print(f"[[bold green]{option}[/bold green]] {self.options[option]}")

    def select_plotting_type(self) -> str:
        while True:
            print("How should the graph be plotted")
            for option in self.plotting_options:
                self.console.print(f"[[bold blue]{option}[/bold blue]] {self.plotting_options[option]}")
            try:
                choice = input("What would you like to do? ")
                if choice in self.plotting_options.keys():
                    return choice
                else:
                    self.err("Unrecognized option, try again.")
                    self.newline()
            except:
                self.err("Something went wrong.")
                self.newline()

    def run(self) -> None:
        self.console.print("[bold]Hello, user!")

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
                    try:
                        groups = None
                        n_nodes = int(input("Number of nodes: "))
                        prob = float(input("Probability (0-1): "))
                        w_min = int(input("Lowest possible weight: "))
                        w_max = int(input("Highest possible weight: "))
                        result = get_directed_graph_with_probability(num_of_nodes=n_nodes,
                                                                     probability=prob,
                                                                     lowest_weight=w_min,
                                                                     highest_weight=w_max)


                        G.load_data(result, RepresentationType.ADJACENCY_MATRIX)
                        self.console.print("[bold green]Success:[/bold green] Graph generated.")
                    except:
                        self.err("Something went wrong")
                    # GraphPlotter.plot_graph(G, draw_wages=True, draw_arrows=True)

                elif main_choice == '2':
                    groups = None
                    n_nodes = int(input("Number of nodes: "))
                    prob = float(input("Probability (0-1): "))
                    w_min = int(input("Lowest possible weight: "))
                    w_max = int(input("Highest possible weight: "))
                    try:
                        G = get_connected_digraph(num_of_nodes=n_nodes,
                                                  probability=prob,
                                                  lowest_weight=w_min,
                                                  highest_weight=w_max)
                        self.console.print("[bold green]Success:[/bold green] Graph generated.")
                    except RuntimeError as e:
                        self.err(str(e))
                    except:
                        self.err("Something went wrong")

                    # GraphPlotter.plot_graph(G, draw_wages=True, draw_arrows=True)

                elif main_choice == '3':
                    if not G.repr:
                        self.err("Graph not created. Generate it first")
                        continue
                    groups = kosaraju(G)
                    self.console.print("[bold green]Success:[/bold green] Groups successfully found.")
                    GraphPlotter.plot_graph(G, draw_wages=False,
                                            draw_arrows=True,
                                            nodes_color_modes=groups)

                elif main_choice == '4':
                    if not G.repr:
                        self.err("Graph not created. Generate it first")
                        continue
                    start = int(input("Start from: "))
                    try:
                        print(f"\nShortest paths from node [{start}]:")
                        print(bellman_ford(G, start))
                    except Exception as e:
                        self.err(str(e))

                elif main_choice == '5':
                    if not G.repr:
                        self.err("Graph not created. Generate it first")
                        continue
                    G.to_adjacency_matrix()
                    try:
                        johnson_algorithm(G)
                    except Exception as e:
                        self.err(str(e))

                elif main_choice == 'p':
                    if not G.repr:
                        self.err("Graph not created. Generate it first")
                        continue
                    print_graph(G)

                elif main_choice == 't':
                    if not G.repr:
                        self.err("Graph not created. Generate it first")
                        continue
                    choice = self.select_plotting_type()
                    if choice == '1':
                        GraphPlotter.plot_graph(G, draw_wages=True,
                                                draw_arrows=True,
                                                nodes_color_modes=groups)
                    elif choice == '2':
                        GraphPlotter.plot_graph(G, draw_wages=True,
                                                draw_arrows=True,
                                                nodes_color_modes=None)

                    elif choice == '3':
                        GraphPlotter.plot_graph(G, draw_wages=False,
                                                draw_arrows=True,
                                                nodes_color_modes=groups)

                    elif choice == '4':
                        GraphPlotter.plot_graph(G, draw_wages=False,
                                                draw_arrows=True,
                                                nodes_color_modes=None)

                else:
                    self.err("Unrecognized option")
                    self.newline()
        except:
            self.err("Critical error. Exiting..")
            self.newline()


if __name__ == "__main__":
    program = Program()
    program.run()
