# crie um codigo que pergunte o nome, sexo e idade dos usuarios. Depois mostre a media do grupo (vai soma e dividir pela quantidade de cadastros)
# mostras os homens mais velhos e mostrar as mulheres que possua menos de 20 anos.

Homens_Velhos = 0
mulheres_idade20 = 0
soma = 0
media = 0
idadeHomem = 0

for indice in range (1, 5):
    nome = str(input("Nome {}º ".format(indice))).strip()
    idade = int(input("{}º Informe sua idade => ".format(indice)))
    sexo = str(input("{}º Informe seu sexo [M/F] => ".format(indice))).strip()
    soma += idade
    media = soma/indice
    if indice == 1 and sexo in "Mm":
        Homens_Velhos = nome
        idadeHomem = idade
    elif sexo in 'Mm' and idade > idadeHomem:
        idadeHomem = idade
        Homens_Velhos = nome
    elif sexo in 'Ff' and idade < 20:
        mulheres_idade20 += 1
print('A MEDIA EM GRUPO É {}'.format(media))
print('O HOMEM MAIS VELHO É {} COM {} ANOS! '.format(Homens_Velhos, idadeHomem))
print('MULHERES COM MENOS DE 20 SÃO {}'.format(mulheres_idade20))
