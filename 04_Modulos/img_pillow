from pathlib import Path
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

# Caminhos
ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'img_original.JPG'
MALUCA = ROOT_FOLDER / 'img_maluca.JPG'
REDIMENSIONADA = ROOT_FOLDER / 'img_redimensionada.JPG'

# Abrindo a imagem original
img = Image.open(ORIGINAL)

# 1. Versão maluca: inverter cores, aumentar contraste, aplicar blur
img_maluca = ImageOps.invert(img.convert('RGB'))
img_maluca = ImageEnhance.Contrast(img_maluca).enhance(2.5)
img_maluca = img_maluca.filter(ImageFilter.GaussianBlur(3))
img_maluca.save(MALUCA)
print(f'Imagem maluca salva em: {MALUCA}')

# 2. Versão redimensionada (largura ~600px, mantendo proporção)
largura, altura = img.size
nova_largura = 600
nova_altura = int((nova_largura / largura) * altura)
img_redimensionada = img.resize((nova_largura, nova_altura))
img_redimensionada.save(REDIMENSIONADA)
print(f'Imagem redimensionada salva em: {REDIMENSIONADA}')