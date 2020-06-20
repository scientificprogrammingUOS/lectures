import numpy
import random
from functools import reduce

def condition(ls):
    """returns False if two consecutive list-elements start with the same letter, else True"""
    return reduce(lambda x,y: False if x is False or x[0]==y[0] else y, ls) != False

def generate_lists2(num_elems):
    l1 = list(["A" + str(i) for i in range(num_elems)])
    l2 = list(["B" + str(i) for i in range(num_elems)])
    l3 = list(["C" + str(i) for i in range(num_elems)])
    for ls in [l1, l2, l3]:
        random.shuffle(ls)
    return l1, l2, l3

lists = generate_lists2(30)

# print(lists)
# print(list(numpy.where(list_allowed))[0])


amdone = False
while not amdone:
    try:
        list_allowed = [True, True, True]
        indices = [0, 0, 0]
        merged = []
        for _ in range(sum(len(i) for i in lists)):
            next_val = random.choice(list(numpy.where(list_allowed))[0])
            merged.append(lists[next_val][indices[next_val]])
            indices[next_val] += 1
            list_allowed = [True, True, True]
            list_allowed[next_val] = False
            for i in range(len(indices)):
                if indices[i] >= len(lists[i]):
                    list_allowed[i] = False
    except IndexError:
        pass
    else:
        amdone = True

print(merged)