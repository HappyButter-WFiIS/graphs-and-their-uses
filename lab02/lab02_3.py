from utils.GraphRepresentation import GraphRepresentation, RepresentationType
from utils.GraphPlotter import plot_graph


def max_len(lst):
    max = 0
    for i in range(len(lst)):
        if len(lst[i]) > len(lst[max]):
            max = i
    return max


def search(G):

    def visit_node(i):
        visited[i] = True
        groups[i] = current_group
        for j in range(len(G[i])):

            if not visited[G[i][j]-1]:
                visit_node(G[i][j]-1)

    G = G.repr
    node_count = len(G)
    visited = [False] * node_count
    groups = [None] * node_count
    current_group = 0

    for i in range(node_count):

        if not visited[i]:
            visit_node(i)
            current_group += 1

    return groups


def sort_groups(G, groups):
    G = G.repr
    numof_groups = max(groups)+1
    sorted_groups = []
    for i in range(numof_groups):
        sorted_groups.append([])
    for i in range(len(G)):
        sorted_groups[groups[i]].append(i+1)

    for i in range(len(sorted_groups)):
        print("%d) " % (i+1), end='')
        separator = ''
        for node in sorted_groups[i]:
            print("%s%d " % (separator, node), end='')
            separator = ''
        print()
    print("Najwieksza wspolna skladowa ma numer %d." %
          (max_len(sorted_groups) + 1))


print("Znajdowanie najwiekszej wspolnej skladowej")
G = GraphRepresentation()
G.load_data([4, 2, 2, 3, 1, 3, 4, 1, 2, 2, 2],
            RepresentationType.GRAPH_SEQUENCE)
G.to_adjacency_list()
groups = search(G)

sort_groups(G, groups)
G.to_adjacency_matrix()
plot_graph(G.repr, groups)
