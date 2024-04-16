#questão 2

tam = 5

matriz = [0] * tam
for i in range(len(matriz)):
    matriz[i] = [0] * tam

for l in range(len(matriz)):
    for p in range(len(matriz)):
        if l == p:
            matriz[l][p] = 1

for o in range(len(matriz)):
    print(matriz[o])