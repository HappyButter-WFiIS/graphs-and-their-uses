1. Presenting tasks from exercies set no. 3 using random graphs.
   
	There are 6 options to choose from:
   
	[1] Generate a random consisten simple graph
   
        Input:
        Expects integer value - size of the generated graph.
                
        Description:
        If input is correct the program generates a graph. If operation was successfull,
        user will see a confirmation message. In case of passing inadequate input,
        user will se a message reminding about type of expected input.
   
    [2] Use Djikstra algorithm

        Option [2] gives possibility to find the shortest paths to each node starting
        from the selected one.
        
        Input:
        Excepts integer describing node number (starting from 1).
        If input is correct, the program will print informations about
        the lenghts of the shortest paths inside the considered graph.
        Otherwise, user will se a reminder message about the expected input.

        Description:
        If input is correct and sequence is graphical than the program plots
        one of possible solutions and than asks for the number of randomizations.
        After performing randomization given number of times, plot is created again
        to check if graph changed it's appearance.

   [3] Get a distance matrix
        
        This option performs generation of a distance matrix.

        Input:
        Algorithm does not expect any input.
          
        Description:
        The program displays a matrix showing the distances between each node in 
        the graph.

    [4] Find the center
    
        This option allows to find center of a graph.
        
        Input:
        Algorithm does not expect any input.
        
        Description:
        The program display information about the node number, where center
        of the graph is located.

    [5] Find the MinMax center
    
        This option allows to find minmax center of a graph.
        
        Input: 
        Algorithm does not expect any input.

        Description: 
        The program display information about the node number, where minmax center
        of the graph is located.
        
    [6] Find the minimal spanning tree
    
        This options finds the minimal spanning tree of users graph.
        
        Input:
        Integer - number 1 or 2, where:
        '1' means that user would like to use Kruskal algorithm,
        '2' means that user would like to user Prim algorithm.
        Pressing any other key, will move user back to main menu.
        
        Description:
        After choosing algorithm option, it will find the minimal spanning tree,
        Then it will plot it and print the tree sum.

    [p] Plot the graph    
        
        Plots currently stored graph.
   
    [0] Load graph from file

        Allows to load graph directly from a file.

        Input:
        Path to a file as user was inside lab03 directory.
    
    [q] Quit
        
        Exit program option.
    
 -Note
   In case of missing graph, there will be a message displayed. User will be informed, that
   before using any algorithm, a graph needs to be generated or loaded.

 Program should be started from main folder: python lab03/Lab03_console.py
