""" Pedir dos números y mostrarlos ordenados de mayor a menor """

def question(a,b):

    if(a>b):
        return f'{a} {b}'
    else:
        return f'{b} {a}'


def run():
    a = int(input())
    b = int(input())
    print(question(a,b))


if __name__ == '__main__':
    run()