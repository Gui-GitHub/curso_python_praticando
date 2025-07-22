import csv
from pathlib import Path

# Lista de produtos para salvar no CSV
produtos = [
    {"Nome": "Caneta", "Preço": 2.50, "Estoque": 100},
    {"Nome": "Caderno", "Preço": 15.90, "Estoque": 50},
    {"Nome": "Borracha", "Preço": 1.20, "Estoque": 200}
]

CAMINHO_CSV = Path(__file__).parent / "csv_produtos.csv"

# Escrevendo os produtos no arquivo CSV
with open(CAMINHO_CSV, "w", encoding="utf-8", newline="") as arquivo:
    colunas = produtos[0].keys()
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)
    escritor.writeheader()
    for produto in produtos:
        escritor.writerow(produto)

# Lendo os produtos do arquivo CSV
with open(CAMINHO_CSV, "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    print("Produtos cadastrados:")
    for linha in leitor:
        print(f"{linha['Nome']}: R$ {linha['Preço']} (Estoque: {linha['Estoque']})")
