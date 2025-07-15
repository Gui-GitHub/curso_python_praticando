# Exemplo prático de automação com Selenium no Chrome
# pip install selenium

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

# Caminho para o chromedriver
ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    """Cria uma instância do navegador Chrome com opções extras."""
    chrome_options = webdriver.ChromeOptions()
    for option in options:
        chrome_options.add_argument(option)
    chrome_service = Service(executable_path=str(CHROME_DRIVER_PATH))
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser

if __name__ == '__main__':
    print("Iniciando o navegador Chrome...")
    # Permite autoplay sem interação do usuário
    browser = make_chrome_browser('--autoplay-policy=no-user-gesture-required')
    print("Navegador iniciado!")

    print("Acessando o vídeo surpresa no YouTube...")
    browser.get('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    print("Aguardando o player carregar...")
    sleep(5)  # Aguarda o vídeo carregar

    print("Curtindo a música por 60 segundos...")
    sleep(60)

    print("Fechando o navegador.")
    browser.quit()
    print("Navegador fechado. Fim!")