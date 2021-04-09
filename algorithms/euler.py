from random import random
from utils.graph_generators import get_graph_with_probability

def dfs(graph: list, vertex: int) -> list:
    path = list()

    for v in graph[vertex - 1]:
        graph[vertex - 1].remove(v)
        graph[v - 1].remove(vertex)
        path += dfs(graph, v)
    
    path.append(str(vertex))
    return path
    

def euler_cycle(graph: list) -> str:
    cycle = dfs(graph, 1)
    cycle.reverse()
    return '[' + ' - '.join(cycle) + ']'

def generate_euler_graph_sequence(vertices: int) -> list:
    data = get_graph_with_probability(vertices, 0.5)
    graphical_sequence = [sum(x) for x in data]
    graphical_sequence = [x - 1 if x % 2 == 1 else x for x in graphical_sequence]
    return graphical_sequence