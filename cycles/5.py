""" Realizar un juego para adivinar un número. Para ello pedir un número N, y luego ir pidiendo números
indicando “mayor” o “menor” según sea mayor o menor con respecto a N.
El proceso termina cuando el usuario acierta. """


def run(num):
    guess = int(input("Try to figure it out the number, type a number:\n"))

    if guess == num :
        print(f"Congrats the number is {num}!!")
    elif guess>num:
        print("The number you type is higher, try some number less.\n")
        run(num)
    elif guess<num:
        print("The number you type is lower, try some number higher.\n")
        run(num)


if __name__== "__main__":
    num = 47
    run(num)