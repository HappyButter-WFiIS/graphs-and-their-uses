from enum import Enum

class RepresentationType(Enum):
    EMPTY = 0
    ADJ_MAT = 1
    ADJ_LIST = 2
    INC_MAT = 3

class GraphRepresentation:

    def __init__(self):
        self.repr = list()
        self.repr_type = RepresentationType.EMPTY
    
    def __str__(self):
        result = ''
        for index, row in enumerate(self.repr):
            if self.repr_type == RepresentationType.ADJ_LIST:
                result += str(index + 1) + '. '
            for elem in row:
                result += str(elem) + ' '
            result += '\n'
        return result
    """
    Creating various representations from file
    """
    def create_adjacency_matrix(self, filename: str):
        self.repr_type = RepresentationType.ADJ_MAT
        self.__create(self.__read_file(filename))
        print(self)
    
    def create_adjacency_list(self, filename: str):
        self.repr_type = RepresentationType.ADJ_LIST
        self.__create(self.__read_file(filename))
        print(self)

    def create_incidence_matrix(self, filename: str):
        self.repr_type = RepresentationType.INC_MAT
        self.__create(self.__read_file(filename))
        print(self)

    def __read_file(self, filename: str): 
        try:
            file = open(filename, 'r')
            return file.read().split('\n')
        except IOError:
            print("Wrong filename")
            return ''

    def __create(self, content: str):
        self.repr.clear()
        for line in content:
            row = list()
            line = line.split(' ')
            if self.repr_type == RepresentationType.ADJ_LIST:
                line = line[1:]
            for elem in line:
                row.append(int(elem))
            self.repr.append(row)
    """
    Transform representations
    """
    def to_adjacency_matrix(self):
        if self.repr_type == RepresentationType.ADJ_LIST:
            self.__from_adjlist_to_adjmat()
        elif self.repr_type == RepresentationType.INC_MAT:
            self.__from_incmat_to_adjmat()
        print(self)

    def to_adjacency_list(self):
        if self.repr_type == RepresentationType.ADJ_MAT:
            self.__from_adjmat_to_adjlist()
        elif self.repr_type == RepresentationType.INC_MAT:
            self.__from_incmat_to_adjlist()
        print(self)
    
    def to_incidence_matrix(self):
        if self.repr_type == RepresentationType.ADJ_LIST:
            self.__from_adjlist_to_incmat()
        elif self.repr_type == RepresentationType.ADJ_MAT:
            self.__from_adjmat_to_incmat()
        print(self)
    """
    To Adjacency Matrix
    """
    def __from_adjlist_to_adjmat(self):
        pass
    
    def __from_incmat_to_adjmat(self):
        pass
    """
    To Adjacency List
    """
    def __from_adjmat_to_adjlist(self):
        pass

    def __from_incmat_to_adjlist(self):
        pass
    """
    To Incidence Matrix
    """
    def __from_adjmat_to_incmat(self):
        pass

    def __from_adjlist_to_incmat(self):
        pass




