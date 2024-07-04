# crie um codigo que se o carro passar de 80km ele irá ser multado. para cada km ultrapassado é acrescetado 7 reais

km = float(input("Digite o km percorrido => "))
multa = (km - 80) * 7
if km > 80:
    print("VOCE FOI MULTADO POR ULTRAPSSA O LIMITE DE 80KM POR HORA")
    print(f"TOTAL A PAGAR R${multa}")
    
else:
    print("VOCE ESTA DIRIGINTO NA MEDIDA CERTA")