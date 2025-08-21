#//Exercicio 1\\

#comparar a media de geral


nomes = {}

#input de 5 saltos, input de nomes
for i in range(5):
    nome = input("digite o nome do atleta: ")
    saltos = []
    for j in range(5):
        salto = input(f"Digite a distancia do {j+1}° salto: ")
        saltos.append(salto)
    nomes[nome] = saltos

#excluir o maior e o menor e tirar a media pra cada atleta
for nome, saltos in nomes.items():

    # remove o maior salto
    saltos.remove(max(saltos))
    
    # remove o menor salto
    saltos.remove(min(saltos))

    # agora a lista só tem os 3 valores do meio
    media = sum(saltos) / len(saltos)
    print(f"{nome} - média dos 3 saltos: {media:.2f}")
