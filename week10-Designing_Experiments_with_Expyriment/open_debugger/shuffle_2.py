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


NUM_ELEMS = 30
OKAY_ELEMS = 5
l1, l2, l3 = generate_lists2(NUM_ELEMS)
tmp_lists = []

for i in range(NUM_ELEMS // OKAY_ELEMS):
    tmp = l1[i * OKAY_ELEMS: (i + 1) * OKAY_ELEMS] + l2[i * OKAY_ELEMS: (i + 1) * OKAY_ELEMS] + l3[i * OKAY_ELEMS: (
                                                                                                                               i + 1) * OKAY_ELEMS]
    while not condition(tmp):
        random.shuffle(tmp)
    tmp_lists.append(tmp)

for i in range(len(tmp_lists) - 1):
    while not condition([tmp_lists[i][-1]] + [tmp_lists[i + 1][0]]):
        tmp_lists[i + 1] = tmp_lists[i + 1][1:] + [tmp_lists[i + 1][0]]

final_list = reduce(lambda x, y: x + y, tmp_lists)

print(final_list)