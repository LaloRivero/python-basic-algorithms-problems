""" Pedir una hora de la forma hora, minutos y segundos, y mostrar la hora en el segundo siguiente. """

def questions(hour, min, sec):
    sec+=1

    if sec == 60:
        sec = 0
        min+=1

    if min == 60:
        min = 0
        hour +=1

    if hour == 13:
        hour = 1

    return f'{hour} : {min} : {sec}'




def run():
    sec = int(input())
    min = int(input())
    hour = int(input())
    print(questions(sec, min, hour))


if __name__ == '__main__':
    run()