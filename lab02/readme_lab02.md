- The program consists of 2 main parts:
1. Presenting tasks from exercies set no. 2 using random graphs.
   
	There are 6 options to choose from:
   
	[1] Chceck if sequence is graphical
   
        This option allows to load sequence of integer numbers.
        
        Input:
        Format of input (example): 4 2 2 3 2 1 4 2 2 2 2
        Number i denotes expected degree of vertex i.
        Every number should be in range [0, number_of_vertices-1].
        
        Description:
        If input is correct and degrees are not bigger than number of vertices,
        the program checks if given sequence is graphical and displays anwser.
        Moreover if it is possible to create a graph using given sequence,
        the program plots one of possible graphs represented by the sequence.
        
    [2] Example of graph randomization for given graphical sequence

        Option [2] gives possibility to randomize graph created using graphical sequence.
        
        Input:
        First step is to enter correct graphical sequence. 
        Input is exactly the same as in option [1].
        Second step is to enter number of randomizations - integer in range [0, 10000+),
        but 100 is recommended in most of cases.

        Description:
        If input is correct and sequence is graphical than the program plots
        one of possible solutions and than asks for the number of randomizations.
        After performing randomization given number of times, plot is created again
        to check if graph changed it's appearance.

   [3] Graph components in random graph
        
        This option performs generation of random graph with given parameters,
        finds components of graph and the biggest one of them.

        Input:
        Integer - number of vertices in a random graph [0, 1000+),
        but numbers bigger than 100 are not recommended because of plotting time.
        Float - probability that each pair of nodes is connected by edge [0, 1].
          
        Description:
        If input is correct the programs creates random graph, 
        displays it's components as list of nodes inside each component 
        and points out the biggest one.
        Moreover the graph is then plotted showing each component with different color.  

    [4] Random Eulerian graphs
    
        This option allows to generate Eulerian graph 
        and finds Eulerian Cycle in it.
        
        Input:
        Single integer - number of vertices of random graph in recommended in range [3, 200+).
        
        Description:
        Firstly the program displays random graphical sequence used for generating graph.
        Number of randomizations during generating graph is constant (100).
        Secondly the program finds Eulerian Cycle and displays it as a path of 
        consecutive nodes, starting with vertex with index 1.
        
        Performance:
        For 100 vertices expected execution time including plotting is about ~1s.
        For 200 vertices - about ~10s.
        
    [5] Random k-regular graphs
    
        This option allows to create k-regular graph with given parameters.
        
        Input: 
        First integer - number of vertices [1, 1000+).
        Second integer - degree of every vertex [0, vertices-1].
        Third integer - number of randomizations [0, 10000+),
        but 100 is recommended in most of cases.
        
        Description: 
        After entering the corrcet input k-regular graph is created,
        than randomized and finally plotted. 
        
    [6] Check if random graph is Hamiltonian
    
        This options checks if random graph generated
        for given parameters has Hamiltonian Cycle.
        
        Input:
        Integer - number of vertices [1, 30+)
        Float - probability that each pair of nodes is connected by edge [0, 1].
        
        Description:
        If input is correct the programs creates random graph, 
        checks if it has Hamiltonian Cycle and displays proper anwser.
        At the end graph is plotted on the screen.
        
        Performance:
        For maximal possible number of edges and
        1) 16 nodes - 0.68s
        2) 20 nodes - 2.83s
        3) 24 nodes - 9.11s
        4) 28 nodes - 29.75s
        5) 32 nodes - 66.82s
        
    [q] Quit
        
        Exit program option.
    
2. Presenting some of the tasks from exercise set no. 2 using graph uploaded from file.
   
   After uploading graph from file using option '0' 
   the submenu is displayed and there are 5 options to choose from:
    
   [1] Chceck if graph is Hamiltonian
    
        This options returns simple message stating whether 
        graph is Hamiltonian or not.

   [2] Check if graph is k-regular
        
        This options returns simple message stating whether 
        graph is k-regular or not. 
        Moreover the option informs about the exact k value. 
            
   [3] Randomize graph
   
        This option modifies given graph by performing
        given number of randomizations.

   [4] Mark components in graph and find the biggest one
    
       This options finds components of given graph and the biggest one of them.
       Moreover the graph is then plotted showing each component with different color. 
       
   [5] Plot graph
    
        This options plots a graph from file. 
    
   [b] Go back to menu
        
        Exits to main menu.
      
 - Note: 
 It is assumed that input data is correct.
 However, if it is not, the proper message is displayed and the program returns to main menu / submenu.
 In case of graphs from file, it is highly recommended to plot graph after upload 
 to check if it was loaded without any errors.
