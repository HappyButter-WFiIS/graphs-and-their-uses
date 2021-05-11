import numpy as np
import heapq


def kruskal(matrix: list) -> list:
    edges = matrix_to_edges_list(matrix)
    result = np.zeros(shape = (len(matrix), len(matrix)), dtype = int)
    parent = [i for i in range(len(matrix))]
    rank = [0 for _ in range(len(matrix))]
    tree_sum = 0

    print(len(result[0]))

    for edge in edges:
        a, b = edge[1], edge[2]
        if union(a, b, parent, rank):
            tree_sum += edge[0]
            result[a][b] = edge[0]
            result[b][a] = edge[0]
    
    print("Kruskal tree sum = ", tree_sum)
    return result


def matrix_to_edges_list(matrix: list) -> list:
    result = []
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] > 0:
                result.append([matrix[i][j], i, j])
    
    result.sort()
    return result


def find_parent(x: int, parent: list) -> int:
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union(a: int, b: int, parent: list, rank: list) -> bool:
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a == b:
        return False

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        rank[a] += 1
        parent[b] = a

    return True


def prim(matrix: list) -> list:
    visited = [False for _ in range(len(matrix))]
    visited[0] = True
    result = np.zeros(shape = (len(matrix), len(matrix)), dtype = int)
    tree_sum = 0
    Q = list()

    push_edges(0, matrix[0], Q)
    while Q != []:
        edge = heapq.heappop(Q)
        a, b = edge[1], edge[2]
        if visited[b] == False:
            tree_sum += edge[0]
            result[a][b] = edge[0]
            result[b][a] = edge[0]
            visited[b] = True
            push_edges(b, matrix[b], Q)
    
    print("Prim tree sum = ", tree_sum)
    return result


def push_edges(vertex: int, row: list, Q: list):
    for i in range(len(row)):
        if row[i] > 0:
            Q.append([row[i], vertex, i])
    
    heapq.heapify(Q)
