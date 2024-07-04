# Crie um codigo que pergunte o NOME, SALARIO  e faça um reajuste de 15% no salario atual

nome = str(input("Digite o seu nome => "))
salario = float(input("Digite seu Salário R$"))
salario_Novo = salario + (salario * 15 /100)
print(f"""O COLABORADOR {nome} ATUALMENTE RECEBE R${salario}
O PROXIMO MÊS O COLABORADOR IRÁ RECEBER R${salario_Novo}""")