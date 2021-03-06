import sys
from random import randint, random
from math import exp
from copy import deepcopy
from utils.Graph import Graph

def find_closest_neighbour_path(vertex: int, path_length: float, visited: list, path: list, matrix: list) -> float:
    visited[vertex] = True
    min_val = sys.float_info.max
    min_node = -1

    for i in range(len(matrix[vertex])):
        if visited[i] == False and min_val > matrix[vertex][i]:
            min_val = matrix[vertex][i]
            min_node = i
    
    if min_node == -1:
        path_length += matrix[vertex][0]
        path.append(0)
        return path_length

    else:
        path_length += min_val
        path.append(min_node)
        return find_closest_neighbour_path(min_node, path_length, visited, path, matrix)

def closest_neighbour(G: Graph) -> list:
    visited = [False for _ in range(len(G.repr))]
    path = [0]

    path_length = find_closest_neighbour_path(0, 0.0, visited, path, G.repr)

    print('\n--- Closest Neighbour Algorithm ---\n')
    print('Path:')
    print('[' + ' - '.join([str(x + 1) for x in path]) + ']\n')
    print('Length:')
    print(path_length)
    print('-------------------------\n')

    return path

def find_path_length(path: list, matrix: list) -> float:
    result = 0.0
    for i in range(len(path)-1):
        result += matrix[path[i]][path[i+1]]
    
    return result

def simulated_annealing(G: Graph, start_temp: int, iter_max: int, repeat: int, path: list = []) -> list:
    if len(G.repr) < 5:
        print('Graph is too small for this algorithm!')
        return []
    
    if path == []:
        P = [x for x in range(len(G.repr))]
        P.append(0)
    else:
        P = path
    
    step = -start_temp // 5
    global_best_path = P
    global_best_len = find_path_length(P, G.repr)

    for counter in range(repeat): #repeats
        print('Loop: ' + str(counter + 1))

        for step_temp in range(start_temp, 0, step): #waterfalls
            for i in range(step_temp, 0, -1): #cooling
                T = 0.001*i*i

                for _ in range(iter_max):
                    Pnew = deepcopy(P)
                    
                    a = 0
                    b = 0
                    c = 0
                    d = 0

                    while a == c or b == d:
                        a = randint(1, len(P) - 3)
                        b = a + 1

                        c = randint(1, len(P) - 3)
                        d = c + 1

                    Pnew[b], Pnew[c] = Pnew[c], Pnew[b]

                    lenP = find_path_length(P, G.repr)
                    lenPnew = find_path_length(Pnew, G.repr)

                    if lenP > lenPnew or random() < exp(-(lenPnew - lenP)/T):
                        P = Pnew

                        if global_best_len > lenPnew:
                            global_best_path = Pnew
                            global_best_len = lenPnew
                    
    
    print('\n--- Simulated Annealing Algorithm ---\n')

    if path != []:
        print('Initial path was given by parameter')

    print('Starting temperature: ' + str(start_temp))
    print('ITER_MAX: ' + str(iter_max))
    print('Repeats: ' + str(repeat))
    print('Path:')
    print('[' + ' - '.join([str(x + 1) for x in global_best_path]) + ']\n')
    print('Length:')
    print(global_best_len)
    print('-------------------------\n')

    return global_best_path








