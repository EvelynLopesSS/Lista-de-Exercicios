def fazer_perguntas():
    respostas_positivas = 0
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    for pergunta in perguntas:
        resposta = input(f"{pergunta} (s/n): ").lower()
        if resposta == "s":
            respostas_positivas += 1
    return respostas_positivas

def classificar_participacao(respostas_positivas):
    if respostas_positivas == 2:
        return "🕵️ Suspeita"
    elif 3 <= respostas_positivas <= 4:
        return "🧑‍🤝‍🧑 Cúmplice"
    elif respostas_positivas == 5:
        return "🔪 Assassino"
    else:
        return "😇 Inocente"

def main():
    try:
        print("Responda às perguntas com 's' para sim e 'n' para não.")
        respostas_positivas = fazer_perguntas()
        classificacao = classificar_participacao(respostas_positivas)
        print("Classificação:", classificacao)
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    main()
