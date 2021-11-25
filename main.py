import math


Statistics1 = 0
Statistics2 = 0


def shell1(arr):
    passes = math.floor(math.log(len(arr), 2))
    while passes >= 0:
        increment = int(pow(2, passes)) - 1
        for start in range(increment, len(arr), 1):
            arr = InsertionSort(arr, start, increment, 1)
        passes -= 1
    return arr


def shell2(arr):
    passes = math.floor(math.log(2 * len(arr) + 1, 3)) - 2
    while passes >= 0:
        increment = int(pow(3, passes)) + int(pow(3, passes - 1))
        for start in range(increment, len(arr), 1):
            arr = InsertionSort(arr, start, increment, 2)
        passes -= 1
    return arr


def InsertionSort(arr, start, gap, version):
    global Statistics1, Statistics2
    new_element = arr[start]
    location = start - gap
    while location >= 0 and arr[location] > new_element:
        if version == 1:
            Statistics1 += 1
        else:
            Statistics2 += 1
        arr[location + gap] = arr[location]
        location -= gap
    arr[location + gap] = new_element
    return arr


matr1 = []
matr2 = []

with open('input10.txt') as f:
    matr1 = [int(x) for x in next(f).split()]
with open('input10.txt') as f:
    matr2 = [int(x) for x in next(f).split()]
with open('output10.txt', 'a') as f:
    shell1(matr1)
    f.write(str(matr1))
    f.write('\n')
    shell2(matr2)
    f.write(str(matr2))
    f.write('\n')
    f.write(str(Statistics1))
    f.write('\n')
    f.write(str(Statistics2))
    f.write('\n')

