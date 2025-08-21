'''
#tentando enteder funcao


#bota tenta aprender funcao
#i) construa uma funcao de soma

def soma(a,b):
    return a + b

resultado = soma(1, 4)
print(resultado)
print(soma(6, 10))

#ii) faca divir a lista em pares e impares
lista = [4,1,5,7,3,6,9,2,10,8]

pares = 0
impar = 0

for i in range(len(lista)):
    if i%2 != 0:
        pares +=1
    else:
        impar +=1
print(pares, impar)
'''

#iii) faca agora pedir 5 numeros da lista e receber par e impar

lista = []
def pedir_num(msg):
    num = input(msg)
    num = int(num)
    lista.append(num) #<-- usar .APPEND pra adicionar coisas em uma lista comando importante e crucial
    return num
#nota: voce da valor ao paramtro *quando voce chama a funcao*
#nota: e EXTREMAMENTE comum voce chamar a funcao atribuindo ela a uma variavel e consequentemente ao valor do parametro se tiver um

for i in range(1,6):
    pedindo = pedir_num("me da 5 numero:\n-> ")
print(pedir_num)

pares = 0
impar = 0

for num in (lista):
    if num%2 == 0:
        pares +=1
    elif num%2 != 0:
        impar +=1
print(f"a quantidade de pares e: {pares}, a quantidade de impares e: {impar}")