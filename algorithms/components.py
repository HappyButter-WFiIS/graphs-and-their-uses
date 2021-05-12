from utils.Graph import Graph


def get_index_of_max_value(values: list) -> int:
    """
    A helper function which returns the index from a list-of-lists,
    for which the list corresponding to it has the biggest length.
    """
    list_sizes = [len(item) for item in values]
    return list_sizes.index(max(list_sizes))


def get_components(graph: Graph) -> list:
    """
    Creates a list which contains labels for Graph nodes.
    Same value means the same component of the Graph.
    """
    def visit_node(idx):
        visited[idx] = True
        groups[idx] = current_group
        for j in range(len(graph[idx])):

            if not visited[graph[idx][j] - 1]:
                visit_node(graph[idx][j] - 1)

    graph = graph.repr
    node_count = len(graph)
    visited = [False] * node_count
    groups = [None] * node_count
    current_group = 0

    for i in range(node_count):

        if not visited[i]:
            visit_node(i)
            current_group += 1

    return groups


def print_sorted_components(graph: Graph, groups: list) -> int:
    """
    Prints Graph node indices sorted into components.
    Also prints and returns the biggest component.
    """
    graph = graph.repr
    num_of_groups = max(groups)+1
    sorted_groups = []
    for i in range(num_of_groups):
        sorted_groups.append([])
    for i in range(len(graph)):
        sorted_groups[groups[i]].append(i+1)

    print("Components:")

    for i in range(len(sorted_groups)):
        print("%d) " % (i+1), end='')
        separator = ''
        for node in sorted_groups[i]:
            print("%s%d " % (separator, node), end='')
            separator = ''
        print()

    biggest = get_index_of_max_value(sorted_groups) + 1

    print(f"Biggest component has index: {biggest}.")

    return biggest
