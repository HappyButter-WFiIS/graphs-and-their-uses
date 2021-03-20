from enum import Enum

class Representation(Enum):
    EMPTY = 0
    ADJ_MAT = 1
    ADJ_LIST = 2
    INC_MAT = 3

class Graph:

    def __init__(self):
        self.repr = list()
        self.repr_type = Representation.EMPTY
    
    def __str__(self):
        result = ''
        for row in self.repr: 
            for elem in row:
                result += str(elem) + ' '
            result += '\n'
        return result

    def create_adjacency_matrix(self, content):
        self.__create_matrix(content)
        self.repr_type = Representation.ADJ_MAT
    
    def create_adjacency_list(self, content):
        pass

    def create_incidence_matrix(self, content):
        self.__create_matrix(content)
        self.repr_type = Representation.INC_MAT

    def __create_matrix(self, content):
        for line in content:
            row = list()
            line = line.split(' ')
            for elem in line:
                row.append(int(elem))
            self.repr.append(row)





