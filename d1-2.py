#! usr/bin/python3

def calculateFuelReqs(mass):
    totalFuelReq = 0
    curFuelReq = (mass // 3) - 2

    while curFuelReq > 0:
        totalFuelReq += curFuelReq
        curFuelReq = (curFuelReq // 3) - 2

    return totalFuelReq

massList = []

with open(filename) as f:
    massList = [int(line.strip()) for line in f]

fuelReqList = [calculateFuelReqs(mass) for mass in massList]

print(sum(fuelReqList))
