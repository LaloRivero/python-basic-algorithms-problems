""" Pedir el día, mes y año de una fecha correcta y mostrar la fecha del día siguiente. suponer que todos los meses tienen 30 días. """
""" Ídem que el ej. 17, suponiendo que cada mes tiene un número distinto de días (suponer que febrero tiene siempre 28 días). """

def questions(day, month, year):

    if month == 2 and day >= 28:
        day = 1
        month+=1
    elif month % 2 == 0 and day == 30:
        day = 1
        month+=1
    elif day == 31:
        day = 1
        month+=1
    else:
        day += 1

    if month == 13:
        month = 1
        year +=1

    return f'{day}-{month}-{year}'




def run():
    day = int(input())
    month = int(input())
    year = int(input())
    print(questions(day, month, year))


if __name__ == '__main__':
    run()