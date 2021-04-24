def create_path_list(destination: int, start: int, predecessos: dict) -> dict:
    path = []
    current_node = destination

    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessos[current_node]
        except KeyError:
            print("Something went wrong!")
            break

    path.insert(0, start)
    return path


def find_shortest_path(G: dict, start: int, destination: int):
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

    path = create_path_list(destination, start, predecessors)

    if shortest_distance[destination] != infinity:
        print("d({})  = {} ==> {}".format(
            destination, str(shortest_distance[destination]), str(path)))
