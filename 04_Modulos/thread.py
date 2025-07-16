from threading import Thread
from time import sleep

def baixar_arquivo(nome, tempo):
    """
    Simula o download de um arquivo.
    :param nome: Nome do arquivo
    :param tempo: Tempo para baixar (em segundos)
    """
    print(f'Iniciando download de {nome}...')
    sleep(tempo)
    print(f'{nome} baixado em {tempo}s.')

# Lista de arquivos simulados com tempo de download
arquivos = [
    ('arquivo1.txt', 3),
    ('arquivo2.txt', 2),
    ('arquivo3.txt', 5),
    ('arquivo4.txt', 1),
]

threads = []

# Cria e inicia uma thread para cada download
for nome, tempo in arquivos:
    t = Thread(target=baixar_arquivo, args=(nome, tempo))
    t.start()
    threads.append(t)

# Aguarda todas as threads terminarem
for t in threads:
    t.join()

print('Todos os downloads foram concluídos!')
