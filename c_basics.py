""" Pedir el radio de una circunferencia y calcular su longitud. L=2*PI*r. """

def calc_circ(pi,r):
    return(2*pi*r)


def run():
    pi = 3.1416
    r=float(input())
    print(calc_circ(pi,r))


if __name__ == '__main__':
    run()