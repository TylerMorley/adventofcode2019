#! usr/bin/python3

def openFile(filename):
    with open(filename) as f:
        return [int(position.strip()) for position in f.readline().split(',')]

def runProgram(program):
    updatedProg = program
    for index in range(0, len(updatedProg), 4):
        if program[index] == 99:
            return updatedProg
        else:
            updatedProg = handleOpcode(updatedProg, index)
    return updatedProg

def restoreGravityAssist(program):
    updatedProg = program
    updatedProg[1] = 12
    updatedProg[2] = 2
    return updatedProg

def handleOpcode(program, i):
    op = program[i]
    if (op == 1) or (op == 2):
        inputPos1 = program[i+1]
        inputPos2 = program[i+2]
        outputPos = program[i+3]

        input1 = program[inputPos1]
        input2 = program[inputPos2]
        
        return executeOpcode(program, op, input1, input2, outputPos)
    else:
        raise ValueError(f"unknown opcode {op}")
    
def executeOpcode(program, operation, input1, input2, outputPos):
    output = 0
    if operation == 1:
        output = input1 + input2
    elif operation == 2:
        output = input1 * input2
    else:
        raise ValueError(f'unknown operation value {operation}')
    
    program[outputPos] = output
    return program

filename = "input2.txt"
program = openFile(filename)
restoredProg = restoreGravityAssist(program)
result = runProgram(restoredProg)
print(result)
