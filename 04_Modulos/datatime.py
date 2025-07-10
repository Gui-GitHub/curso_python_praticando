from datetime import datetime

# Exemplo: calcular quantos dias faltam para um evento (ex: aniversário)
data_atual = datetime.now()
# Suponha que o aniversário seja em 15 de setembro de 2026
data_aniversario = datetime.strptime('15/09/2026', '%d/%m/%Y')

# Calculando a diferença entre as datas
diferenca = data_aniversario - data_atual

print(f"Hoje é: {data_atual.strftime('%d/%m/%Y')}")
print(f"Seu aniversário é em: {data_aniversario.strftime('%d/%m/%Y')}")
print(f"Faltam {diferenca.days} dias para o seu aniversário!")

# Exemplo extra: formatando data e hora atual para exibir em um relatório
print("Data e hora atual formatada:", data_atual.strftime('%d/%m/%Y %H:%M:%S'))
