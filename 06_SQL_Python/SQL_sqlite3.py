import sqlite3
from pathlib import Path

# Caminho do banco de dados
DB_FILE = Path(__file__).parent / 'exemplo.sqlite3'

# Conexão e cursor
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Criação da tabela customers
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE
    )
    '''
)

# Criação da tabela orders
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product TEXT NOT NULL,
        price REAL,
        status TEXT,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )
    '''
)

# Adicionando uma nova coluna na tabela orders
cursor.execute(
    '''
    ALTER TABLE orders ADD COLUMN created_at TEXT
    '''
)
# Se a coluna já existir, ignore o erro
connection.commit()

# Inserindo dados em customers
customers = [
    ('Alice', 'alice@email.com'),
    ('Bob', 'bob@email.com'),
    ('Carol', 'carol@email.com'),
]
cursor.executemany(
    'INSERT OR IGNORE INTO customers (name, email) VALUES (?, ?)',
    customers
)

# Inserindo dados em orders
orders = [
    (1, 'Notebook', 2500.0, 'shipped', '2024-06-01'),
    (1, 'Mouse', 150.0, 'pending', '2024-06-02'),
    (2, 'Keyboard', 300.0, 'shipped', '2024-06-03'),
    (3, 'Monitor', 1200.0, 'cancelled', '2024-06-04'),
]
cursor.executemany(
    'INSERT INTO orders (customer_id, product, price, status, created_at) VALUES (?, ?, ?, ?, ?)',
    orders
)
connection.commit()

# Atualizando um dado
cursor.execute(
    '''
    UPDATE customers SET name = "Alice Smith" WHERE id = 1
    '''
)
connection.commit()

# Consulta complexa: buscar todos os pedidos enviados (shipped) OU acima de R$1000, mostrando nome do cliente e produto
cursor.execute(
    '''
    SELECT c.name, c.email, o.product, o.price, o.status, o.created_at
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE (o.status = "shipped" AND o.price > 200)
       OR (o.price >= 1000 AND o.status != "cancelled")
    ORDER BY o.created_at
    '''
)

print('Pedidos relevantes:')
for row in cursor.fetchall():
    name, email, product, price, status, created_at = row
    print(f'Cliente: {name} ({email}) | Produto: {product} | Preço: {price} | Status: {status} | Data: {created_at}')

# Fechando conexão
cursor.close()
connection.close()