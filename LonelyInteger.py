import sys


def lonely_integer(a):
    vCounts = dict()
    for values in a:
        vCounts[values] = vCounts.get(values, 0)+1
    lst = list()
    for key, val in vCounts.items():
        lst.append((val, key))
    lst.sort(reverse=False)
    retVal = lst[0][1]
    return retVal

n = int(input().strip())
a = [a_temp for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
