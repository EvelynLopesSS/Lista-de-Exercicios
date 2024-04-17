class Aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media == 10:
            return "Aprovado com Distinção 🌟"
        elif media >= 7:
            return "Aprovado 😊"
        else:
            return "Reprovado 😔"


def main():
    try:
        nota1 = float(input("Digite a primeira nota parcial: "))
        nota2 = float(input("Digite a segunda nota parcial: "))

        aluno = Aluno(nota1, nota2)
        resultado = aluno.verificar_aprovacao()
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Por favor, insira notas válidas.")


if __name__ == "__main__":
    main()
