import networkx as nx
from itertools import combinations
from random import random
import sys

def generateGraph(n, p):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)
    
    return g



n = 100000
G = generateGraph(n, 5/n)
fname=str(n)+"_nodes1.txt"
original_stdout = sys.stdout  # Save a reference to the original standard output
with open(fname, 'w') as f:
    sys.stdout = f
    for i in G.edges():
        print (i[0], i[1])
        print (i[1], i[0])
    sys.stdout = original_stdout




