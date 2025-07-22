from PyPDF2 import PdfWriter, PdfReader
from pathlib import Path

# Caminhos
PASTA_RAIZ = Path(__file__).parent
PDF_ORIGINAL = PASTA_RAIZ / 'pdf_original.pdf'
NOVO_PDF = PASTA_RAIZ / 'pdf_editado.pdf'

# 1. Criando um PDF do zero
writer = PdfWriter()

# Adicionando uma página em branco
writer.add_blank_page(width=200, height=200)

# Salvando o PDF criado
with open(PDF_ORIGINAL, 'wb') as f:
    writer.write(f)

# 2. Agora vamos ler e manipular o PDF criado
reader = PdfReader(PDF_ORIGINAL)

# Extraindo informações do PDF
print(f'Número de páginas: {len(reader.pages)}')

# Adicionando texto em uma nova página (PyPDF2 não escreve texto diretamente em páginas existentes)
# Para adicionar texto, normalmente é necessário usar uma biblioteca como reportlab,
# mas podemos adicionar uma página em branco e depois mesclar com outra que tenha texto.
# Aqui, apenas mostramos como adicionar páginas e ler o PDF.

# 3. Adicionando uma nova página ao PDF existente
writer2 = PdfWriter()
for page in reader.pages:
    writer2.add_page(page)

# Adicionando outra página em branco
writer2.add_blank_page(width=200, height=200)

with open(NOVO_PDF, 'wb') as f:
    writer2.write(f)

print('PDF criado e manipulado com sucesso!')
