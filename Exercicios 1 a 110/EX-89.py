# crei um codigo para cadastra as notas de alunos

ficha = list()
r = 'S'
while r in 'S':
    nome = str(input('NOME: '))
    nota1 = float(input('PRIMEIRA NOTA: '))
    nota2 = float(input('SEGUNDA NOTA: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('QUER CONTINUAR? [S/N] => ')).upper().strip()[0]
print('-=' * 30)
print('Nº  NOME       MÉDIA')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>6.1f}')
while True:
    print('-'* 30)
    opc = int(input('MOSTRAR NOTAS DE QUAL ALUNO? (999 PARA INTERROMPER) => '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'NOTAS DO ALUNO[A] {ficha[opc][0]} É {ficha[opc][1]}')
print('>>>>>> VOLTE SEMPRE <<<<<<')