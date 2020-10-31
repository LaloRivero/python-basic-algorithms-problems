""" Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo. """

def run(num):
    num = int(input("Type a number (0 to exit):\n"))

    if num!=0:
        print(f'result {num*num}')
        run(num)

    return

if __name__ == '__main__':
    run(1)