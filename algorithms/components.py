
def get_index_of_max_value(values: list):
    return values.index(max(values))    


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
          (get_index_of_max_value(sorted_groups) + 1))
