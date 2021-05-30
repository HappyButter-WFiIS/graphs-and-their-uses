!important 

	The program must be run from the main project file - "graphs-and-their-uses"!
	
	Example:
	[graphs-and-their-uses] python lab01/Lab01_console.py


The program has 2 main parts:
1. Reading from a file or generating new graph.
   
	There are 4 options to choose from:
   
	[1] Load graph from file
   
        This option ensures reading the graph with a given representation. In
        the first step the user has to choose input representation type. There 
        are 3 representation types to choose from:
            
        [1] Adjancency matrix
        [2] Adjacency list
        [3] Incidence matrix

        The second step requires from the user to put name of the text file and 
        its path which starts from "lab01" folder. So if the user wants to add 
        any new file it has to be inside "lab01" folder. As example we have 
        created folder "inputs" inside "lab01" which contains 3 txt files with
        each available graph representation type. 
        
        Example:
        1) User pick adjancency matrix type with option [1]
        2) User puts file name and its path from lab01 folder:
            inputs/adjmat.txt
        
        Exceptions: 
        We assume that the user puts correct representation type of the graph
        inside the text file. If not some errors may occure or the graph will not
        be read correctly. 
        If the file does not exists program would print info but it will go to 
        graph handler menu even though. To go back just put [b] option in submenu.

    [2] Generate with probability

        Option [2] ensures generating graph with given nodes number and 
        probability. Generated representation type is adjacency matrix.
        
        Assumptions:
        Number of nodes is greater then 0 and less then 1000. 
        The maximum number 1000 is still being counted in reliable time. Putting
        greater number is also possible, however this may take a few seconds to be 
        done.

        10 000 nodes graph takes around 26-28 seconds to be generated.

   [3] Generate with vertices and edges
        
        This oprion ensures generating graph with given number of vertices and 
        edges. 

        Assumptions:
        User gives correct number of vertices and edges. 
        - The number of vertices should be greater then 0 and less then 100. 
        - The number of edges must be positive and less or equal n(n – 1)/2 
        where n is the number of given vertices.
    
        Performance (test CPU: Intel Core i7-8550U):
        - for 100 vertices: 0.33s
        - for 150 vertices: 1.65s
        - for 200 vertices: 5.10s
        Statistics above were done for the most pesymistic number of edges.

    [q] Quit
        
        Exit program option.
    
2. Submenu - handling read graph
   
	There are 4 options to choose from:
    
    [1] Convert
    
        This option ensures conversion of the read graph. There have been 
        implemented all required conversions algorithms from every representation
        to every representation type. After picking this option user is able to 
        chose to which representation type graph should be converted:
   
        [1] Adjancency matrix
        [2] Adjacency list
        [3] Incidence matrix

    [2] Plot
        
        Plotting given graph. Current graph representation does not matter.
   
        Assumptions:
        Graph with up to 100 nodes would be plotted smoothly. However it 
        requires quit large screen to be readable. 
        The more edges the plotter works slower.
            
    [3] Print current graph
   
        This option prints to console current representation type.
   
        Assumptions:
        This option works smooth even with large graphs up to 1000 nodes.
        However reading such a big graph representation from console is not 
        convenient.

    [b] Go back to menu
        
        Exits to reading from a file or generating new graph menu.
