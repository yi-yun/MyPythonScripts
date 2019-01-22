import random
def QuickSort(array):
    if len(array) < 2:
        return array
    else:
        piovt = array[0]
        less = [i for i in array[1:] if i <= piovt]
        more = [i for i in array[1:] if i > piovt]
        return QuickSort(less) + [piovt] + QuickSort(more)


def QuickSortRandom(array):
    num = random.randint(0, len(array) - 1)
    array[0], array[num] = array[num], array[0]
    return QuickSort(array)


print(QuickSortRandom([10, 4, 2, 56, 23, 12]))


