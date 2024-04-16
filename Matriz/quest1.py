#questão 1

linha = 4
coluna = 4

matriz = [int] * linha
for i in range(len(matriz)):
    matriz[i] = [int] * coluna

cont = 0

for l in range(len(matriz)):
    for z in range(len(matriz[l])):
        matriz[l][z] = int(input("Digite um numero: "))
        if matriz[l][z] > 10:
            cont += 1

for p in range(len(matriz)):
    print(matriz[p])

print(f"Ela possue {cont} numeros maior que 10")
