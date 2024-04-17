class OrdenadorNumeros:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def ordenar_decrescente(self):
        lista_numeros = [self.num1, self.num2, self.num3]
        lista_numeros.sort(reverse=True)
        return lista_numeros


def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))

        ordenador = OrdenadorNumeros(num1, num2, num3)
        numeros_ordenados = ordenador.ordenar_decrescente()

        print("Números em ordem decrescente:")
        for numero in numeros_ordenados:
            print("🔽 5" + str(numero))

    except ValueError:
        print("Por favor, insira números válidos.")


if __name__ == "__main__":
    main()
