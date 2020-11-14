""" Pedir números hasta que se teclee un 0, mostrar la suma de todos los números introducidos. """

def run():

    numbers = []
    num = int(input("Type a number:"))
    while num !=0:
        numbers.append(num)
        num = int(input("Type a number:"))

    for number in numbers:
        print(number, end=' ')


if __name__ == '__main__':
    run()