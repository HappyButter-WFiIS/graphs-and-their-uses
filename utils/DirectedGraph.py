from enum import Enum
from copy import deepcopy
import numpy as np

from algorithms.dijkstra import find_shortest_path
from utils.Graph import Graph, RepresentationType


class DirectedGraph(Graph):

    """
    Transform representations
    """

    def to_adjacency_matrix(self) -> None:
        if self.repr_type == RepresentationType.ADJACENCY_LIST:
            self.__from_adjlist_to_adjmat()
        elif self.repr_type == RepresentationType.INCIDENCE_MATRIX:
            self.__from_incmat_to_adjmat()
        elif self.repr_type == RepresentationType.GRAPH_SEQUENCE:
            self.__from_sequence_to_adjlist()
            self.__from_adjlist_to_adjmat()

    def to_adjacency_list(self) -> None:
        if self.repr_type == RepresentationType.ADJACENCY_MATRIX:
            self.__from_adjmat_to_adjlist()
        elif self.repr_type == RepresentationType.INCIDENCE_MATRIX:
            self.__from_incmat_to_adjlist()
        elif self.repr_type == RepresentationType.GRAPH_SEQUENCE:
            self.__from_sequence_to_adjlist()

    def to_incidence_matrix(self) -> None:
        if self.repr_type == RepresentationType.ADJACENCY_LIST:
            self.__from_adjlist_to_incmat()
        elif self.repr_type == RepresentationType.ADJACENCY_MATRIX:
            self.__from_adjmat_to_incmat()
        elif self.repr_type == RepresentationType.GRAPH_SEQUENCE:
            self.__from_sequence_to_adjlist()
            self.__from_adjlist_to_incmat()

    def to_graphical_sequence(self) -> None:
        if self.repr_type == RepresentationType.ADJACENCY_LIST:
            self.__from_adjlist_to_sequence()
        elif self.repr_type == RepresentationType.ADJACENCY_MATRIX:
            self.__from_adjmat_to_sequence()
        elif self.repr_type == RepresentationType.INCIDENCE_MATRIX:
            self.__from_incmat_to_sequence()

    """
    To Adjacency Matrix
    """

    def __from_adjlist_to_adjmat(self) -> None:
        adjmat_repr = list()
        count_nodes = len(self.repr)

        for i, row in enumerate(self.repr):
            adjmat_repr.append(list([0] * count_nodes))

            for value in row:
                adjmat_repr[i][value - 1] = 1

        self.repr = adjmat_repr
        self.repr_type = RepresentationType.ADJACENCY_MATRIX

    def __from_incmat_to_adjmat(self) -> None:
        count_edges = self.__count_edges()

        count_nodes = len(self.repr)
        adjmat_repr = [[0 for _ in range(count_nodes)] for __ in range(count_nodes)]

        for edge_index in range(count_edges):
            edge = [-1, -1]
            for vertex_index in range(count_nodes):
                if self.repr[vertex_index][edge_index] == -1:
                    edge[0] = vertex_index
                if self.repr[vertex_index][edge_index] == 1:
                    edge[1] = vertex_index
            if edge != [-1, -1]:
                adjmat_repr[edge[0]][edge[1]] = 1

        self.repr = adjmat_repr
        self.repr_type = RepresentationType.ADJACENCY_MATRIX

    """
    To Adjacency List
    """

    def __from_adjmat_to_adjlist(self) -> None:
        adjlist_repr = list()

        for i, row in enumerate(self.repr):
            adjlist_repr_row = list()

            for j, element in enumerate(row):
                if (element == 1):
                    adjlist_repr_row.append(j + 1)

            adjlist_repr.append(adjlist_repr_row)

        self.repr = adjlist_repr
        self.repr_type = RepresentationType.ADJACENCY_LIST

    def __from_incmat_to_adjlist(self) -> None:
        count_edges = self.__count_edges()
        count_nodes = len(self.repr)
        adjlist_repr = list()

        for _ in range(count_nodes):
            adjlist_repr.append(list())

        for edge_index in range(count_edges):
            edge = [-1, -1]
            for vertex_index in range(count_nodes):
                if self.repr[vertex_index][edge_index] == -1:
                    edge[0] = vertex_index
                if self.repr[vertex_index][edge_index] == 1:
                    edge[1] = vertex_index
            if edge != [-1, -1]:
                adjlist_repr[edge[0]].append(edge[1] + 1)

        self.repr = adjlist_repr
        self.repr_type = RepresentationType.ADJACENCY_LIST

    """
    To Incidence Matrix
    """

    def __from_adjmat_to_incmat(self) -> None:
        incmat_repr = list()

        count_edges = self.__count_edges()
        count_nodes = len(self.repr)

        # prepare matrix filled with zeros
        for i in range(count_nodes):
            incmat_repr.append(list([0] * count_edges))

        # fill matrix with apropriate values
        current_edge = 0

        for i, row in enumerate(self.repr):
            for j in range(count_nodes):
                if (row[j] == 1):
                    incmat_repr[i][current_edge] = -1
                    incmat_repr[j][current_edge] = 1
                    current_edge += 1

        self.repr = incmat_repr
        self.repr_type = RepresentationType.INCIDENCE_MATRIX

    def __from_adjlist_to_incmat(self) -> None:
        count_edges = self.__count_edges()
        count_nodes = len(self.repr)
        edges_list = list()
        incmat_repr = list()

        for index, row in enumerate(self.repr):
            for vertex in row:
                edge = (index, vertex - 1)
                if edge not in edges_list:
                    edges_list.append(edge)

        for i in range(count_nodes):
            incmat_repr.append(list([0] * count_edges))

        for edge_index, edge in enumerate(edges_list):
            incmat_repr[edge[0]][edge_index] = -1
            incmat_repr[edge[1]][edge_index] = 1

        self.repr = incmat_repr
        self.repr_type = RepresentationType.INCIDENCE_MATRIX

    def __from_sequence_to_adjlist(self) -> None:
        enumerated_data = [[idx, conn] for idx, conn in enumerate(self.repr)]
        adjacency_list = [[] for _ in range(len(enumerated_data))]
        for _ in range(len(enumerated_data)):
            enumerated_data.sort(reverse=True, key=lambda x: x[1])
            i = 0
            j = 1
            while enumerated_data[i][1] > 0 and j < len(enumerated_data):
                adjacency_list[enumerated_data[i][0]].append(
                    enumerated_data[j][0] + 1)
                adjacency_list[enumerated_data[j][0]].append(
                    enumerated_data[i][0] + 1)
                enumerated_data[i][1] -= 1
                enumerated_data[j][1] -= 1
                j += 1

        self.repr = adjacency_list
        self.repr_type = RepresentationType.ADJACENCY_LIST

    """
    To Graphical Sequence
    """

    def __from_adjmat_to_sequence(self) -> None:
        print("You cannot convert ADJACENCY_MATRIX into GRAPH_SEQUENCE within digraph")

    def __from_adjlist_to_sequence(self) -> None:
        print("You cannot convert ADJACENCY_LIST into GRAPH_SEQUENCE within digraph")

    def __from_incmat_to_sequence(self) -> None:
        print("You cannot convert INCIDENCE_MATRIX into GRAPH_SEQUENCE within digraph")

    """
    Helper methods
    """

    def __count_edges(self) -> int:
        sum_edges = 0

        if self.repr_type == RepresentationType.ADJACENCY_LIST:
            for line in self.repr:
                sum_edges += len(line)

        elif self.repr_type == RepresentationType.ADJACENCY_MATRIX:
            for line in self.repr:
                sum_edges += np.count_nonzero(line)

        elif self.repr_type == RepresentationType.INCIDENCE_MATRIX:
            sum_edges = len(self.repr[0])

        elif self.repr_type == RepresentationType.GRAPH_SEQUENCE:
            sum_edges = sum(self.repr)

        return int(sum_edges)
