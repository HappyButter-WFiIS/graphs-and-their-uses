from utils.DirectedGraph import DirectedGraph, RepresentationType
from algorithms.bellman_ford import bellman_ford
from algorithms.dijkstra import find_shortest_path
from utils.graph_plotter import GraphPlotter
from utils.Graph import Graph
from utils.graph_generators import get_graph_with_probability, get_connected_digraph


def johnson_algorithm(graph: DirectedGraph) -> list:
    if graph.repr_type != RepresentationType.ADJACENCY_MATRIX:
        graph.to_adjacency_matrix()
        
    g = graph.repr

    # add vertex to graph and add edges of value 0 from this vertex to the rest
    g.append([0])
    for i in range(len(g)-2):
        g[len(g)-1].append(0)

    for i in range(len(g)):
        g[i].append(None)

    graph.to_adjacency_list()
    edges = bellman_ford(graph, len(g))
    edges.pop(len(g))
    graph.to_adjacency_matrix()

    new_g = [[0 for x in range(len(g)-1)] for y in
                    range(len(g)-1)]

    for i in range(len(new_g)):
        for j in range(len(new_g[i])):
            if g[i][j] is not None:
                new_g[i][j] = (g[i][j] +
                    edges[i+1] - edges[j+1])

    graph.repr.pop()
    for i in range(len(graph.repr)):
        graph.repr[i].pop()

    graph_for_dijkstra = Graph()
    data = get_graph_with_probability(len(graph.repr), 0.5)
    graph_for_dijkstra.load_data(data=data, representation_type=RepresentationType.ADJACENCY_MATRIX_WITH_WEIGHTS)

    for i in range(len(graph.repr)):
        for j in range(len(graph.repr[i])):
                graph_for_dijkstra.repr[i][j] = new_g[i][j]

    dist_matrix = []
    for s in range(len(graph_for_dijkstra.repr)):
        print(f"For node [{s+1}]:")
        from_point = find_shortest_path(G=graph_for_dijkstra.get_weighted_adjacency_list(), start=s+1, verbose=True)
        dist_matrix.append([])
        for node in from_point:
            dist_matrix[s].append(from_point[node])
        print()
    return dist_matrix

    # GraphPlotter.plot_graph(graph_for_dijkstra)


if __name__ == "__main__":
    randomgraph = get_connected_digraph(5, 0.2, -5, 10)
    randomgraph.to_adjacency_matrix()
    johnson_algorithm(randomgraph)
    print("gg")

