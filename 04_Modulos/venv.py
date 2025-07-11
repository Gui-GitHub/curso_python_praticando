import os
from dotenv import load_dotenv  # pip install python-dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Obtendo as variáveis de ambiente
bd_user = os.getenv("BD_USER")
bd_password = os.getenv("BD_PASSWORD")
bd_port = os.getenv("BD_PORT")
bd_host = os.getenv("BD_HOST")

# Exemplo de uso das variáveis de ambiente
print("Configurações do banco de dados (usando variáveis de ambiente):")
print(f"Usuário: {bd_user}")
print(f"Senha: {bd_password}")
print(f"Host: {bd_host}")
print(f"Porta: {bd_port}")

# Você pode usar essas variáveis para configurar conexões, autenticação,
# ou qualquer outro recurso que precise ser protegido ou alterado facilmente.

if bd_user and bd_password:
    print("Usuário e senha definidos, pronto para autenticação segura!")
else:
    print("Usuário ou senha não definidos, verifique seu arquivo .env.")

