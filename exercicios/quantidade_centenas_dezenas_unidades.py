def calcular_centenas_dezenas_unidades(numero):
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    resultado = ""

    if centenas > 0:
        resultado += f"{centenas} {'centenas' if centenas > 1 else 'centena'}"
    
    if dezenas > 0:
        if centenas > 0:
            resultado += ", "
        resultado += f"{dezenas} {'dezenas' if dezenas > 1 else 'dezena'}"
    
    if unidades > 0:
        if centenas > 0 or dezenas > 0:
            resultado += " e "
        resultado += f"{unidades} {'unidades' if unidades > 1 else 'unidade'}"
    
    return resultado

def main():
    try:
        numero = int(input("Digite um número inteiro menor que 1000: "))
        if numero >= 1000:
            print("❌ O número deve ser menor que 1000.")
            return
        
        resultado = calcular_centenas_dezenas_unidades(numero)
        print(f"👉  O número {numero} possui {resultado}.")
    
    except ValueError:
        print("❌ Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()
