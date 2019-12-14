#! usr/bin/python3

def openFile(filename):
    with open(filename) as f:
        return [int(position.strip()) for position in f.readline().split(',')]

def runProgram(program):
    i = 0
    stepSize = -1
    
    while (program[i] != 99) and i <= len(program):
        instr = str(program[i])
        skipLength = -1
        op = 0
        parameterModes = []
        parameters = []
        values = []
        
        if (instr[-1] == '1') or (instr[-1]== '2'):
            op = int(instr[-2:])
            parameterModes = refineParModes([int(i) for i in instr[:-2]])
            parameters = [i for i in program[i+1:i+4]]
            # values = [list(i) for i in zip(parameterModes, parameters)]
            
            skipLength = 4

        elif (instr[-1] == '3') or (instr[-1] == '4'):
            op = int(instr)
            parameterModes = [0]
            parameters = [program[i+1]]
            # values = [[0,parameters]]

            skipLength = 2
        
        else:
            raise ValueError(f"unknown opcode {op}")

        program =  executeInstr(program, op, parameterModes, parameters)

        i += skipLength
            
    return program[0]

def refineParModes(parModes):
    n = 3 - len(parModes)
    return parModes[::-1] + ([0] * n)
            
def initializeMemory(program, noun, verb):
    program[1] = noun
    program[2] = verb
    return program

def executeInstr(program, operation, parModes, params):
    if operation == 1:
        for i in range(2):
            if parModes[i] == 0:
                params[i] = program[params[i]]

        output = params[0] + params[1]
        program[params[2]] = output
        
    elif operation == 2:
        for i in range(2):
            if parModes[i] == 0:
                params[i] = program[params[i]]

        output = params[0] * params[1]
        program[params[2]] = output

    elif operation == 3:
        print('Please provide an input value:')
        output = int(input())
        program[params[0]] = output
        
    elif operation == 4:
        output = program[params[0]]
        print(f'System: {output}')

    elif operation == 5:
        return None
        
    return program

def findInitialization(program):
    DESIRED_OUTPUT = 19690720
    
    for i in range(100):
        for j in range(100):
            curProgram = initializeMemory(program.copy(), i, j)
            
            if runProgram(curProgram) == DESIRED_OUTPUT:
                return [i, j]
            
    return [-1,1]

filename = "input5.txt"
program = openFile(filename)
runProgram(program)
