
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
