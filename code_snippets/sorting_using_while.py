""" iterating over given list and popping up the min element and storing in result varibale """

arr = [64, 34, 25, 12, 22, 11, 90]

def sort_using_while(arr):
    """ returns sorted array from the given input array """
    res = []
    while arr:
        res.append(arr.pop(arr.index(min(arr))))
    return res


print('Sorting without built-in or existing algorithms: ', sort_using_while(arr))
