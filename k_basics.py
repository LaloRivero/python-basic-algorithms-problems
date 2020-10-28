""" Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene """

def question(a):

    if(a < 10):
        return 1
    elif(a>=10 and a < 100):
        return 2
    elif(a>=100 and a< 1000):
        return 3
    else:
        return 4

def run():
    a = int(input())
    print(question(a))


if __name__ == '__main__':
    run()