import random

import numpy as np


def init_rand_dist_matrix(num_of_nodes: int) -> np.ndarray:
    dist_mat = np.zeros((num_of_nodes, num_of_nodes))
    for row in range(num_of_nodes):
        for col in range(num_of_nodes):
            if row == col:
                dist_mat[row, col] = 0
            else:
                dist_mat[row, col] = random.randint(5, 30)
    return dist_mat


def print_matrix(matrix: np.ndarray, name=None) -> None:
    if name:
        print(f"{name} =")
    else:
        print("Matrix = ")
    for row in matrix:
        for elem in row:
            print("%2d " % elem, end='')
        print()


def get_graph_centre(dist_matrix: np.ndarray) -> int:
    num_of_nodes = len(dist_matrix)
    sum_distances = [0] * num_of_nodes
    for row in range(num_of_nodes):
        for col in range(num_of_nodes):
            sum_distances[col] += dist_matrix[row][col]
    return sum_distances.index(min(sum_distances)) + 1


def get_minimax_centre(dist_matrix: np.ndarray) -> int:
    num_of_nodes = len(dist_matrix)
    max_distances = [0] * num_of_nodes
    for row in range(num_of_nodes):
        for col in range(num_of_nodes):
            max_distances[col] = max(dist_matrix[row][col], max_distances[col])
    return max_distances.index(min(max_distances)) + 1


def main() -> None:
    distances = init_rand_dist_matrix(8)
    print_matrix(distances, "Rand distance matrix")
    center_idx = get_graph_centre(distances)
    print(f"Center of graph is in node {center_idx}")
    minimax_idx = get_minimax_centre(distances)
    print(f"Minimax center is in node {minimax_idx}")


if __name__ == "__main__":
    main()
