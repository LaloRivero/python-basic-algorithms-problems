""" Pedir un número N, introducir N sueldos, y mostrar el sueldo máximo. """


def run():
    n = int(input())
    x = 0;
    max_n=0;
    for _ in range(0,n):
        x = int(input())
        if max_n < x:
            max_n = x;

    print(max_n)

if __name__ == '__main__':
    run()