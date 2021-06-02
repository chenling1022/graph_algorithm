import pickle
import time
def nearest_Hosp_MultiBFS(pointerDict, hospList, exportfile="exportNearest.p", verbose=1):
    #prints input details if the user wishes to
    if verbose == 2:
        print("Pointer list: ", pointerDict)
        print("Hospitals: ", hospList)
    H = len(hospList)
    N = len(pointerDict)
    distDict = {i: N+1 for i in pointerDict.keys()}  # stores distance to nearest hospital. Default value is N+1
    checked = {i: 0 for i in pointerDict.keys()}  # stores whether the nearest hospital of a node has already been found
    paths = {key: [] for key in pointerDict.keys()}  # stores the path to the nearest hospital

    hMap = {}  # used solely for printing purposes, acts as a map from the hospital node index to its position in lists
    # The below loop initializes values for hospitals
    for i, j in enumerate(hospList):
        hMap[j] = i
        distDict[j] = 0  # distance of hospital from itself is 0
        checked[j] = 1  # no need to replace the above, so set as checked
        paths[j] = [j]

    last_checked = hospList  # at each step of loop, nodes connected to those in "last checked" are checked.
    # so, we start by setting last_checked to all hospital nodes.
    print("Starting search...")
    t0 = time.process_time()  # starting time counter for actual search
    # O(V+2E) complexity, j takes exactly 2E values regardless of the structure of the graph
    # V -> number of nodes, same as n.
    # E -> number of edges, has range [n-1, n(n-1)/2] for a connected graph
    while True:
        temp = []
        for i in last_checked:
            for j in pointerDict[i]:
                if not checked[j]:
                    distDict[j] = distDict[i] + 1  # sets shortest distance
                    paths[j] = [j] + paths[i]  # adds itself to begining of path
                    checked[j] = 1  # sets checked flag
                    temp.append(j)
        last_checked = temp.copy()
        if not len(last_checked):
            break

    t1 = time.process_time() - t0  # ending time counter

    # Printing stats and results
    if verbose:
        print("Total no. of updations: ", sum(checked.values()))
        print("Value of V (for comparison): ", N)
    if verbose == 2:
        print("\nTop route for each node:")
        for i in paths:
            try:  # fails if path is empty
                print("From {} to hosptial at {}: {}\t\tDistance: {}".format(i, paths[i][-1], paths[i], distDict[i]))
            except:
                print("No path from node at {} to any hospital".format(i))

    print("\nSearch executed in {:.2f} seconds".format(t1))
    with open(exportfile, mode="wb+") as file:
        pickle.dump(paths, file)
        pickle.dump(distDict, file)
        print("Successfully saved paths and distDict to", exportfile)

