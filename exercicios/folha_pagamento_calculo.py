from tabulate import tabulate

def formatar_valor(valor_str):
    valor_str = valor_str.replace("R$", "").replace(" ", "")
    if "." in valor_str and "," in valor_str:
        #  "x.xxx,xx"
        valor_str = valor_str.replace(".", "").replace(",", ".")
    elif "." in valor_str:
        #  "x.xxx"
        valor_str = valor_str.replace(".", "")
    elif "," in valor_str:
        #  "xxx,xx"
        valor_str = valor_str.replace(",", ".")
    return float(valor_str)

def formatar_horas(horas_str):
    horas_str = horas_str.replace("h", ":")
    return int(horas_str.split(":")[0]) + int(horas_str.split(":")[1]) / 60

def calcular_folha_pagamento(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    fgts = salario_bruto * 0.11
    
    if salario_bruto <= 900:
        ir = 0
    elif salario_bruto <= 1500:
        ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        ir = salario_bruto * 0.10
    else:
        ir = salario_bruto * 0.20
    
    inss = salario_bruto * 0.10
    total_descontos = ir + inss + (salario_bruto * 0.03)
    salario_liquido = salario_bruto - total_descontos
    
    return salario_bruto, ir, inss, fgts, total_descontos, salario_liquido

def main():
    try:
        valor_hora_str = input("💲 Digite o valor da sua hora de trabalho: ")
        valor_hora = formatar_valor(valor_hora_str)
        
        horas_trabalhadas_str = input("🕐 Digite a quantidade de horas trabalhadas no mês: ")
        horas_trabalhadas = formatar_horas(horas_trabalhadas_str)
        
        salario_bruto, ir, inss, fgts, total_descontos, salario_liquido = calcular_folha_pagamento(valor_hora, horas_trabalhadas)
        
        tabela = [
            ["Salário Bruto", f"R$ {salario_bruto:.2f}"],
            ["(-) IR (5%)", f"R$ {ir:.2f}"],
            ["(-) INSS (10%)", f"R$ {inss:.2f}"],
            ["FGTS (11%)", f"R$ {fgts:.2f}"],
            ["Total de descontos", f"R$ {total_descontos:.2f}"],
            ["Salário Líquido", f"R$ {salario_liquido:.2f}"]
        ]
        
        print(tabulate(tabela, headers=["Descrição", "Valor"], tablefmt="fancy_grid"))
        
    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    main()
