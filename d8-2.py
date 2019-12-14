#! usr/dev/python3

WIDTH = 25
HEIGHT = 6
LAYER = WIDTH * HEIGHT

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

def buildImage(layers):
    image = []
    
    for j in range(HEIGHT):
        image.append([])
        
        for k in range(WIDTH):
            i = 0
            
            while layers[i][j][k] == 2:
                i += 1
                
            image[j].append(layers[i][j][k])
            
    return image

sifImage = openFile('input8.txt')
layeredImage = splitLayers(sifImage)
layers = len(layeredImage)
rows = len(layeredImage[0])
columns = len(layeredImage[0][0])
image = buildImage(layeredImage)

for row in image:
    print(row)
