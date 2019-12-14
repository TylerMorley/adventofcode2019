#! usr/bin/python3

relativeBase = 0

def openFile(filename):
    with open(filename) as f:
        return [int(position.strip()) for position in f.readline().split(',')]

def runProgram(program):
    i = 0
    stepSize = -1
    
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
            
    return program[0]

def refineParModes(parModes, parmLength):
    n = parmLength - len(parModes)
    return parModes[::-1] + ([0] * n)

def applyModes(program, params, parModes):
    for i in range(len(parModes)):
        if parModes[i] == 0:
            params[i] = program[params[i]]
        elif parModes[i] == 1:
            noneValue = None
        elif parModes[i] == 2:
            global relativeBase
            params[i] = program[params[i] + relativeBase]
            
    return params

def howManyVariables(op):
    if (op == 1) or (op == 2) or (op == 7) or (op == 8):
        return 3

    elif (op == 3) or (op == 4) or (op == 9):
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
        instrPtr = 2
        print('Please provide an input value:')
        output = int(input())
        program[params[0]] = output
        
    elif operation == 4:
        instrPtr = 2
        output = program[params[0]]
        print(f'System: {output}')

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
        
    elif operation == 9:
        instrPtr = 2
        global relativeBase
        relativeBase += params[0]
        
    return [program, instrPtr]

filename = "input5.txt"
program = openFile(filename)
runProgram(program)
