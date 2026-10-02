# Loop while

import os
os.system('cls')

while True:
    os.system('cls')
    print('''
    1) Estou com fome
    2) Estou com sede
    3) Quero minha mãe

    0) Sair
    ''')

    x = input("Escolha uma opção: ")

    if x == '0':
        print('Acabou')
        break

    if x == '1':
        print('Vai comer')
        input('Tecle [Enter] para continuar.')

