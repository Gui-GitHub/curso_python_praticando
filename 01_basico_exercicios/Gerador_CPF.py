"""
Gerador de CPF válido - Simples e didático
Gera CPFs válidos usando os cálculos de dígito verificador.
"""

import random

try:
    numero_desejado = int(input("Deseja gerar quantos CPF's? "))
    if numero_desejado <= 0:
        print("Por favor, digite um número maior que zero.")
except:
    print("Entrada inválida. Digite apenas números inteiros.")

for _ in range(numero_desejado):
    # Gera os 9 primeiros dígitos do CPF
    cpf_base = ''
    for _ in range(9):
        cpf_base += str(random.randint(0, 9))

    # Calcula o primeiro dígito verificador
    soma_1 = 0
    regressivo_1 = 10
    for digito in cpf_base:
        soma_1 += int(digito) * regressivo_1
        regressivo_1 -= 1
    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Calcula o segundo dígito verificador
    cpf_com_digito_1 = cpf_base + str(digito_1)
    soma_2 = 0
    regressivo_2 = 11
    for digito in cpf_com_digito_1:
        soma_2 += int(digito) * regressivo_2
        regressivo_2 -= 1
    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # CPF final completo
    cpf_completo = f'{cpf_base}{digito_1}{digito_2}'
    print(f'CPF gerado: {cpf_completo}')
