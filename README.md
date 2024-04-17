# Exercícios de Programação em Python

Este repositório contém uma coleção de exercícios de programação resolvidos em Python.

## Lista de Exercícios

### 01 - 📊 Média de Notas [![calculadora_notas.py](https://img.shields.io/badge/calculadora__notas.py-View-green)](calculadora_notas.py)

Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar a mensagem:

| Média | Situação                |
|-------|-------------------------|
| >= 7  | Aprovado                |
| < 7   | Reprovado               |
| 10    | Aprovado com Distinção |



### 02 -🔢 Ordenação de Números [![ordenador_numeros.py](https://img.shields.io/badge/ordenador__numeros.py-View-green)](ordenador_numeros.py)


Faça um Programa que leia três números e mostre-os em ordem decrescente.


### 03 - Reajuste Salarial [![reajuste_salario.py](https://img.shields.io/badge/reajuste__salario.py-View-green)](reajuste_salario.py)


Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

| Faixa Salarial         | Aumento |
|------------------------|---------|
| Até R$ 280,00          | 20%     |
| Entre R$ 280,00 e R$ 700,00 | 15% |
| Entre R$ 700,00 e R$ 1500,00 | 10% |
| Acima de R$ 1500,00    | 5%      |

Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.


### 04 -💵 Folha de Pagamento [![folha_pagamento_calculo.py](https://img.shields.io/badge/folha__pagamento__calculo.py-View-green)](folha_pagamento_calculo.py)


Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

| Faixa Salarial                 | Desconto |
|--------------------------------|----------|
| Até R$ 900,00                  | Isento   |
| Até R$ 1500,00 (inclusive)     | 5%       |
| Até R$ 2500,00 (inclusive)     | 10%      |
| Acima de R$ 2500,00            | 20%      |


Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de horas é 220.

| Descrição                | Valor        |
|--------------------------|--------------|
| Salário Bruto            | R$ 1100,00   |
| (-) IR (5%)              | R$ 55,00     |
| (-) INSS (10%)           | R$ 110,00    |
| FGTS (11%)               | R$ 121,00    |
| Total de descontos       | R$ 165,00    |
| Salário Líquido          | R$ 935,00    |


### 05 - 🧮 Raízes de uma Equação do Segundo Grau [![raizes_equacao_segundo_grau.py](https://img.shields.io/badge/raizes__equacao__segundo__grau.py-View-green)](raizes_equacao_segundo_grau.py)


Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, sendo encerrado;
- Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
- Se o delta calculado for igual a zero, a equação possui apenas uma raiz real; informe-a ao usuário;
- Se o delta for positivo, a equação possui duas raízes reais; informe-as ao usuário.



### 06 - 🔢 Quantidade de Centenas, Dezenas e Unidades [![quantidade_centenas_dezenas_unidades.py](https://img.shields.io/badge/quantidade__centenas__dezenas__unidades.py-View-green)](quantidade_centenas_dezenas_unidades.py)


Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades que ele possui. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1 e 7


### 07 - 🧾 Cupom Fiscal de Compra de Carnes [![cupom_fiscal.py](https://img.shields.io/badge/cupom__fiscal.py-View-green)](cupom_fiscal.py)


O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

|                          | Até 5 Kg         | Acima de 5 Kg    |
|--------------------------|------------------|------------------|
| File Duplo               | R$ 49,00 por Kg  | R$ 58,00 por Kg  |
| Alcatra                  | R$ 59,00 por Kg  | R$ 68,00 por Kg  |
| Picanha                  | R$ 69,00 por Kg  | R$ 78,00 por Kg  |

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.


### 08 - 🕵️‍♂️ Investigação Criminal [![investigacao_criminosa.py](https://img.shields.io/badge/investigacao__criminosa.py-View-green)](investigacao_criminosa.py)


Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".



