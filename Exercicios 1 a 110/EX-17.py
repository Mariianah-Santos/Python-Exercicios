# crie um codigo que descubra a hipotenusa

cateto = float(input('DIGITE O CATETO => '))
adj=float(input('DIGITE O ADJECENTER => '))
hipo = (cateto ** 2 + adj ** 2) ** (1/2)
print('A HIPOTENUSA DE {} E {} É IGUAL A {:.2f}'.format(cateto, adj, hipo))

# OU

import math
cateto = float(input('DIGITE O CATETO => '))
adj=float(input('DIGITE O ADJECENTER => '))
hipo = math.hypot(cateto, adj)
print('A HIPOTENUSA DE {} E {} É IGUAL A {:.2f}'.format(cateto, adj, hipo))