'''
#//Exercicio 1\\

#comparar a media de geral


nomes = {}
medias = {}

# input de 5 saltos e nomes
for i in range(5):
    nome = input("Digite o nome do atleta: ")
    saltos = []
    for j in range(5):
        salto = float(input(f"Digite a distancia do {j+1}° salto: "))
        saltos.append(salto)
    nomes[nome] = saltos

# calcular medias
for nome, saltos in nomes.items():
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    media = sum(saltos) / len(saltos)
    medias[nome] = media

# imprimir cada media
for nome, media in medias.items():
    print(f"{nome} - média dos 3 saltos: {media:.2f}")

# maior media
maior_media = max(medias.values())
for nome, media in medias.items():
    if media == maior_media:
        print(f"O atleta com maior média é {nome}, média: {media:.2f}")
'''

#//Exercicio 2\\