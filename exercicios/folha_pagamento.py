def calcular_folha_pagamento(valor_hora, horas_trabalhadas):
    try:
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
        
        return [
            ["Salário Bruto", f"R$ {salario_bruto:.2f}"],
            ["(-) IR (5%)", f"R$ {ir:.2f}"],
            ["(-) INSS (10%)", f"R$ {inss:.2f}"],
            ["FGTS (11%)", f"R$ {fgts:.2f}"],
            ["Total de descontos", f"R$ {total_descontos:.2f}"],
            ["Salário Líquido", f"R$ {salario_liquido:.2f}"]
        ]

    except ValueError:
        print("Por favor, insira valores válidos.")

if __name__ == "__main__":
    valor_hora_str = input("💲 Digite o valor da sua hora de trabalho: ")
    valor_hora = float(valor_hora_str)
    
    horas_trabalhadas_str = input("🕐 Digite a quantidade de horas trabalhadas no mês: ")
    horas_trabalhadas = float(horas_trabalhadas_str)
    
    folha_pagamento = calcular_folha_pagamento(valor_hora, horas_trabalhadas)
    for item in folha_pagamento:
        print(item)
