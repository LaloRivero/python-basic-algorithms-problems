""" Pedir los coeficientes de una ecuación de 2º grado, y muestre sus soluciones reales.
Si no existen, debe indicarlo. """

import math


def calc(a,b,c):
    op = (b*b)-(4*a*c)
    if op >= 0:
        result1 = (-b+math.sqrt(op))/(2*a)
        result2 = (-b-math.sqrt(op))/(2*a)
        return f'x1={result1}, x2={result2}'
    else:
        return 'Operation not posible'


def run():
    a = float(input())
    b = float(input())
    c = float(input())

    print(calc(a,b,c))



if __name__ == '__main__':
    run()