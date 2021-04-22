from random import randint
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
    graphical_sequence = [(randint(2, vertices-1) // 2) * 2 for _ in range(vertices)]
    return graphical_sequence