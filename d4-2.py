#! usr/bin/python3

def openFile(filename):
    with open(filename, 'r') as f:
        return [int(endpoint.strip()) for endpoint in f.readline().split('-')]

def followsRules(number):
    num = [int(i) for i in str(number)]

    twoAdjDigits = False
    doesNotDecrease = True
    
    streakLength = 1
    
    for i in range(len(num) - 1):
        digit = num[i]
        nextDigit = num[i + 1]

        if digit > nextDigit:
            doesNotDecrease = False

        if digit == nextDigit:
            streakLength += 1
        else:
            if streakLength == 2:
                twoAdjDigits = True
            streakLength = 1

    if streakLength == 2:
        twoAdjDigits = True

    return (twoAdjDigits and doesNotDecrease)

inputRange = openFile('input4.txt')

possiblePasswords = []
for i in range(inputRange[0], inputRange[1]):
    if followsRules(i):
        possiblePasswords.append(i)

print(len(possiblePasswords))
