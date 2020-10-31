""" Leer un número e indicar si es positivo o negativo. El proceso se repetirá hasta que se introduzca un 0. """

def run(num):
    num = int(input("Type a number (0 to exit):\n"))

    if num>0:
        print(f'{num} is a positive number\n')
        run(num)
    elif num<0:
        print(f'{num} is a negative number\n')
        run(num)
    else:
        return


if __name__ == '__main__':
    run(0)