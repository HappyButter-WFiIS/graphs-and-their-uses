import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import numpy as np
from random import random
from utils.Graph import Graph, RepresentationType
from utils.graph_generators import get_graph_from_points
from utils.graph_plotter import GraphPlotter
from algorithms.salesman import closest_neighbour, simulated_annealing


def display_menu() -> None:
    print('\n[1] Create graph from points')
    print('[2] Find cycle')
    print('[q] Quit')


def create_graph(G: Graph) -> None:
    print('\n[1] Read points from file')
    print('[2] Generate random points')

    if G.repr_type != RepresentationType.EMPTY:
        G.repr_type = RepresentationType.EMPTY
        print('\nOld graph has been deleted')

    points = []

    option = input("\nChoose option\n")
    if option == '1':
        print("\nOk. Now put the file name.")
        filename = input('Filename: ')
        points = np.loadtxt(os.path.dirname(__file__) + '/' + filename, usecols=(0,1))
        
        G.load_data(get_graph_from_points(points), RepresentationType.ADJACENCY_MATRIX)
        print('\nGraph created!\n')

    if option == '2':
        print('\nPut number of points')
        num = int(input('Number: '))

        for _ in range(num):
            points.append((2000*random()-1000, 2000*random()-1000))

        G.load_data(get_graph_from_points(points), RepresentationType.ADJACENCY_MATRIX)
        print('\nGraph created!\n')
    
    return points


def find_cycle(G: Graph, points: list) -> None:
    if G.repr_type == RepresentationType.EMPTY:
        print('\nGraph is empty! First try to create it.')
    else:
        print('\n[1] Closest Neighbour Algorithm')
        print('[2] Simulated Annealing Algorithm')
        print('[3] Combine two algorithms')

        option = input("\nChoose option\n")

        if option == '1':
            GraphPlotter.plot_points(points, closest_neighbour(G))

        if option == '2':
            print('\nChoose how many times algorithms should be repeated (int)')
            repeat = int(input('Repeats: '))
            print('\nChoose starting temperature (int)')
            temp = int(input('Temperature: '))
            print('\nChoose number of iterations (int)')
            iter_max = int(input('ITER_MAX: '))
            path = simulated_annealing(G, temp, iter_max, repeat)
            if path != []:
                GraphPlotter.plot_points(points, path)

        if option == '3':
            print('\nChoose how many times algorithms should be repeated (int)')
            repeat = int(input('Repeats: '))
            print('\nChoose starting temperature (int)')
            temp = int(input('Temperature: '))
            print('\nChoose number of iterations (int)')
            iter_max = int(input('ITER_MAX: '))
            path = simulated_annealing(G, temp, iter_max, repeat, path=closest_neighbour(G))
            if path != []:
                GraphPlotter.plot_points(points, path)


if __name__ == '__main__':
    points = list()
    G = Graph()
    main_choice = ''

    while main_choice != 'q':
        display_menu()
        main_choice = input("\nWhat would you like to do?\n")

        try:
            if main_choice == '1':
                points = create_graph(G)
            if main_choice == '2':
                find_cycle(G, points)
        
        except:
            print('Something went wrong. Try again!')
        
    print("\nThanks for playing. Bye.")