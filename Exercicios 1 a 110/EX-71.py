# crie um codigo que pergunte o nome do produto e o valor.
# mostra na tela, os produtos mais caro que será maior que R$1000 os mais baratos abaixo de mil e mostra o total a ser pago.

total = 0
resposta = "S"
produto = 0
nome_produto = ""
maior = menor = 0
maior_nome = menor_nome = ""


while resposta in "S":
    nome_produto = str(input("Informe o nome do produto => "))
    produto = float(input("Informe o valor do produto R$"))
    print("-=-"*10)
    resposta = str(input("Voce quer adicionar mais algum produto? [S/N] ")).upper().strip()
    
    if produto > 1000:
        maior = produto
        maior_nome = nome_produto
    elif produto < 1000:
        menor = produto
        menor_nome = nome_produto
    total += produto
print("o maior produto é {} e custa R${}".format(maior_nome, maior))
print("o menor produto é {} e custa R${}".format( menor_nome, menor))
print("O total a pagar é R${}".format(total))