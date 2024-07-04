# CRIE UM CODIGO PARA DESCOBRI QUANTO DE TINTA UMA PAREDE VAI PRECISAR (precisa calcular altura, largura e a area do local)

largura = float(input("Digite a largura da parede => "))
altura = float(input("Digite a altura da parede => "))
area = largura * altura
print(f'SUA PAREDE TEM DIMESÃO DE {largura}X{altura} E SUA AREA {area}')
tinta = area/2
print("O total de litros de tinta é {}".format(tinta))