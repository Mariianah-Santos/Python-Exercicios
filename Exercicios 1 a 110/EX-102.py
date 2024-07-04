from math import factorial
def fatorial():
    num = int(input('DIGITE O FATORIAL: '))
    print(f'O FATORIAL DE {num} É IGUAL A {factorial(num)}')
    for c in range(num, 0, -1):
        print(f'{c} x', end=' ')
    print(factorial(num))
    print('-'*30)


fatorial()

# ou

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print(' x ', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f



print(fatorial(5, show=False))