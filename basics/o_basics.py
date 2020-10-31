""" Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo todos los meses de 30 días.
    Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. Con meses de 28, 30 y 31 días. Sin años bisiestos.
"""

def questions(day, month, year):

    if(day>0 and day <= 31 and month > 0 and month <= 12 and year > 0):
        
        if month % 2 == 0 and day > 30:
            return 'Incorrect Date'
        else:
            if month == 2 and day > 28:
                return 'Incorrect Date'
            return 'Correct Date'

    return 'Incorrect Date'


def run():
    day = int(input())
    month = int(input())
    year = int(input())
    print(questions(day, month, year))


if __name__ == '__main__':
    run()