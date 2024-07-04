# 9. Escreva um programa que solicite ao usuário o valor de um empréstimo, a
#taxa de juros mensal e o número de meses do empréstimo, e exiba o valor
# total a ser pago (incluindo juros).

print("taxa de juros de 15%")

din_emprestimo = float(input("informe o valor do emprestimo R$"))
prestacao = int(input("informe em quantas vezes irá pagar => "))
juros = din_emprestimo + (din_emprestimo * 15 /100)
mensal = din_emprestimo / prestacao
print("total a pagar R${}".format(juros))
print("prestação ficou em {} vezes de R${}".format(prestacao, mensal))

