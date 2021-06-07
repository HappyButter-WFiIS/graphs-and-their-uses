from FlowNetworkPlotter import FlowNetworkPlotter

example_graph = [
    [0, 2, 5, 1, 0, 0, 0],
    [0, 0, 0, 3, 9, 4, 0],
    [0, 2, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 2, 0, 4],
    [0, 0, 0, 0, 0, 0, 0]
]
example_layers = [0, 1, 1, 1, 2, 2, 3]

plotter = FlowNetworkPlotter()
plotter.load_network(graph=example_graph, layers=example_layers)
plotter.plot()