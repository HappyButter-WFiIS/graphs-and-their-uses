# Lab 4

## How to use
[1] Launch the app by executing command: `python3 lab/lab04/lab04_console.py` from the project directory.

[2] You should see a prompt and a list of available options.

[3] By typing in an option code given in `[]` you choose an option.

[4] Follow the further instructions given by the particular option.

## Options description

###[1] Generate random directed graph
As the name says. The program will ask you to pass some parameters:

- `Number of nodes` - a positive integer, if you give wrong input it will assume a number is equal to 1.
- `Probability(0-1)` - a real number from 0 to 1 describing the probability of edge being created.
- `Lowest possible weight` - integer. Weights are random for each node and this is the lower boundary of random range. 
- `Lowest possible weight` - as above.

If everything was correct you should see a `Success` message.

###[2] Generate strongly consistent digraph
This option requires the same arguments as above, but generates a graph which has only one component.

If everything was correct you should see a `Success` message.

Sometimes graph couldn't be generated due to limited number of tries. The program will signalize it by `Error` message.

###[3] Find strongly consistent components (Kosaraju algorithm)
This option will search for strongly consistent components in the generated graph. 
After completion, it will assign a colours to the nodes of the graph, therefore they can be plotted.

If everything was correct you should see a `Success` message and also a graph plot.
In order to complete the option, close the plot.

###[4] Find shortest paths from one node to the rest (Bellman-Ford algorithm)

This option will plot the shortest paths from the given node to the rest. 
You will be asked for a parameter:
- `Start from` - a starting node for the algorithm

If success, the program will print the values of the shortest paths.
`Inf` means that there is no path leading to the node (the cost of travel is infinite).

###[5] Find all distances between pairs (Johnson algorithm)

This option will plot the distances from each node to another, plus the path leading trough nodes.
The distances and path are the shortest possible.

###[p] Print graph
Print the graph and its representation type.

###[t] Plot graph
Plots the graph. You will be redirected to a submenu which gives you some options:

- [1] `Normal (all options on)` - plot edges with wages and their direction, and gives separate colors to each strongly consistent component.
It would use only one color if components were not generated. generate them first by using `[3]` option from main menu.

- [2] `Without groups` - this will plot graph with only one color for all nodes.

- [3] `Without wages` - coloured components without wages on edges.

- [4] `Nodes and edges only` - basic edges without wages and one colour for nodes.

- [b] `Go back` - Go to main menu.

###[q] Quit

Exits the program.