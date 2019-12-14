#! usr/bin/python3

def openFile(filename):
    with open(filename) as f:
        return [int(position.strip()) for position in f.readline().split(',')]

def runProgram(program):
    for i in range(0, len(program), 4):
        op = program[i]
        
        if op == 99:
            return program[0]
        
        elif (op != 1) and (op != 2):
            raise ValueError(f"unknown opcode {op}")
        
        else:
            inputPos1 = program[i+1]
            input1 = program[inputPos1]

            inputPos2 = program[i+2]
            input2 = program[inputPos2]

            outputPos = program[i+3]
        
            program =  executeOpcode(program, op, input1, input2, outputPos)

    return program[0]

def initializeMemory(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program

def executeOpcode(program, operation, input1, input2, outputPos):
    output = 0
    
    if operation == 1:
        output = input1 + input2
    elif operation == 2:
        output = input1 * input2
    
    program[outputPos] = output
    return program

def findInitialization(program):
    DESIRED_OUTPUT = 19690720
    
    for i in range(100):
        for j in range(100):
            curProgram = initializeMemory(program.copy(), i, j)
            
            if runProgram(curProgram) == DESIRED_OUTPUT:
                return [i, j]
            
    return [-1,1]

filename = "input2.txt"
program = openFile(filename)
result = findInitialization(program)

print(100 * result[0] + result[1])
