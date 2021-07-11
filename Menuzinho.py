from time import sleep
import os
primeiro = int(
    input(
'\033[33mQual o primeiro número: \033[m'
))
segundo = int(
    input(
    '\033[33mQual o segundo número: \033[m'
    )
)
escolha = 0
while escolha != 5:
    print('''\033[33mEscolha o que deseja fazer com esses valores\033[m
\033[31m[ 1 ] somar\033[m
\033[32m[ 2 ] multiplicador\033[m
\033[34m[ 3 ] maior\033[m
\033[35m[ 4 ] novo número\033[m
\033[36m[ 5 ] sair do programa\033[m'''
)
    escolha = int(
        input(
        '\033[33mQual sua opção: \033[m'
        )
    )
    if escolha ==  1:
        soma =  primeiro + segundo
        print(
        '\033[31m{} + {} = {}\033[m'.format(primeiro, segundo, soma)
        )
    elif escolha == 2:
        multiplicação = primeiro * segundo
        print(
        '\033[32m{} X {} = {}\033[m'.format(primeiro, segundo, multiplicação)
        )
    elif escolha == 3:
        if primeiro < segundo:
            print(
            '\033[34mO número {} é maior que o {}\033[m'.format(segundo, primeiro)
            )
        if primeiro > segundo:
            print(
            '\033[34mO número {} é maior que o {}\033[m'.format(primeiro, segundo)
            )
        if primeiro == segundo:
            print(
            '\033[34mO número {} é igual a o {}\033[m'.format(primeiro, segundo)
            )
    elif escolha == 4:
        primeiro = int(
            input(
            'Qual o novo 1º número: '
            )
        )
        segundo = int(
            input(
            'Qual o novo 2º número: '
            )
        )
    elif escolha == 5:
        print('Fim do programa volte sempre!')
        sleep(2.5)
        os.system(
        'cls'
        )
    else:
        print(
        'Erro inconsistência na sua escolha tente novamente'
        )
    sleep(2)
     