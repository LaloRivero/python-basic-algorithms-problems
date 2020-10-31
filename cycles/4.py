""" Pedir números hasta que se teclee uno negativo, y mostrar cuántos números se han introducido. """

def run(num):
    cont = 0

    while num>=0:
        num = int(input("Type a number (-1 to exit):\n"))
        cont+=1

    return cont

if __name__ == '__main__':
    print(run(1))