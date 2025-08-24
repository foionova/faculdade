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
Windows = 0
Unix = 0
Linux = 0
Netware = 0
Mac = 0
Outro = 0
while True:
    try:
        print("Qual o melhor Sistema Operacional para uso em servidores?")
        print("Digite um valor entre 1 a 6, e 0 para encerrar o programa")
        print("1 - Windows Server")
        print("2 - Unix")
        print("3 - Linux")
        print("4 - Netware")
        print("5 - Mac OS")
        print("6 - Outro")
        resposta = input()
        resposta = int(resposta)
        if resposta == 0:
            break
        if resposta == 1:
            Windows += 1
            continue
        if resposta == 2:
            Unix += 1
            continue
        if resposta == 3:   #talvez seja melhor por elif
            Linux += 1
            continue
        if resposta == 4:
            Netware += 1
            continue
        if resposta == 5:
            Mac += 1
            continue
        if resposta == 6:
            Outro += 1
            continue
        else:
            print("--por favor insira como solicitado acima--")
            continue
    except ValueError:
        print("--valor invalido, insira corretamente--")
        continue

Votos = [Windows, Unix, Linux, Netware, Mac, Outro]
sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
total = sum(Votos)
# Cabeçalho
print(f"\n{'Sistema Operacional':<20} {'Votos':>5} {'%':>5}")
print(f"{'-'*20} {'-'*5} {'-'*5}")

# Mostrando votos e porcentagem
for i in range(len(Votos)):
    if total > 0:
        pct = Votos[i] / total * 100
    else:
        pct = 0
    print(f"{sistemas[i]:<20} {Votos[i]:>5} {round(pct):>4}%")

print(f"{'-'*20} {'-'*5}")
print(f"{'Total':<20} {total:>5}")
