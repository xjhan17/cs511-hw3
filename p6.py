from z3 import *
import sys
import itertools
import json
import numpy as np

# get input from either command line or script
# format in command line: [[node#, weight, *, *, * ...], [node#, weight, *, *, * ...], ...]
# e.g: [[1,2,2,3,4,5],[2,4,1,4],[3,4,1,5],[4,7,1,2,5],[5,7,1,3,4]]
# format in script: same as described in hw 3 p6
# e.g: [(1, 2, [2, 3, 4, 5]), (2, 4, [1, 4]), (3, 4, [1, 5]), (4, 7, [1, 2, 5]), (5, 7, [1, 3, 4])]
if len(sys.argv) > 1:
    G = np.array(json.loads(sys.argv[1]))
else:
    G = [(1, 2, [2, 3, 4, 5]), \
         (2, 4, [1, 4]), \
         (3, 4, [1, 5]), \
         (4, 7, [1, 2, 5]), \
         (5, 7, [1, 3, 4])]

def extractGraph():
    n = len(G)
    weight = []
    nodes = []
    boolValue = [[Bool('x_%s_%s' % (i+1, j+1)) for j in range(n)] for i in range(n)]
    for i in range(n):
        weight.append(Int('w_%s' % (i+1)))
        nodes.append(i)
    for i in range(n):
        weight[i] = G[i][1]
        if len(sys.argv) > 1:
            adjNodes = np.delete(np.delete(G[i], 0),0)
        else:
            adjNodes = G[i][2]
        for j in range(n):
            if (j + 1) not in adjNodes and i != j:
                boolValue[i][j] = False
    return nodes, weight, boolValue

def maxClique(length):
    s = Solver()
    nodes, weight, boolValue = extractGraph()
    maxClique = []
    constraints = []
    maxWeight = 0
    
    for size in reversed(range(1, length)):
        for elements in list(itertools.combinations(nodes, size+1)):
            currWeight = -1
            for index in elements:
                if currWeight == -1:
                    currWeight = weight[index]
                else:
                    currWeight += weight[index]
                for cons in elements:
                    constraints += [And(boolValue[index][cons])]
            constraints += [currWeight > maxWeight]
            s.add(And(constraints))
            if s.check() == sat:
                maxWeight = currWeight
                maxClique = elements
            constraints = []
            s.reset()
    return maxClique

def main():
    clique_max = []
    for x in maxClique(len(G)):
        clique_max.append(int(x+1))
    print('G = \n', G)
    print('The maximum-weight clique in G = \n', clique_max)

if __name__== "__main__":
    main()