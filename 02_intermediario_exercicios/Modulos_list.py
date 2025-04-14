import copy
from dados import produtos

# Gerando uma nova lista com aumento de 10% no preço de cada produto
# Utiliza copy.deepcopy para evitar modificar a lista original
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in 
    copy.deepcopy(produtos)
]

# Ordena os produtos por nome em ordem decrescente (Z → A)
# Também usa deepcopy para preservar os dados originais
produtos_decrescente = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# Ordena os produtos por preço em ordem crescente (menor para maior)
# deepcopy garante que a lista original continue intacta
produtos_preco_crescente = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# Exibindo os resultados formatados
print('NOVOS PRODUTOS (com 10% de aumento):', *novos_produtos, sep='\n')
print('PRODUTOS ORDENADOS POR NOME (decrescente):', *produtos_decrescente, sep='\n')
print('PRODUTOS ORDENADOS POR PREÇO (crescente):', *produtos_preco_crescente, sep='\n')
