import os, sys
import numpy as np

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from random import randint
from utils.graph_plotter import GraphPlotter
from utils.Graph import Graph, RepresentationType
from utils.graph_generators import get_graph_from_points
from algorithms.salesman import closest_neighbour, simulated_annealing

if __name__ == '__main__':
    G = Graph()
    points = list()

    for _ in range(50):
        points.append((randint(-100,100), randint(-100, 100))) 
    
    G.load_data(get_graph_from_points(points), RepresentationType.ADJACENCY_MATRIX)

    path = closest_neighbour(G)
    GraphPlotter.plot_points(points, path)
    path = simulated_annealing(G, 100, 1000)
    GraphPlotter.plot_points(points, path)

    points = np.loadtxt(os.path.dirname(__file__) + '/inputs/input59.dat', usecols=(0,1))
    G.load_data(get_graph_from_points(points), RepresentationType.ADJACENCY_MATRIX)

    path = closest_neighbour(G)
    GraphPlotter.plot_points(points, path)
    path = simulated_annealing(G, 100, 1000, path)
    GraphPlotter.plot_points(points, path)


