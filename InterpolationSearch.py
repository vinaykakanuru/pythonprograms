l = [2, 6, 11, 19, 27, 31, 45, 121]


def interpolation_search(values, x):
    idx0 = 0
    idxn = len(values) - 1

    while idx0 <= idxn and values[idx0] <= x <= values[idxn]:

        # Find the mid point
        mid = idx0 + int(((float(idxn - idx0) / (values[idxn] - values[idx0])) * (x - values[idx0])))

        # Compare the value at mid point with search value
        if values[mid] == x:
            return "Found "+str(x)+" at index "+str(mid)

        if values[mid] < x:
            idx0 = mid + 1
    return "Searched element not in the list"


print('Interpolation Search: ', interpolation_search(l, 11))
