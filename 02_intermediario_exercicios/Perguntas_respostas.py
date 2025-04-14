# Aqui eu digito minhas perguntas e respostas
perguntas = [
    {
        'Pergunta': 'Quanto é 3 + 5?',
        'Opções': ['5', '8', '9', '10'],
        'Resposta': '8',
    },
    {
        'Pergunta': 'Quanto é 7 x 6?',
        'Opções': ['42', '36', '40', '48'],
        'Resposta': '42',
    },
    {
        'Pergunta': 'Qual o resultado de 9 - 4?',
        'Opções': ['3', '4', '5', '6'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Qual o dobro de 12?',
        'Opções': ['22', '20', '24', '26'],
        'Resposta': '24',
    },
    {
        'Pergunta': 'Quanto é 81 dividido por 9?',
        'Opções': ['8', '9', '7', '6'],
        'Resposta': '9',
    },
]

# Inicializo a váriacel
qtd_acertos = 0

# Inicio meu for para cada pergunta
for pergunta in perguntas:
    # Separo cada pergunta e pulo linha
    print('Pergunta:', pergunta['Pergunta'], end='\n\n')

    # Separo as opções de cada pergunta, uma por uma
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()

    # Entrada de dados do funcionário
    escolha = input('Digite o número da opção correta: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    # Garanto que o dado seja int
    if escolha.isdigit():
        escolha_int = int(escolha)

    # Garanto que o usuário digitou algo válido e que contabilizou o acerto
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    # Mensagens de acertos e erros e o print final com os dados
    if acertou:
        qtd_acertos += 1
        print('✅ Acertou!')
    else:
        print('❌ Errou.')
    print('-' * 30)

print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')