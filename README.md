# Graph-Algorithms

> The codes containing the executable algorithms along with the driver function are available as 4 Python files in the directory 'codes' attached alongside. (genGraph.py, mainFile.py, Nearest_Hosp_MultiBFS.py and top_K_MultiBFS.py)

> To execute the program, you can run mainFile.py on the terminal. (Do note that usage of a 64 bit python interpreter is recommended so that you don't face heap issues)

> Make sure the algorithm files (Nearest_Hosp_MultiBFS.py and top_K_MultiBFS.py) are in the same directory as mainFile.py

> Once the program begins execution, you will be displayed a menu, where you can upload Graph file, either generate a hospital list(based on hashing) or upload hospital files, enter output directory and run the algorithm of your choice

> while entering the input file name, enter the full name along with the proper extension. 
   >> A few test files have been included in the "codes/Files" directory as a sample reference.
   >> if you want to use the files we have provided, enter "./Files/graph/<file_name>.txt" for inputting Graphs and "./Files/hospital/<file_name>.txt" for hospitals
   >> if you are using your own files, make sure you enter the entire directory of the file.

> The outputs are stored in the files as pickle format. You can choose to enter the output file directory, otherwise, they are exported to the codes directory as "exportNearest.p" or "exportTopK.p" for the two algorithms respectively.
   >> for the nearest Hospital Algorithm, we are dumping the shortest paths as well as the distance Dictionary to the file, in that order
   >> for the Top K hospitals Algorithm, we are dumping the topK distance dictionary to the pickle file.

> To control what information is logged onto the console screen, you can access the developer options. You will be prompted with the options there and yoou can choose what you want to view on the console output. By default, only the process time is printed, you can choose to print the execution details, and the data structures as well.

> A note on generating random graphs: You can open the genGraph.py file in your editor, enter the parameters N being the number of nodes, and the saveFile direcory. you can also change the edge density if you want, and run the file
