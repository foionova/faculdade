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

notas = [7, 8, 9, 10]
for i in range(len(notas)):
    print(f"indice: {i} valor {notas[i]}")

lista = [3,'danilo',0.5,True] 
lista[0] = 3
lista[1] = 'danilo'
lista[2] = 0.5
lista[3] = True

for elem in lista:
    print(elem) #aqui podemos ver que o elem, pegou o indice e valor dos elementos da lista, e o criterio para encerrar o for foi o fim da lista (
    #oque declara que e um processo finito).
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")
'''
#Peça 10 numeros ao usuario. Coloque-os dentro da lista. Após a lista estar completa, conte a qtd de pares e impares lá dentro.


lista = []
for i in range(1,6):
    num = float(input("meda 5 numero ai:\n-> "))
    lista.append(num)
print(lista)

par = 0
impar = 0

for i in range(len(lista)):
    if lista[i]%2 == 0:
        par += 1
    else:
        impar += 1
print(f"a lista possui {par} numeros pares e {impar} numeros impares")



lista = []
for i in range(1, 11):   # de 1 a 10
    num = int(input(f"Digite o {i}º número:\n-> "))
    lista.append(num)

print("Lista final:", lista)

par = 0
impar = 0

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"A lista possui {par} números pares e {impar} números ímpares.")
