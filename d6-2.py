#! usr/bin/python3

root = 'COM'
    
def openFile(filename):
    with open(filename, 'r') as f:
        return [i.strip() for i in f]

def buildOrbitTree(orbitsMap):
    tree = {}
    orbitsMap = [i.split(')') for i in orbitsMap]
    
    for orb in orbitsMap:
        if orb[0] not in tree:
            tree[orb[0]] = {'parent':None, 'chld':[]}

        if orb[1] not in tree:
            tree[orb[1]] = {'parent':None, 'chld':[]}
            
        tree[orb[0]]['chld'].append(orb[1])
        tree[orb[1]]['parent'] = orb[0]
        
    return tree
        
def countOrbits(orbTree, node, layer):
    if len(orbTree[node]) == 0:
        return layer

    else:
        sum = layer
        for i in orbTree[node]:
            sum += countOrbits(orbTree, i, layer + 1)

        return sum

def getParents(tree, body):
    #Start on the body they're orbiting, don't count theirself
    body = tree[body]['parent']
    parents = []

    while body != 'COM':
        body = tree[body]['parent']
        parents.append(body)
        
    return parents

def calcMinTransfers(youPath, sanPath):
    commonBodies = list(set(youPath) & set(sanPath))
    you = min([youPath.index(i) for i in commonBodies]) + 1
    san = min([sanPath.index(i) for i in commonBodies]) + 1
    return you + san
    
orbitsMap = openFile('input6.txt')
localOrbitsTree = buildOrbitTree(orbitsMap)
youPath = getParents(localOrbitsTree, 'YOU')
sanPath = getParents(localOrbitsTree, 'SAN')

print(calcMinTransfers(youPath, sanPath))
# print(countOrbits(localOrbitsTree, root, 0))
