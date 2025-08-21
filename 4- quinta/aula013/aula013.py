#introducao a convulacao
#convulucao basicamente multiplicacao de matriz pra borrar ou dar resolucao em ua imagem 
'''
import matplotlib.pyplot as plt
matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,4]] #parenteses vazioz = 3 linhas, os valores dentro da as colunas
plt.imshow(matriz,'hot')
plt.colorbar()
plt.show()


#i) printe a lista e cada elemento dentro dela ( for dentro de um for)
matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,4]]
print(matriz[0]) #<-- aqui prinda 1,2,3,4
print(type(matriz[0]))
print(matriz[0][2]) #<-- printar o numero da lista da lista

for i in range(len(matriz)):
    for j in range(len(matriz)):
        print(f"matriz[{i}][{j}] = matriz {matriz[i][j]}")



#ii) adicione a uma matriz vazia listas ate ela ficar com 3 linhas e 4 colunas
matriz = []
linhas = 3
colunas = 4
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(1)
    matriz.append(linha)
    print(matriz)

import matplotlib.pyplot as plt

linhas = 3
colunas = 4

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if linhas == colunas:
                linha.append(0)  
        matriz.append(linha)
    return matriz
diagonal = cria_matriz(linhas=10, colunas=10)

for i in range(len(diagonal)):
    diagonal[i][i] = 1
a = diagonal

# mostra como imagem
plt.imshow(a, cmap='hot')
plt.colorbar()
plt.show()
'''
#iv) fazer tabuleiro de xadrez
import matplotlib.pyplot as plt

linhas = 8
colunas = 8

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)  # preenche com 0
        matriz.append(linha)
    return matriz

xadrez = cria_matriz(linhas, colunas)

# preencher xadrez
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2 == 0:
            if j%2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j%2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
plt.imshow(xadrez, cmap='gray')  # cinza para xadrez ficar preto/branco
plt.show()
