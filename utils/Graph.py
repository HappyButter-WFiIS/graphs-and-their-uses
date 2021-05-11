from enum import Enum
from copy import deepcopy


class RepresentationType(Enum):
    """
    Enumeration class denoting diffrent types of graph representations.
    """
    EMPTY = 0
    ADJACENCY_MATRIX = 1
    ADJACENCY_LIST = 2
    INCIDENCE_MATRIX = 3
    GRAPH_SEQUENCE = 4
    ADJACENCY_MATRIX_WITH_WEIGHTS = 5
    ADJACENCY_LIST_WITH_WEIGHTS = 6


class Graph:

    def __init__(self):
        """
        Simple class constructor
        self.repr - list for graph representation
        self.repr_type - type of graph representation 
        """
        self.repr = list()
        self.repr_type = RepresentationType.EMPTY

    def __str__(self):
        """
        Returns string containing current graph representation.
        """
        result = ''
        if self.repr_type == RepresentationType.GRAPH_SEQUENCE:
            result = str(self.repr)
        else:
            for index, row in enumerate(self.repr):
                if self.repr_type == RepresentationType.ADJACENCY_LIST:
                    result += str(index + 1) + '. '
                for elem in row:
                    result += str(elem) + ' '
                result += '\n'
        return result

    """
    Creating various representations
    """

    def create_representation(self, filename: str, representation_type: RepresentationType) -> None:
        """
        Creates graph from file in given representation. 
        """
        self.repr_type = representation_type
        self.__create(self.__read_file(filename))

    def load_data(self, data: list, representation_type: RepresentationType) -> bool:
        """
        Loads graph from data in given representation.
        Returns False in case when given data is not graphical sequence, otherwise True.  
        """
        self.repr_type = representation_type
        self.repr = data
        if self.repr_type == RepresentationType.GRAPH_SEQUENCE and self.__is_graphical() == False:
            return False
        return True

    def __read_file(self, filename: str) -> str:
        try:
            file = open(filename, 'r')
            return file.read().split('\n')
        except IOError:
            print("Wrong filename")
            return ''

    def __create(self, content: str) -> None:
        self.repr.clear()

        for line in content:
            row = list()
            line = line.split(' ')

            if self.repr_type == RepresentationType.ADJACENCY_LIST:
                line = line[1:]
            for elem in line:
                try:
                    row.append(int(elem))
                except ValueError:
                    return
            self.repr.append(row)

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
        adjmat_repr = list()

        for i, row in enumerate(self.repr):
            adjmat_repr.append(list([0] * count_nodes))

        for edge_index in range(count_edges):
            edge = list()
            for vertex_index in range(count_nodes):
                if self.repr[vertex_index][edge_index] == 1:
                    edge.append(vertex_index)
            adjmat_repr[edge[0]][edge[1]] = 1
            adjmat_repr[edge[1]][edge[0]] = 1

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

        for index in range(count_nodes):
            adjlist_repr.append(list())

        for edge_index in range(count_edges):
            edge = list()
            for vertex_index in range(count_nodes):
                if self.repr[vertex_index][edge_index] == 1:
                    edge.append(vertex_index)
            adjlist_repr[edge[0]].append(edge[1] + 1)
            adjlist_repr[edge[1]].append(edge[0] + 1)

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
            for j in range(i):
                if (row[j] == 1):
                    incmat_repr[i][current_edge] = 1
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
                if edge not in edges_list and (vertex - 1, index) not in edges_list:
                    edges_list.append(edge)

        for i in range(count_nodes):
            incmat_repr.append(list([0] * count_edges))

        for edge_index, edge in enumerate(edges_list):
            incmat_repr[edge[0]][edge_index] = 1
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
                adjacency_list[enumerated_data[i][0]].append(enumerated_data[j][0] + 1)
                adjacency_list[enumerated_data[j][0]].append(enumerated_data[i][0] + 1)
                enumerated_data[i][1] -= 1
                enumerated_data[j][1] -= 1
                j += 1

        self.repr = adjacency_list
        self.repr_type = RepresentationType.ADJACENCY_LIST

    """
    To Graphical Sequence
    """

    def __from_adjmat_to_sequence(self) -> None:
        graphical_sequence = [sum(x) for x in self.repr]

        self.repr = graphical_sequence
        self.repr_type = RepresentationType.GRAPH_SEQUENCE

    def __from_adjlist_to_sequence(self) -> None:
        graphical_sequence = [len(x) for x in self.repr]

        self.repr = graphical_sequence
        self.repr_type = RepresentationType.GRAPH_SEQUENCE
    
    def __from_incmat_to_sequence(self) -> None:
        graphical_sequence = [sum(x) for x in self.repr]

        self.repr = graphical_sequence
        self.repr_type = RepresentationType.GRAPH_SEQUENCE

    """
    Helper methods
    """

    def __count_edges(self) -> int:
        sum_edges = 0

        if self.repr_type == RepresentationType.ADJACENCY_LIST:
            for line in self.repr:
                sum_edges += len(line)
            sum_edges = sum_edges / 2

        elif self.repr_type == RepresentationType.ADJACENCY_MATRIX:
            for line in self.repr:
                sum_edges += sum(line)
            sum_edges = sum_edges / 2

        elif self.repr_type == RepresentationType.INCIDENCE_MATRIX:
            sum_edges = len(self.repr[0])

        elif self.repr_type == RepresentationType.GRAPH_SEQUENCE:
            sum_edges = sum(self.repr) / 2

        return int(sum_edges)

    def __is_graphical(self) -> bool:
        data = deepcopy(self.repr)
        for _ in range(len(data)):
            data.sort(reverse=True)
            item = data[0]
            data[0] = 0
            for i in range(1, item + 1):
                data[i] -= 1
                if data[i] == -1:
                    return False

        return True

    def is_k_regular(self, k: int) -> bool:
        if self.repr_type == RepresentationType.ADJACENCY_MATRIX:
            for line in self.repr:
                current_k = len(line) - line.count(0)

                if current_k != k:
                    return False

            return True

        print("Transform to ADJACENCY_MATRIX first.")
        return False

    def get_weighted_adjacency_list(self) -> dict:
        if self.repr_type == RepresentationType.ADJACENCY_MATRIX_WITH_WEIGHTS:
            adjlist_repr = {}

            for i, row in enumerate(self.repr):
                adjlist_repr_row = {}

                for j, element in enumerate(row):
                    if (element != 0):
                        adjlist_repr_row[j + 1] = element

                adjlist_repr[i + 1] = (adjlist_repr_row)
            return adjlist_repr
        return {}

        
