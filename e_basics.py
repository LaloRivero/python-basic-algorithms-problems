""" Pedir un número e indicar si es positivo o negativo. """

def question(a):
    if(a>=0):
        return 'Positive number'
    else:
        return 'Negative number'


def run():
    a = int(input())
    print(question(a))


if __name__ == '__main__':
    run()