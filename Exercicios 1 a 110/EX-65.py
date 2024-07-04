# crie um codigo que mostre o maior, menor e a media dos numeros digitados.
# usa a função WHILE e pergunte se o usuario deseja continua

cont = 0
media = 0
menor = 0
maior = 0
soma = 0 
numero = 0
resposta = "S"
while resposta in "Ss":
    numero = int(input("Digite um valor => "))
    soma += numero
    cont += 1
    media = soma / cont
    resposta = str(input("Deseja continuar? [S/N] => ")).strip().upper()
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print("A SOMA É {} A MEDIA É {} QUANTAS VEZES FORAM DIGITADOS {} O MAIOR NUMERO É {} E O MENOR NUMERO É {}".format(soma, media, cont, maior, menor))