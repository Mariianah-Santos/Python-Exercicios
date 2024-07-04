# crie um codigo que mostre um reajuster salarioa. Se o salario for inferior a R$ 1250 recebe um aumento de 15%
# se for maior que o R$1250 recebe um aumento de 10%

salario = float(input("Digite o seu salario R$"))
novoS_15 = salario + (salario * 15 / 100)
novoS_10 = salario + (salario * 10 / 100)
if salario >= 1250:
    print(f"VOCE TEVE UM REAJUSTER DE SALARIO R${salario} 10% de aument0")
    print(f"IRA PASSAR A RECEBER R${novoS_10}")
else:
    print(f"VOCE TEVE UM REAJUSTER DE SALARIO R${salario} 15% de aumento")
    print(f"IRA PASSAR A RECEBER R${novoS_15}")