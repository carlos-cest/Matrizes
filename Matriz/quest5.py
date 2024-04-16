#questão 5

matriz = [
    [0, 1, 4],
    [5, 6, 6],
    [8, 7, 2]
]

busca = int(input("Digite um número: "))

linha = 0
coluna = 0
cont = False

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if matriz[l][c] == busca:
            linha = l
            coluna = c
            cont = True

if cont == False:
    print("Numero não encontrado!!!")
else:
    print(f"O número está na linha {linha} e na coluna {coluna}")