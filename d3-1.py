#! usr/bin/python3

def openFile(filename):
    paths = []
    with open(filename, 'r') as f:
        for wire in f:
            paths.append([instr.strip() for instr in wire.split(',')])
    return paths
            
def tracePaths(wirePaths):
    wireLocations = []
    for path in wirePaths:
        easyPath = simplifyPath(path)
        pathLocations = tracePath(easyPath)
        wireLocations.append(pathLocations)
        
    return wireLocations

def simplifyPath(wirePath):
    easyPath = []
    curLocation = [0, 0]
    
    for instr in wirePath:
        direction = instr[0]
        distance = int(instr[1:])

        if direction == 'R':
            curLocation[0] += distance
            
        elif direction == 'U':
            curLocation[1] += distance

        elif direction == 'L':
            curLocation[0] -= distance

        elif direction == 'D':
            curLocation[1] -= distance

        easyPath.append(curLocation.copy())

    return easyPath

def tracePath(easyPath):
    pathLocations = set()
    curLocation = [0, 0]

    for instr in easyPath:
        if (curLocation[0] < instr[0]) or (curLocation[1] < instr[1]):
            for i in range(curLocation[0], instr[0] + 1):
                for j in range(curLocation[1], instr[1] + 1):
                    pathLocations.add((i,j))
        else:
            for i in range(curLocation[0], instr[0] - 1, -1):
                for j in range(curLocation[1], instr[1] - 1, -1):
                    pathLocations.add((i,j))
        curLocation = instr

    return pathLocations
    
def closestCross(wireLocations):
    crosses = wireLocations[0].intersection(wireLocations[1])
    
    crosses.remove((0, 0))
    
    return min([(abs(cross[0]) + abs(cross[1])) for cross in crosses])
    
wirePaths = openFile("input3.txt")

wireLocations = tracePaths(wirePaths)

result = closestCross(wireLocations)

print(result)

