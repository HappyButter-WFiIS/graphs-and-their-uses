- The console program consists two main options
1. Creating graph from points
   
	There are 2 options in that part to choose from:
   
	  [1] Read points from file
   
        This option allows to load sequence of floats from .dat file,
        where numbers are printed in two columns.
        Every row is interpreted as point (x,y) on the plane 
        and one single vertex of complete graph.
        
    [2] Generate random points

        This option gives possibility to generate given number of points,
        and use them to build a graph.
        Recommended number of points is between 5 and 500.
    
2. Finding cycle
    
   [1] Closest Neighbour Algorithm
    
        Option allows to find minimal Hamiltonian cycle (approximated) using Algorithm of Closest Neighbour. 
        Anwser is given as:
          - sequence of nodes
          - length of path
          - plot of graph with result path 

   [2] Simulated Annealing Algorithm
        
        Option allows to find minimal Hamiltonian cycle (approximated) using Algorithm of Simulated Annealing,
        with given parameters (integers): initial temperature and paramter of maximal iterations.
        
        Answer is given as:
          - sequence of nodes
          - length of path
          - plot of graph with result path
          - starting temperature
          - number of iterations
            
   [3] Combine two algorithms
   
        Option allows to use simultaneously two algorithms described above.
        The path is found by Closest Neighbour Algorithm and then this path is used 
        as inital path for Simulated Annealing Algorithm.
        
        Answer is given as:
          - sequence of nodes
          - length of path
          - plot of graph with result path
          - starting temperature
          - number of iterations
          - message if initial path was given as parameter
        
 - Note: 
 It is assumed that input data is correct.
 However, if it is not, the proper message is displayed and the program returns to main menu / submenu.

 Program should be started from main folder: python lab06/Lab06_console.py
 
 In subfolder (inputs) there are some sample, randomly generated points which can be used to testing program.
 In subfolder (outputs) there are program answers for files in (inputs) folder with diffrent algorithms and parameters. 
