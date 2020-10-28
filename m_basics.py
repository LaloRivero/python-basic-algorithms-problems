""" Pedir un número entre 0 y 9.999, decir si es capicúa """

def question(a):
    if a == str(a[::-1]):
        return True
    else:
        return False

def run():
    a = input()
    print(question(a))


if __name__ == '__main__':
    run()