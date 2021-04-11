from array import *
import random

def traverse(u, visited ,G):
    visited[u] = 1
    for v in range(len(G)):
        if (G[u][v]):
            if not (visited[v]):
                traverse(v,visited,G)

def isConnected(G) -> bool:
    visited = [0]*len(G)
    for u in range(len(G)):
        for i in range(len(G)):
            visited[i] = 0;
        traverse(u,visited,G)
        for i in range(len(G)):
            if not (visited[i]):
                return 0
    return 1

def gen_random_conn_graph_weighted(size): # size is num of vertices
    flag = 1
    while flag == 1:
        G = [[0] * size for i in range(size)]
        p = random.randint(1,10) # more or less roll graph density here
        print(p)
        for i in range(size):
            for j in range(size):
                if random.randint(1,10) <= p:
                    G[i][j] = random.randint(1,10)
        for i in range(size):               #
            for j in range(size):           # making matrix
                if (j == i): G[i][j] = 0    # symetric
                if (j<i): G[i][j] = G[j][i] #
        if isConnected(G): return G


#G = gen_random_conn_graph_weighted(10)
#print(G)
