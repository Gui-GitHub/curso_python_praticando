import os

palavra_secreta = 'Propaganda'
letras_acertadas = ''
numero_tentativas = 0

# Inicio o Loop do meu jogo
while True:
    # Somo as tentativas e inicio o jogo com o Input do usuário
    letra_digitada = input('Digite uma letra ([S] para sair): ').lower()
    numero_tentativas += 1

    # Caso ele queira sair do jogo, basta digita 's' ou 'S'
    if letra_digitada == 's':
        print('Saindo do jogo...')
        break

    # Verificação de apenas 1 letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    # Adiciona a váriavel letra acertadas se o input estiver correto
    if letra_digitada in palavra_secreta.lower():
        letras_acertadas += letra_digitada

    # A palavra formada sempre contém um * como se fosse uma senha escondendo o jogo
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta.lower() in letras_acertadas:
            palavra_formada += letra_secreta  # mantém a letra original (com maiúscula, se houver)
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    # Assim que acerta, o sistema limpa o prompt, parabenizamos o usuário e mostramos estatísticas sobre o jogo
    if palavra_formada.lower() == palavra_secreta.lower():
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você ganhou, PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
