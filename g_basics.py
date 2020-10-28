"""  Pedir dos números y decir cual es el mayor. """

def question(a,b):
    if(a>b):
        return f'{a} is greater than {b}'
    else:
        return f'{b} is greater than {a}'


def run():
    a = int(input())
    b = int(input())
    print(question(a,b))


if __name__ == '__main__':
    run()