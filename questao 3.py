linhas = int(input('nº de linhas: '))
colunas = int(input('nº de colunas: '))
im = []
list = []
def leiamatriz(l, c):
    matriz = []
    for i in range(l):
        matriz.append(c * [0])
    return matriz
matriz = leiamatriz(linhas, colunas)
print(matriz)
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input(f'Digite um numero para a posiçao {i, j}'))
def buscaval():
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            list.append(valor)
            if valor % 2 != 0:
                im.append(valor)
buscaval()
for i, valor in enumerate(matriz):
    print(valor)

print(f'A matriz possui {len(im)}  impares!')
print(f'O menor valor eh {min(list)}')