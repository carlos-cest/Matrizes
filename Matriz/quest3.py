#questão3

tam = 4

matriz = [0] * tam
for i in range(len(matriz)):
    matriz[i] = [0] * tam

for o in range(len(matriz)):
    for p in range(len(matriz[o])):
        matriz[o][p] = o * p 

for t in range(len(matriz)):
    print(matriz[t])
