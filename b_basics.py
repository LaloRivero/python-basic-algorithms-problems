""" Pedir el radio de un círculo y calcular su área. A=PI*r^2. """

def calc_area(pi,r):
    return(pi*r*r)


def run():
    pi = 3.1416
    r=float(input())
    print(calc_area(pi,r))


if __name__ == '__main__':
    run()