#Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada
#posição das matrizes lidas.

matriz1 = [
    [0, 1, 4],
    [5, 6, 6],
    [8, 7, 2]
]

matriz2 = [
    [7, 9, 4],
    [2, 5, 6],
    [8, 1, 2]
]

matriz_maior = [int] * 3
for i in range(len(matriz_maior)):
    matriz_maior[i] = [int] * 3


matriz1[0][0] > matriz2[0][0]