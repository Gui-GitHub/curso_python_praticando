import json
import os

# Exemplo: salvar e carregar uma lista de usuários em JSON

usuarios = [
    {"nome": "Alice", "idade": 30, "ativo": True},
    {"nome": "Bob", "idade": 25, "ativo": False},
    {"nome": "Carol", "idade": 22, "ativo": True}
]

CAMINHO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "JSON.json"
    )
)

# Salvando os dados em um arquivo JSON
with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(usuarios, arquivo, ensure_ascii=False, indent=2)

# Carregando os dados do arquivo JSON
with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
    usuarios_carregados = json.load(arquivo)

print("Usuários carregados do JSON:")
for usuario in usuarios_carregados:
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Ativo: {usuario['ativo']}")
