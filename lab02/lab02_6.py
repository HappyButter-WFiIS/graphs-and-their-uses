import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from algorithms.hamilton import isHamiltonian

if __name__ == '__main__':
    graph1 = [[1,3,4],[7,2,0],[3,6,1],[0,5,2],[0,7,5],[4,6,3],[7,5,2],[1,4,6]]  # adjacency list
    graph2 = [[1,2,3,4,5], [0], [0], [0,4,5], [0,3,5], [0,3,4]]                 # adjacency list
    
    print(isHamiltonian(graph1))  # output 1 means graph is hamiltonian
    print(isHamiltonian(graph2))  # output 0 means graph is not hamiltonian
