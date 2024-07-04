# CRIE UM CODIGO QUE PERGUNTE QUNATOS KM O USUARIO PERCORREU, QUANTOS DIAS O CARRO FICOU EM SUA POSSE
# KM = 0.20(KM VALER R$ 0.20) E DIA = R$90 (VALER R$90 O DIA COM O CARRO)

dia = int(input("Quantos dias o carro ficou em sua posse? "))
km = float(input("Digite os km percorridos =>"))
Dia_a_Pagar = dia * 90
KM_A_pagar = km * 0.20
tot = Dia_a_Pagar + KM_A_pagar
print(f"km perccoridos {km} a pagar R${KM_A_pagar}")
print(f"Total de dias que esteve em uso {dia} a pagar R${Dia_a_Pagar}")
print(f"O total a pagar é R${tot}")