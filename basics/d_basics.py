""" Pedir dos números y decir si son iguales o no. """

def question(a,b):
    if(a==b):
        return True
    else:
        return False


def run():
    a = int(input())
    b = int(input())
    print(question(a,b))


if __name__ == '__main__':
    run()