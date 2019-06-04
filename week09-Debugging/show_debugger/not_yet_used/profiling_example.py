import random

RANGE = 5000000

A = [i for i in range(RANGE)]

def do_stuff():
    a = (1+1)*2-2+5**random.randint(1, 3)
    b = a**2
    c = 0
    while c < b:
        c += 1
    return c*b


def do_other_stuff():
    a = A
    b = random.randint(0, RANGE)
    c = check(a, b)
    return c


def check(a, b):
    return (b in a)


def main():
    for i in range(1000):
        do_stuff()
        do_other_stuff()





if __name__ == '__main__':
    main()