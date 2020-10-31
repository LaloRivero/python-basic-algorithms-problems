""" Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar. """

def run(num):
    while num!= 0:
        num = int(input("Type a number (0 to exit):\n"))

        if num == 0:
            return
        elif num%2:
            print(f'{num} is an odd number')
        else:
            print(f'{num} is a pair number')


if __name__ == '__main__':
    run(1)