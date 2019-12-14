#! usr/bin/python3

import itertools

inputs = []
outSig = 0

def openFile(filename):
    with open(filename) as f:
        return [int(position.strip()) for position in f.readline().split(',')]

def runProgram(program, phaseSet, inputSig):
    i = 0
    phaseSetting = phaseSet
    inputSignal = inputSig
    global inputs
    inputs = [phaseSet, inputSig]
    
    while (program[i] != 99) and i <= len(program):
        instruction = str(program[i])

        opCode = int(instruction[-2:])
        numVars = howManyVariables(opCode)

        unrefinedParModes = [int(i) for i in instruction[:-2]]
        noModeParamInds = [n for n in range((i + 1), (i + 1 + numVars))]
        parameterModes = refineParModes(unrefinedParModes, len(noModeParamInds))
        paramIndexes = applyModes(program, noModeParamInds, parameterModes)
        
        response = executeInstr(program, opCode, paramIndexes, i)
        program = response[0]
        skipLength = response[1]
        
        i += skipLength

    global outSig
    return outSig

def refineParModes(parModes, parmLength):
    n = parmLength - len(parModes)
    return parModes[::-1] + ([0] * n)

def applyModes(program, params, parModes):
    for i in range(len(parModes)):
        if parModes[i] == 0:
            params[i] = program[params[i]]
    return params

def howManyVariables(op):
    if (op == 1) or (op == 2) or (op == 7) or (op == 8):
        return 3

    elif (op == 3) or (op == 4):
        return 1

    elif (op == 5) or (op == 6):
        return 2
        
    else:
        raise ValueError(f"unknown opcode {op}")
    
def executeInstr(program, operation, params, i):
    if operation == 1:
        instrPtr = 4
        output = program[params[0]] + program[params[1]]
        program[params[2]] = output
        
    elif operation == 2:
        instrPtr = 4
        output = program[params[0]] * program[params[1]]
        program[params[2]] = output

    elif operation == 3:
        global inputs
        instrPtr = 2
        program[params[0]] = inputs.pop(0)
        
    elif operation == 4:
        global outSig
        instrPtr = 2
        outSig = program[params[0]]

    elif operation == 5:
        if program[params[0]] != 0:
            instrPtr = program[params[1]] - i
        else:
            instrPtr = 3

    elif operation == 6:
        if program[params[0]] == 0:
            instrPtr = program[params[1]] - i
        else:
            instrPtr = 3

    elif operation == 7:
        instrPtr = 4
        if program[params[0]] < program[params[1]]:
            output = 1
        else:
            output = 0
        program[params[2]] = output
        
    elif operation == 8:
        instrPtr = 4
        if program[params[0]] == program[params[1]]:
            output = 1
        else:
            output = 0
        program[params[2]] = output
        
    return [program, instrPtr]

def calcPermutations(seqList):
    return list(itertools.permutations(seqList, len(seqList)))

def findMaxThrust(program, sequences):
    maxThrust = -1
    for sequence in sequences:
        seqThrust = testSequence(program, sequence)
        if seqThrust > maxThrust:
            maxThrust = seqThrust
    return maxThrust

def testSequence(program, sequence):
    inputSig = 0
    for phaseSetting in sequence:
        inputSig = runProgram(program.copy(), phaseSetting, inputSig)
    return inputSig

filename = "input7.txt"
program = openFile(filename)
allSequences = calcPermutations([0,1,2,3,4])
print(findMaxThrust(program, allSequences))
