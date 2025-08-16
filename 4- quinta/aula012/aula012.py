def solicitar_ano_nascimento():
    while True:
        ano = input("Por favor, digite seu ano de nascimento (ex: 1980): ")
        if ano.isdigit() and len(ano) == 4:
            return int(ano)
        else:
            print("Ano inválido. Digite um ano completo com 4 dígitos.")

def solicitar_numero_inteiro(mensagem):
    while True:
        num = input(mensagem)
        if num.isdigit():
            return int(num)
        else:
            print("Por favor, digite um número inteiro válido.")

def solicitar_opcao(mensagem, opcoes_validas):
    while True:
        opcao = input(mensagem).strip().lower()
        if opcao in opcoes_validas:
            return opcao
        else:
            print(f"Opção inválida. Escolha entre: {', '.join(opcoes_validas)}")

def main():
    print("=== Bem-vindo à nossa loja de vinhos! ===\n")

    endereco = input("Para começar, por favor informe seu endereço para entrega: ")

    ano_nascimento = solicitar_ano_nascimento()
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        print("Desculpe, não é permitida a venda de bebidas alcoólicas para menores de idade.")
        return

    vinhos = {
        "vinho tinto": 150.0,
        "vinho branco": 120.0,
        "vinho rosé": 100.0,
        "vinho reserva": 300.0,
        "vinho especial": 450.0
    }

    preco_medio = sum(vinhos.values()) / len(vinhos)
    preco_mais_caro = max(vinhos.values())
    preco_mais_barato = min(vinhos.values())

    print(f"\nAqui estão algumas informações sobre nossos vinhos:")
    print("sim")
