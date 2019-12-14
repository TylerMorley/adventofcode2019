#! usr/dev/python3

WIDTH = 25
HEIGHT = 6
# WIDTH = 3
# HEIGHT = 2
LAYER = WIDTH * HEIGHT
MIN_DIGITS = 0

def openFile(filename):
    with open(filename, 'r') as f:
        return [int(i) for i in list(f.readline().strip())]

def splitLayers(sifImage):
    layeredImage = []
    if len(sifImage) % LAYER != 0:
        raise ValueError(f'Input size off')
    else:
        numLayers = len(sifImage) // LAYER
        for i in range(numLayers):
            layer = []
            for j in range(HEIGHT):
                begin = (LAYER * i) + (WIDTH * j)
                end = (LAYER * i) + (WIDTH * (j+1))
                layer.append(sifImage[begin:end])
            layeredImage.append(layer)
            
    return layeredImage

def findMinZeroes(layers):
    zeroCounts = []
    for layer in layers:
        layerCount = 0
        for row in layer:
            layerCount += row.count(0)
        zeroCounts.append(layerCount)

    return zeroCounts.index(min(zeroCounts))

def onesAndTwos(layer):
    ones = 0
    twos = 0
    for row in layer:
        ones += row.count(1)
        twos += row.count(2)
    return ones * twos
    
sifImage = openFile('input8.txt')
layeredImage = splitLayers(sifImage)
minZeroLayer = findMinZeroes(layeredImage)
print(onesAndTwos(layeredImage[minZeroLayer]))
