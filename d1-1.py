#! usr/bin/python3

def calculateFuelReqs(mass):
    return (mass // 3) - 2
        
def openfile(filename):
    massList = []
    with open(filename) as f:
        massList = [int(line.strip()) for line in f]

    return massList

massList = openfile('input1.txt')
fuelReqList = [calculateFuelReqs(mass) for mass in massList]
print(sum(fuelReqList))

