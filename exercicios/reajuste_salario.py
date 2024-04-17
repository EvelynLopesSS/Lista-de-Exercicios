from tabulate import tabulate

class ReajusteSalario:
    def __init__(self, salario):
        self.salario = salario

    def calcular_reajuste(self):
        if self.salario <= 280:
            percentual = 20
        elif self.salario <= 700:
            percentual = 15
        elif self.salario <= 1500:
            percentual = 10
        else:
            percentual = 5

        aumento = (self.salario * percentual) / 100
        novo_salario = self.salario + aumento

        return percentual, aumento, novo_salario


def formatar_salario(salario_str):
    salario_str = salario_str.replace("R$", "").replace(" ", "")
    if "." in salario_str and "," in salario_str:
        #  "x.xxx,xx"
        salario_str = salario_str.replace(".", "").replace(",", ".")
    elif "." in salario_str:
        #  "x.xxx"
        salario_str = salario_str.replace(".", "")
    elif "," in salario_str:
        #  "xxx,xx"
        salario_str = salario_str.replace(",", ".")
    return float(salario_str)

def main():
    try:
        salario_str = input("Digite o salário atual do colaborador: ")

        salario = formatar_salario(salario_str)

        reajuste = ReajusteSalario(salario)
        percentual, aumento, novo_salario = reajuste.calcular_reajuste()
        print("📋 Detalhes do reajuste:")
        print(tabulate([
            ["Salário antes do reajuste", f"R$ {salario:.2f}"],
            ["Percentual de aumento aplicado", f"{percentual}%"],
            ["Valor do aumento", f"R$ {aumento:.2f}"],
            ["Novo salário após o aumento", f"R$ {novo_salario:.2f}"]
        ], headers=["Descrição", "Valor"], tablefmt="fancy_grid"))

    except ValueError:
        print("Por favor, insira um valor válido para o salário.")


if __name__ == "__main__":
    main()