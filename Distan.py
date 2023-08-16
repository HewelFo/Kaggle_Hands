import numpy as np

def min_distans(source, target):

    target = [y for y in target]
    source = [x for x in source]

    matriz = np.zeros([len(source),len(target)])

    matriz[0] = [x for x in range(len(target))]
    matriz[:,0] = [y for y in range(len(source))]

    for x in range(len(source)):
        for y in range(len(target)):
            if target[y] != source[x]:
                matriz[x,y] = min(matriz[x-1,y], matriz[x,y-1]) + 1
            else: 
                matriz[x,y] = matriz[x-1,y-1]
    print(matriz) 
    

min_distans("abas","abca")