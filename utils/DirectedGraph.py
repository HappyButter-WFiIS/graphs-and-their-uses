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
            adjmat_repr.append(list([None] * count_nodes))

            for value in row:
                adjmat_repr[i][value - 1] = self.repr[i][value]

        self.repr = adjmat_repr
        self.repr_type = RepresentationType.ADJACENCY_MATRIX

    def __from_incmat_to_adjmat(self) -> None:
        count_edges = self.__count_edges()

        count_nodes = len(self.repr)
        adjmat_repr = [[None for _ in range(count_nodes)] for __ in range(count_nodes)]

        for edge_index in range(count_edges):
            edge = [-1, -1]
            weight = -1
            for vertex_index in range(count_nodes):
                if self.repr[vertex_index][edge_index] == '.':
                    edge[0] = vertex_index
                elif self.repr[vertex_index][edge_index] is not None:
                    edge[1] = vertex_index
                    weight = self.repr[vertex_index][edge_index]
            if edge != [-1, -1]:
                adjmat_repr[edge[0]][edge[1]] = weight

        self.repr = adjmat_repr
        self.repr_type = RepresentationType.ADJACENCY_MATRIX

    """
    To Adjacency List
    """

    def __from_adjmat_to_adjlist(self) -> None:
        adjlist_repr = list()

        for i, row in enumerate(self.repr):
            adjlist_repr_row = dict()

            for j, element in enumerate(row):
                if element is not None:
                    adjlist_repr_row[j+1] = element

            adjlist_repr.append(adjlist_repr_row)

        self.repr = adjlist_repr
        self.repr_type = RepresentationType.ADJACENCY_LIST

    def __from_incmat_to_adjlist(self) -> None:
        count_edges = self.__count_edges()
        count_nodes = len(self.repr)
        adjlist_repr = list()

        for _ in range(count_nodes):
            adjlist_repr.append(dict())

        for edge_index in range(count_edges):
            edge = [-1, -1]
            weight = -1
            for vertex_index in range(count_nodes):
                if self.repr[vertex_index][edge_index] == '.':
                    edge[0] = vertex_index
                elif self.repr[vertex_index][edge_index] is not None:
                    edge[1] = vertex_index
                    weight = self.repr[vertex_index][edge_index]
            if edge != [-1, -1]:
                adjlist_repr[edge[0]][edge[1] + 1] = weight

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
            incmat_repr.append(list([None] * count_edges))

        # fill matrix with apropriate values
        current_edge = 0

        for i, row in enumerate(self.repr):
            for j in range(count_nodes):
                if row[j] is not None:
                    incmat_repr[i][current_edge] = '.' #starting node
                    incmat_repr[j][current_edge] = row[j]
                    current_edge += 1

        self.repr = incmat_repr
        self.repr_type = RepresentationType.INCIDENCE_MATRIX

    def __from_adjlist_to_incmat(self) -> None:
        count_edges = self.__count_edges()
        count_nodes = len(self.repr)
        edges_list = list()
        incmat_repr = list()

        for index, row in enumerate(self.repr):
            for vertex in row.items():
                edge = (index, vertex[0] - 1, vertex[1])
                if edge not in edges_list:
                    edges_list.append(edge)

        for i in range(count_nodes):
            incmat_repr.append(list([None] * count_edges))

        for edge_index, edge in enumerate(edges_list):
            incmat_repr[edge[0]][edge_index] = '.'
            incmat_repr[edge[1]][edge_index] = edge[2]

        self.repr = incmat_repr
        self.repr_type = RepresentationType.INCIDENCE_MATRIX


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
                sum_edges += np.sum(1 for x in line if x is not None)

        elif self.repr_type == RepresentationType.INCIDENCE_MATRIX:
            sum_edges = len(self.repr[0])

        elif self.repr_type == RepresentationType.GRAPH_SEQUENCE:
            sum_edges = sum(self.repr)

        return int(sum_edges)
