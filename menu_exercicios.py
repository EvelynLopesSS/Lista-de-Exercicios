import exercicios.calculadora_notas as calculadora_notas
import exercicios.cupom_fiscal as cupom_fiscal
import exercicios.folha_pagamento_calculo as folha_pagamento_calculo
import exercicios.investigacao_criminosa as investigacao_criminosa
import exercicios.ordenador_numeros as ordenador_numeros
import exercicios.quantidade_centenas_dezenas_unidades as quantidade_centenas_dezenas_unidades
import exercicios.raizes_equacao_segundo_grau as raizes_equacao_segundo_grau
import exercicios.reajuste_salario as reajuste_salario

def main():
    print("Bem-vindo ao menu de exercícios!")
    print("Escolha o número do exercício que deseja executar:")
    print("1. Calculadora de Notas")
    print("2. Cupom Fiscal")
    print("3. Cálculo de Folha de Pagamento")
    print("4. Investigação Criminal")
    print("5. Ordenador de Números")
    print("6. Quantidade de Centenas, Dezenas e Unidades")
    print("7. Raízes de uma Equação de Segundo Grau")
    print("8. Reajuste de Salário")
    print("0. Sair")

    while True:
        try:
            escolha = int(input("Digite o número do exercício (0-8): "))
            if escolha == 0:
                print("Programa encerrado.")
                break
            elif 1 <= escolha <= 8:
                if escolha == 1:
                    calculadora_notas.main()
                elif escolha == 2:
                    cupom_fiscal.main()
                elif escolha == 3:
                    folha_pagamento_calculo.main()
                elif escolha == 4:
                    investigacao_criminosa.main()
                elif escolha == 5:
                    ordenador_numeros.main()
                elif escolha == 6:
                    quantidade_centenas_dezenas_unidades.main()
                elif escolha == 7:
                    raizes_equacao_segundo_grau.main()
                elif escolha == 8:
                    reajuste_salario.main()
            else:
                print("Número de exercício inválido. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

if __name__ == "__main__":
    main()
