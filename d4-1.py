#! usr/bin/python3

def openFile(filename):
    with open(filename, 'r') as f:
        return [int(endpoint.strip()) for endpoint in f.readline().split('-')]

def followsRules(number):
    hasTwoAdjDigits = False
    doesNotDecrease = True

    num = [int(i) for i in str(number)]
    
    for i in range(len(num) - 1):
        digit = num[i]
        nextDigit = num[i + 1]
        
        if digit == nextDigit:
            hasTwoAdjDigits = True
            
        if digit > nextDigit:
            doesNotDecrease = False
            
    return hasTwoAdjDigits and doesNotDecrease

inputRange = openFile('input4.txt')

possiblePasswords = []
for i in range(inputRange[0], inputRange[1]):
    if followsRules(i):
        possiblePasswords.append(i)

print(len(possiblePasswords))
