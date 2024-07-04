# Escreva um programa que solicite ao usuário sua idade e se ele é estudante
# (responda com S ou N). Exiba se ele tem direito à meia-entrada no cinema
# (condição: idade menor que 18 ou maior que 60 anos OU ser estudante).

idade = int(input("Idade: "))
estudante = str(input("VOCÊ É UM ESTUDANTE? OBS: DEVE POSSUIR A CARTEIRA DE ESTUDANTE [S/N] => ")).upper()

if estudante == "S":
    print("Cliente é um estudante e possui a Carteira de Estudante. MEIA ENTRADA: ACESSO LIBERADO")
else:
    print("Infelizmente o Cliente não é um estudante ou ão possui Carteira de Estudante: MEIA ENTRADA: ACESSO NEGADO")