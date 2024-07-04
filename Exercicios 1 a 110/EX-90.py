# crie um codigo para saber se um aluno passou de ano

media = dict()
nome = {}
for c in range(0, 1):
    nome = str(input('NOME DO ALUNO(A) => '))
    media = float(input(f'A MEDIA DE {nome} É => '))
print('-_-_'*10)
print(f'O NOME DO ALUNX É {nome} \nE A MÉDIA É {media}')
print(f'A SITUAÇÃO DO ALUNX É', end= ':\033[31m ')
if media >= 7:
    print('ALUNX APROVADO!! PARABÉNS')
elif media >= 5.9:
     print('ALUNO ESTÁ EM RECUPERAÇÃO!')
else:
    print('ALUNO ESTÁ REPROVADO!')