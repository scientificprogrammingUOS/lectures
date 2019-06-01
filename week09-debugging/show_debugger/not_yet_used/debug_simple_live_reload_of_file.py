import util.number_range

#import util.number_range; from importlib import reload; reload(util.number_range)

test_value = util.number_range.test_value

for i in range(0,10):
    if test_value[i] == i:
        print("found the value: " + i)