def area():
    print('-'*20)


print('  CONTROLE DE ÁREA')
area()
lar = float(input('LARGURA (m) => '))
com = float(input('COMPRIMENTO (m) => '))
area1 = lar * com
print(f'A ÁREA DE UM TERRENO DE {lar} X {com} É IGUAL A {area1}m²')

# ou

def area():
    area1 = lar * com
    print(f'A ÁREA DE UM TERRENO DE {lar} X {com} É IGUAL A {area1}m²')


print('  CONTROLE DE ÁREA')
print('-'*20)
lar = float(input('LARGURA (m) => '))
com = float(input('COMPRIMENTO (m) => '))
area()