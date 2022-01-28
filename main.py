def duplicateZeros(array):
    i = 0
    while i < len(array):
        if array[i] == 0:
            positionChange = array[i + 1:-1]
            array[i + 1] = 0
            del array[i + 2:]
            array = array + positionChange
            positionChange.clear()
            i += 2
        else:
            i += 1
    return array


class Solution(object):
    array = duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
    print(array)
