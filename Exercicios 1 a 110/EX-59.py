# crie um codigo para mostra dois valores e pergunta se o usuario quer soma, multiplica, dividir, subtrair, saber qual foi o maior eou sair do progrmaa.
soma = 0
multiplicacao = 0 
dividsao = 0
subtracao = 0 
maior = 0
opcao = 0 
num1 = int(input("informe um valor => "))
num2 = int(input("informe um valor => "))
while opcao != 7:
    print(""""Informe uma das opções do menu"
    [1] SOMA
    [2] MULTIPLICA
    [3] SUBTRAIR
    [4] DIVIDIR
    [5] MAIOR
    [6] NOVOS NUMEROS
    [7] SAIR DO PROGRAMA""")
    opcao = int(input("Informe um numero do menu :)"))
    if opcao == 1:
        soma = num1 + num2
        print("A soma dos valore é {}".format(soma))
        print("-=-"*10)
    elif opcao == 2:
        multiplicacao = num1 * num2
        print("A multiplicação dos numeros é {}".format(multiplicacao))
        print("-=-"*10)
    elif opcao == 3:
        subtracao = num1 - num2
        print("A subtração dos numeros é igual a {}".format(subtracao))
        print("-=-"*10)
    elif opcao == 4:
        dividsao = num1 / num2 
        print("A divisao dos numero sé {}".format(dividsao))
        print("-=-"*10)
    elif opcao == 5:
        if num1 > num2:
            maior = num1
            print("O maior numero entre {} e {} é {}".format(num1, num2, maior))
            print("-=-"*10)
        else:
            print("O maior numero entre {} e {} é {}".format(num1, num2, maior))
            print("-=-"*10)
    elif opcao == 6:
        num1 = int(input("informe um valor => "))
        num2 = int(input("informe um valor => "))
        print("-=-"*10)

    elif opcao == 7:
        print("OBRIGADA POR UTILIZAR NOSSO PROGRAMA")