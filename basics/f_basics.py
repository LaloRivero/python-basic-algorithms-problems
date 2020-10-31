"""Pedir dos números y decir si uno es múltiplo del otro. """

def question(a,b):
    if(b%a):
        return False
    else:
        return True


def run():
    a = int(input("Type a number: "))
    b = int(input("Type a multiple of the number: "))
    print(question(a,b))


if __name__ == '__main__':
    run()