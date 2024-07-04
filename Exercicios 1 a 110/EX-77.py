# crie um codigo usando lista e faça uma lista ou texto e mostre so as vogais (a - e - i - o - u)
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'pratica',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
        print('\nna palavra {} temos'.format(p.upper()), end=' ')
        for letra in p:
                if letra.lower() in 'aeiou':
                        print(letra, end=' ')