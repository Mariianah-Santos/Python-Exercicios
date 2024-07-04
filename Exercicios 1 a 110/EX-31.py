#crie um codigo de viagem, se a viagem for menor que 200km será calculada a passagem se fr maior que 200km irá caluclar
# menor que 200km a pgar por km o.50... maior que 20km a pagar 0.45

km = float(input("QUAL A DISTÂNCIA DO LOCAL? (KM) "))
valor_menor_200 = km * 0.50
valor_maior_200 = km * 0.45
if km <= 200:
    print(f" KM{km} A PASSAGEM ESTA SAINDO POR R${valor_menor_200}")

else:
    print(f"{km} A PASSAGEM ESTA SAINDO POR R${valor_maior_200}")

print("faça uma boa viagem")