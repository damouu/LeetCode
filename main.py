def duplicateZeros(array):
    i = 0
    lenn = len(array)
    while i < len(array):
        if i == (len(array) - 1) and array[-1] == 0:
            break
        if array[i] == 0 and array[i + 1] != 0:
            positionChange = array[i + 1:-1]
            array[i + 1] = 0
            del array[i + 2:]
            for key, value in enumerate(positionChange[:lenn - i]):
                array.append(value)
            for key, value in enumerate(positionChange):
                positionChange[key] = 0
            i += 2
        else:
            i += 1
    return array


class Solution(object):
    array = duplicateZeros([0, 0, 0, 0, 0, 0, 0])
    print(array)
