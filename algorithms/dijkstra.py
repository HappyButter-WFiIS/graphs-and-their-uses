def create_path_list(destination: int, start: int, predecessos: dict) -> list:
    path = []
    current_node = destination

    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessos[current_node]
        except KeyError:
            # raise KeyError
            print(f"d({destination})  = Inf")
            break

    path.insert(0, start)
    return path


def find_shortest_path(G: dict, start: int, verbose: bool):
    # set variables
    not_reached_nodes = G.copy()
    infinity = float('inf')
    shortest_distance = {}
    predecessors = {}

    for node in not_reached_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    # searching optimal path
    while not_reached_nodes:

        min_distance_node = None

        # check neighbours
        for node in not_reached_nodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = G[min_distance_node].items(
        )

        # Dijkstra main part
        for child_node, weight in path_options:

            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                predecessors[child_node] = min_distance_node

        not_reached_nodes.pop(min_distance_node)

    for dest in range(1, len(G)+1):

        path = create_path_list(dest, start, predecessors)
        if shortest_distance[dest] != infinity:
            if verbose:
                print("d({})  = {} ==> {}".format(
                    dest, str(shortest_distance[dest]), str(path)), end="\n")

    return shortest_distance
