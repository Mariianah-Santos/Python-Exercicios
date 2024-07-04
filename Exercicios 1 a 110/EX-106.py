c = ('\033[m',              #0 - sem cores
    '\033[0:30:41m',         # 1 - vermelho
    )
def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO \ {com}\'', 0)
    print(c[1])
    help(com)

def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)
    print(c[0], end='')

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PHYHELP', 1)
    comando = str(input('FUNÇÃO OU BIBLIOTECA? '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo('ATE LOGO!', 1)