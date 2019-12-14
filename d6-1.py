#! usr/bin/python3
    
def openFile(filename):
    with open(filename, 'r') as f:
        return [i.strip() for i in f]

def buildOrbitTree(orbitsMap):
    tree = {}
    orbitsMap = [i.split(')') for i in orbitsMap]
    
    for orb in orbitsMap:
        if orb[0] not in tree:
            tree[orb[0]] = []

        if orb[1] not in tree:
            tree[orb[1]] = []
            
        tree[orb[0]].append(orb[1])
        
    return tree
        
def countOrbits(orbTree, node, layer):
    if len(orbTree[node]) == 0:
        return layer

    else:
        sum = layer
        for i in orbTree[node]:
            sum += countOrbits(orbTree, i, layer + 1)

        return sum
    
orbitsMap = openFile('input6.txt')
localOrbitsTree = buildOrbitTree(orbitsMap)
root = 'COM'

print(countOrbits(localOrbitsTree, root, 0))
