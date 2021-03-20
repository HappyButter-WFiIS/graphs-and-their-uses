from graph_representation.Graph import Graph
import sys

if __name__ == "__main__":
    G = Graph() 

    filename = input("Nazwa pliku\n") 
    file = open(filename, 'r')
    content = file.read().split('\n')

    mode = int(input('[1] - macierz sąsiedztwa\n[2] - lista sąsiedztwa\n[3] - macierz incydencji\n'))
    if mode == 1:
        G.create_adjacency_matrix(content)
    elif mode == 2:
        G.create_adjacency_list(content)
    elif mode == 3:
        G.create_incidence_matrix(content)

    print(G)
    


    
    
    


        