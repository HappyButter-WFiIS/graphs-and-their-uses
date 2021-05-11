import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from utils.Graph import Graph, RepresentationType
from utils.graph_plotter import plot_graph
from utils.graph_generators import get_graph_with_probability, get_graph_by_vertices_and_edges

def print_graph(G: GraphRepresentation):
	print()
	print(G)

def handle_read_from_file(file_name: str="", repr_type: str=""):
	G.create_representation(os.path.dirname(__file__) + "/" + file_name, RepresentationType(int(representation_type)))

def display_welcome():
	print(50*'-')
	print("Welcome to graph destroyer 3000")
	print(50*'-' + '\n')	

def display_submenu(G: Graph):
	operations_choice = ''

	while operations_choice != 'q':
		print(50*'-')
		print("[1] Convert")
		print("[2] Plot")
		print("[3] Print current graph")
		print("[b] Go back to menu")

		operations_choice = input("Pick the option:\n")

		if operations_choice == 'b':
			break

		if operations_choice == '1':
			convert_repr_type = ''

			print("Pick representation type:")	
			print("\n[1] Adjancency matrix")
			print("[2] Adjacency list")
			print("[3] Incidence matrix")
			convert_repr_type = input()


			if convert_repr_type == '1':
				G.to_adjacency_matrix()
				print(G)
			elif convert_repr_type == '2':
				G.to_adjacency_list()
				print(G)
			elif convert_repr_type == '3':
				G.to_incidence_matrix()
				print(G)

		elif operations_choice == '2':
			plot_graph(G)
		elif operations_choice == '3':
			print_graph(G)

if __name__ == "__main__":
	main_choice = ''
	representation_type = ''
	file_name = ''
	G = Graph()


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
			print("What representation type is in the file?")	
			print("\n[1] Adjancency matrix")
			print("[2] Adjacency list")
			print("[3] Incidence matrix")
			print("[q] Quit\n")

			representation_type = input("Pick the type:\n")
			
			if representation_type == 'q':
				print("\nThanks for playing. Bye.")
				break

			print("Ok. Now put the file name.")
			file_name = input("File name:\n")

			if representation_type and file_name:
				handle_read_from_file(file_name, representation_type)
			
			display_submenu(G)

		elif main_choice == '2':
			num_of_nodes = input("Put number of nodes:\n")
			probability = input("Put probability (0;1):\n")
			
			data = get_graph_with_probability(int(num_of_nodes), float(probability))

			G.load_data(data=data, representation_type=RepresentationType.ADJACENCY_MATRIX)

			display_submenu(G)

		elif main_choice == '3':
			num_of_vertices = input("Put number of vertices:\n")
			num_of_edges = input("Put number of edges:\n")
			
			data = get_graph_by_vertices_and_edges(int(num_of_vertices), int(num_of_edges))

			G.load_data(data=data, representation_type=RepresentationType.INCIDENCE_MATRIX)

			display_submenu(G)			
		else:
			print("\nI didn't understand that choice.\n")