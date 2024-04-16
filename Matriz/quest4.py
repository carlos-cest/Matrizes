#questão 4

tam = 4

matriz = [0] * tam
for i in range(len(matriz)):
    matriz[i] = [0] * tam

cont = 0
linha = 0
coluna = 0

def localização():
    pass

for p in range(len(matriz)):
    for u in range(len(matriz)):
        matriz[p][u] = float(input("Digite um número: "))
        if  p == 0 and u == 0:
            cont = matriz[p][u]
            linha = p
            coluna = u
        if matriz[p][u] > cont:
            cont = matriz[p][u]
            linha = p
            coluna = u

print("")      
for w in range(len(matriz)):
    print(matriz[w])
print("")
print(f"O maior número é {cont} e a sua localização é na linha: {linha} e coluna: {coluna}")
