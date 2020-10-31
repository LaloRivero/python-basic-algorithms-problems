""" Pedir un número entre 0 y 9.999 y mostrarlo con las cifras al revés. """

def question(a):
    return str(a[::-1])

def run():
    a = input()
    print(question(a))


if __name__ == '__main__':
    run()