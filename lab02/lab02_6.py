import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from algorithms.hamilton import hamilton

if __name__ == '__main__':
	graph1 = [[0, 1, 0, 1, 0],[1, 0, 1, 1, 1],[0, 1, 0, 0, 1],[1, 1, 0, 0, 1],[0, 1, 1, 1, 0]]  #adjacency matrix
 
	graph2 = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],[0, 1, 0, 0, 1],[1, 1, 0, 0, 0], [0, 1, 1, 0, 0]] #adjacency matrix
 
	print(hamilton(graph1))
	print(hamilton(graph2))
