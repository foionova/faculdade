'''
#tentando deduzir a versao refinada com for
for i in range (1,11):
    print(f"tabuada do {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print() #print aqui no final pra dar uma linha em branco no final do codigo

#compreensao de len lista
lista = [3,'danilo',0.5,True]
lista[0] = 3
lista[1] = 'danilo'
lista[2] = 0.5
lista[3] = True

for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")
'''
notas = [7, 8, 9, 10]
for i in range(len(notas)):
    print(f"A nota {i+1} é {notas[i]}")
