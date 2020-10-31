""" Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien..."""

def question(a):
    if a==10:
        return 'Autonomo'
    elif a<10 and a>=9:
        return 'Destacado'
    elif a<9 and a>=8:
        return 'Bueno'
    elif a<8 and a>=7:
        return 'Suficiente'
    else:
        return 'Insuficiente'

def run():
    a = float(input())
    print(question(a))


if __name__ == '__main__':
    run()