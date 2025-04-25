# Exercício - Lista de tarefas com desfazer e refazer
import os

# Criando todas as Defs para simplificar o código
# Listar as tarefas
def listar(tarefas):
    print() # Espaço em branco
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return # Se cair no if, ele sai da Def

    # Aparece todas as tarefas com TAB
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

# Desfazer alguma tarefa
def desfazer(tarefas, tarefas_refazer):
    print() # Espaço em branco
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return # Se cair no if, ele sai da Def

    # Elimina o último item, faz o print, e adiciona esse item a tarefas_refazer
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()

# Refazer a tarefa
def refazer(tarefas, tarefas_refazer):
    print() # Espaço em branco
    if not tarefas_refazer:
        print('Nenhuma tarefa para listar')
        return # Se cair no if, ele sai da Def
    
    # Elimina o último item, faz o print, e adiciona esse item a tarefas
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

# Adicionar a lista
def adicionar(tarefa, tarefas):
    print() # Espaço em branco
    tarefa = tarefa.strip() # Garantir que não há espaços
    if not tarefa:
        print('Nenhuma tarefa para listar')
        return # Se cair no if, ele sai da Def
    
    # Print e adiciona
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

# Inicializo as arrays fora das defs
tarefas = []
tarefas_refazer = []

# Iniciando o loop com o usuário final
while True:
    print('\n' + '-'*40)
    print('📋 Comandos: listar | desfazer | refazer | limpar | sair')
    print('-'*40)

    tarefa = input('📝  Digite uma tarefa ou comando: ').strip().lower()

    if tarefa == 'listar':
        listar(tarefas)
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
    elif tarefa == 'limpar':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif tarefa == 'sair':
        print('\n✅ Programa encerrado. Até a próxima!')
        break
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)