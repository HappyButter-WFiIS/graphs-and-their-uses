import numpy as np
import random
from array import *

def my_function(numOfVertices, numOfEdges):
    my_list = list(range(0,numOfVertices))
    res = [(a, b) for idx, a in enumerate(my_list) for b in my_list[idx + 1:]]
    while len(res) > numOfEdges:
        random_item_from_list = random.choice(res)
        res.remove(random_item_from_list)
    return res
    
# numOfVertices = 5
# numOfEdges = 8
# edges = my_function(numOfVertices,numOfEdges)

# matrix = [ [0]*numOfEdges for i in range(numOfVertices) ]

# for i in range(numOfEdges):
#     matrix[edges[i][0]][i] = 1
#     matrix[edges[i][1]][i] = 1
    
# print(np.matrix(matrix))

def get_graph_with_probability(num_of_nodes: int, probability: float) -> np.ndarray:
    graph = np.random.random((num_of_nodes, num_of_nodes))
    graph = graph >= 1 - probability

    for i in range(num_of_nodes):
        graph[i][i] = False
    return graph