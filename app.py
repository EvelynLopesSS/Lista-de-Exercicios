from flask import Flask, render_template, request, redirect, url_for
from exercicios.calculadora_notas import Aluno
from exercicios.cupom_fiscal import calcular_preco_total
from exercicios.folha_pagamento  import calcular_folha_pagamento
from exercicios.investigacao_criminosa import fazer_perguntas, classificar_participacao
from exercicios.ordenador_numeros import OrdenadorNumeros
from exercicios.quantidade_centenas_dezenas_unidades import calcular_centenas_dezenas_unidades
from exercicios.raizes_equacao_segundo_grau import calcular_raizes
from exercicios.reajuste_salario import formatar_salario, ReajusteSalario

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculadora_notas', methods=['GET', 'POST'])
def calculadora_notas():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        aluno = Aluno(nota1, nota2)
        resultado = aluno.verificar_aprovacao()
        return render_template('calculadora_notas.html', resultado=resultado)
    return render_template('calculadora_notas.html')

@app.route('/cupom-fiscal', methods=['GET', 'POST'])
def cupom_fiscal():
    if request.method == 'POST':
        tipo_carne = request.form['tipo_carne']
        quantidade = float(request.form['quantidade'])
        
        # Verifica se o checkbox foi marcado
        cartao_tabajara = request.form.get('cartao_tabajara') == 'on'

        preco_total, desconto, tipo_pagamento, nome_carne, preco_unitario = calcular_preco_total(tipo_carne, quantidade, cartao_tabajara)

        nota_fiscal = [
            ["Tipo de carne", nome_carne],
            ["Quantidade (Kg)", quantidade],
            ["Preço unitário", preco_unitario],
            ["Preço total", round(preco_total, 2)],
            ["Tipo de pagamento", tipo_pagamento],
            ["Desconto", round(desconto, 2)],
            ["Valor a pagar", round(preco_total - desconto, 2)]
        ]

        return render_template('cupom_fiscal.html', nota_fiscal=nota_fiscal)

    return render_template('cupom_fiscal.html')

@app.route('/folha-pagamento', methods=['GET', 'POST'])
def folha_pagamento():
    if request.method == 'POST':
        valor_hora = float(request.form['valor_hora'].replace(',', '.'))
        horas_trabalhadas_str = request.form['horas_trabalhadas']
        
        horas_trabalhadas_str = horas_trabalhadas_str.replace(':', '.')
        horas_trabalhadas = float(horas_trabalhadas_str)
        
        folha_pagamento = calcular_folha_pagamento(valor_hora, horas_trabalhadas)

        return render_template('folha_pagamento.html', folha_pagamento=folha_pagamento)

    return render_template('folha_pagamento.html')

@app.route('/investigacao-criminal', methods=['GET', 'POST'])
def investigacao_criminal():
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    
    if request.method == 'POST':
        respostas = [request.form[f'pergunta{i}'] for i in range(1, 6)]
        respostas_positivas = sum(1 for resposta in respostas if resposta == 's')
        classificacao = classificar_participacao(respostas_positivas)
        return render_template('investigacao_criminal.html', perguntas=perguntas, classificacao=classificacao)

    return render_template('investigacao_criminal.html', perguntas=perguntas)

@app.route('/ordenador-numeros', methods=['GET', 'POST'])
def ordenador_numeros():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        num3 = float(request.form['num3'])

        ordenador = OrdenadorNumeros(num1, num2, num3)
        numeros_ordenados = ordenador.ordenar_decrescente()

        return render_template('ordenador_numeros.html', numeros_ordenados=numeros_ordenados)

    return render_template('ordenador_numeros.html')

@app.route('/quantidade-centenas-dezenas-unidades', methods=['GET', 'POST'])
def quantidade_centenas_dezenas_unidades():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        if numero >= 1000:
            return render_template('quantidade_centenas_dezenas_unidades.html', resultado="❌ O número deve ser menor que 1000.")
        
        resultado = calcular_centenas_dezenas_unidades(numero)
        return render_template('quantidade_centenas_dezenas_unidades.html', numero=numero, resultado=resultado)

    return render_template('quantidade_centenas_dezenas_unidades.html')

@app.route('/raizes-equacao-segundo-grau', methods=['GET', 'POST'])
def raizes_equacao_segundo_grau():
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            resultado = calcular_raizes(a, b, c)
            return render_template('raizes_equacao_segundo_grau.html', resultado=resultado)

        except ValueError:
            return render_template('raizes_equacao_segundo_grau.html', resultado="Por favor, insira valores numéricos válidos.")

    return render_template('raizes_equacao_segundo_grau.html')

@app.route('/reajuste-salarial', methods=['GET', 'POST'])
def reajuste_salarial():
    detalhes_reajuste = None
    if request.method == 'POST':
        salario_str = request.form['salario_atual']
        salario_str = salario_str.replace(',', '.') 
        salario = formatar_salario(salario_str)
        
        reajuste = ReajusteSalario(salario)
        percentual, aumento, novo_salario = reajuste.calcular_reajuste()

        detalhes_reajuste = [
            ["Salário antes do reajuste", f"R$ {salario:.2f}"],
            ["Percentual de aumento aplicado", f"{percentual}%"],
            ["Valor do aumento", f"R$ {aumento:.2f}"],
            ["Novo salário após o aumento", f"R$ {novo_salario:.2f}"]
        ]

    return render_template('reajuste_salario.html', detalhes_reajuste=detalhes_reajuste)

if __name__ == '__main__':
    app.run(debug=True)
