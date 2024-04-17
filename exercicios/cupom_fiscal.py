from tabulate import tabulate

def calcular_preco_total(tipo_carne, quantidade, cartao_tabajara=False):
    precos = {
        "1": {"nome": "File Duplo", "preco_ate_5kg": 49, "preco_acima_5kg": 58},
        "2": {"nome": "Alcatra", "preco_ate_5kg": 59, "preco_acima_5kg": 68},
        "3": {"nome": "Picanha", "preco_ate_5kg": 69, "preco_acima_5kg": 78}
    }

    preco_unitario = precos[tipo_carne]["preco_ate_5kg"] if quantidade <= 5 else precos[tipo_carne]["preco_acima_5kg"]
    preco_total = preco_unitario * quantidade

    if cartao_tabajara:
        desconto = preco_total * 0.05
        preco_total -= desconto
        tipo_pagamento = "Cartão Tabajara"
    else:
        desconto = 0
        tipo_pagamento = "Dinheiro"

    return preco_total, desconto, tipo_pagamento, precos[tipo_carne]["nome"], preco_unitario

def main():
    try:
        precos = [
            ["1", "File Duplo", 49, 58],
            ["2", "Alcatra", 59, 68],
            ["3", "Picanha", 69, 78]
        ]
        print("Tabela de Preços:")
        print(tabulate(precos, headers=["Carne", "Tipo", "Até 5 Kg", "Acima de 5 Kg"], tablefmt="grid"))

        print("\nEscolha o tipo de carne:")
        print("1 - File Duplo")
        print("2 - Alcatra")
        print("3 - Picanha")

        opcao_carne = input("Digite o número ou o nome da carne escolhida: ").lower()

        if opcao_carne not in ["1", "file duplo", "2", "alcatra", "3", "picanha"]:
            print("Por favor, escolha uma opção válida.")
            return

        quantidade = float(input("Digite a quantidade de carne (em Kg): "))

        if quantidade <= 0:
            print("A quantidade deve ser positiva.")
            return

        cartao_tabajara_str = input("A compra foi feita no cartão Tabajara? (s/n): ").lower()
        cartao_tabajara = cartao_tabajara_str == "s"

        preco_total, desconto, tipo_pagamento, nome_carne, preco_unitario = calcular_preco_total(opcao_carne, quantidade, cartao_tabajara)

        print("\nCupom Fiscal:")
        nota_fiscal = [
            ["Tipo de carne", nome_carne],
            ["Quantidade (Kg)", quantidade],
            ["Preço unitário", preco_unitario],
            ["Preço total", round(preco_total, 2)],
            ["Tipo de pagamento", tipo_pagamento],
            ["Desconto", round(desconto, 2)],
            ["Valor a pagar", round(preco_total - desconto, 2)]
        ]
        print(tabulate(nota_fiscal, tablefmt="grid"))

    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    main()
