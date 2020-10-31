"""
Pedir una nota numérica entera entre 0 y 10, y mostrar dicha nota de la forma: cero, uno, dos, tres...
Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y seis.

"""

def questions(num):

    switcher = {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis",
        7: "siete",
        8: "ocho",
        9: "nueve",
        10: "diez",
        11: "once",
        12: "doce",
        13: "Trece",
        14: "catorce",
        15: "quince",
        20: "veinte",
        30: "treinta",
        40: "cuarenta",
        50: "cincuenta",
        60: "sesenta",
        70: "setenta",
        80: "ochenta",
        90: "noventa",
        100: "cien"
    }

    u_num = num%10
    d_num = num - num%10

    if num <= 15:
        return switcher.get(num)
    else:
        if num%10 == 0:
            return switcher.get(d_num)
        return f'{switcher.get(d_num)} y {switcher.get(u_num)}'


def run():
    num = int(input())
    print(questions(num))


if __name__ == '__main__':
    run()