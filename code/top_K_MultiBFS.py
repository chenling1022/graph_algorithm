import pickle
import time
def top_k_multiBFS(k, pointerDict, hospList, exportfile="exportTopK.p", verbose=1):
    if verbose==2:
        print("Pointer list: ", pointerDict)
        print("k: ", k)
        print("Hospitals: ", hospList)
    H = len(hospList)
    N = len(pointerDict)
    distDict = {i: [N+1]*H for i in pointerDict.keys()}  # stores distances from each hospital. Default value is N+1, not all are actually calculated.
    checked = {i: [0]*H for i in pointerDict.keys()}  # checked[a][b] stores 0 or 1 to indicate if distance of a'th node from b'th hospital has been checked.
    # Hence, both of the above are n x H matrices, stored as lists of lists.
    numComplete = {i: 0 for i in pointerDict.keys()}  # counts the number of hospitals of the ith node that have been found already.
    # Used to stop checking nodes early, bringing the time complexity down from O(nH) to O(nk) instead.
    topKDist = {i: {} for i in pointerDict.keys()}  # stores only the top k distances once found.

    hMap = {}  # used solely for printing purposes, acts as a map from the hospital node index to its position in lists
    # The below loop initializes values for hospitals
    for i, j in enumerate(hospList):
        hMap[j] = i
        distDict[j][i] = 0  # distance of hospital from itself is 0
        topKDist[j][j] = 0
        checked[j][i] = 1  # no need to replace the above, so set as checked
        numComplete[j] = 1

    last_checked = hospList  # at each step of loop, nodes connected to those in "last checked" are checked.
    # so, we start by setting last_checked to all hospital nodes.
    skipCounter = 0  # just to see how much better this performs compared basic bfs approach
    loopCounter = 0
    print("Starting search...")
    t0 = time.process_time()  # starting time counter for actual search
    while True:
        temp = []
        toUpd = []
        for i in last_checked:  # each node appears <=k times in last_checked
            # there are exactly 2E sub-elements in pointerDict.
            # So, if each node in last_checked appears k times, the below loop executes <=2E*k times total.
            for j in pointerDict[i]:
                loopCounter += 1
                if numComplete[j] < k:  # below code skipped if top k hospitals for the node are already found.
                    for h in range(H):  # allows for updating distances from multiple hospitals in a single "step" of loop
                        # only updates if distance of a hospital from "last checked" node is known but not from "checking" node
                        # below code executes n*k times overall (see updation print statement)
                        if (checked[i][h]) and (not checked[j][h]):
                            distDict[j][h] = distDict[i][h]+1
                            topKDist[j][hospList[h]] = distDict[j][h]
                            toUpd.append([j, h])
                            temp.append(j)
                            numComplete[j] += 1
                else:
                    skipCounter += 1
        for pair in toUpd:  # updating checked list at the end of the "step" to avoid errors
            # below code executes n*k times overall
            checked[pair[0]][pair[1]] = 1
        last_checked = list(set(temp))  # removes duplicates; order doesn't matter as all nodes in a bfs "step" are equidistant
        if not len(last_checked):  # breaks if there are no new nodes left to update
            break

    t1 = time.process_time() - t0  # ending time counter

    # Printing stats and results
    if verbose:
        print("Total no. of updations: ", sum([sum(l) for l in checked.values()]))
        print("Value of V*k (for comparison): ", N*k)
        print("No. of iterations of loop (= edges travelled = 2E): ", loopCounter)
        print("No. of loop executions skipped due to modification: ", skipCounter)

    print("\nSearch executed in {:.2f} seconds".format(t1))
    with open(exportfile, mode="wb+") as file:
        pickle.dump(topKDist, file)
        print("Successfully saved topKDist to", exportfile)

