from utils.DirectedGraph import DirectedGraph, RepresentationType

def get_edges_list(G: DirectedGraph) -> list:
    edges_list = []
        
    for u, edges in enumerate(G.repr):
        for v, w in edges.items():
            edges_list.append([u+1, v, w])
            
    return edges_list

def bellman_ford(G: DirectedGraph, start: int) -> dict:
    # init
    n = len(G.repr)
    edges = get_edges_list(G)    
    infinity = float('inf')
    shortest_distance = {}
    
    
    for i in range(n):
        shortest_distance[i+1] = infinity
    shortest_distance[start] = 0
    
    # main part
    for _ in range(n - 1):
        for u, v, w in edges:
            # relax, take it eeeeeeeeeeazy
            if shortest_distance[u] != infinity and shortest_distance[u] + w < shortest_distance[v]:
                shortest_distance[v] = shortest_distance[u] + w
           
    for u, v, w in edges:       
        if shortest_distance[u] != infinity and shortest_distance[v] > (shortest_distance[u] + w):
            raise Exception("Graph contains negative weight cycle")

    return shortest_distance
