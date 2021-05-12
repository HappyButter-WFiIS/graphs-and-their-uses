import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from algorithms.hamilton import isHamiltonian

if __name__ == '__main__':
    graph1 = [[2,4,5],[8,3,1],[4,7,2],[1,6,3],[1,8,6],[5,7,4],[8,6,3],[2,5,7]] # adjacency list
    graph2 = [[2,3,4,5,6], [1], [1], [1,5,6], [1,4,6], [1,4,5]]                 # adjacency list
    
    print(isHamiltonian(graph1))  # output 1 means graph is hamiltonian
    print(isHamiltonian(graph2))  # output 0 means graph is not hamiltonian
