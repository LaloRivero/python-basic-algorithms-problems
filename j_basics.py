""" Pedir tres números y mostrarlos ordenados de mayor a menor. """

def question(a,b,c):
    if a==b and b==c:
        return f'{a} {b} {c}'
    elif a > b and b >= c:
        return f'{a} {b} {c}'
    elif a > c and c > b:
        return f'{a} {c} {b}'
    elif b > a and a >= c:
        return f'{b} {a} {c}'
    elif b > c and c > a:
        return f'{b} {c} {a}'
    elif c > a and a >= b:
        return f'{c} {a} {b}'
    elif c > b and b > a:
        return f'{c} {b} {a}'


def run():
    a = int(input())
    b = int(input())
    c = int(input())
    print(question(a,b,c))


if __name__ == '__main__':
    run()