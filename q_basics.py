""" Pedir dos fechas y mostrar el número de días que hay de diferencia. Suponiendo todos los meses de 30 días. """

import math

def calc_days(day1, month1, year1, day2, month2, year2):
    year = abs(year1-year2)
    month = abs(month1-month2)
    day = abs(day1-day2)
    total_days = (year*365)+(month*30)+day

    return total_days



def run():
    day1 = int(input())
    month1 = int(input())
    year1 = int(input())
    day2 = int(input())
    month2 = int(input())
    year2 = int(input())
    print(calc_days(day1, month1, year1, day2, month2, year2))


if __name__ == '__main__':
    run()