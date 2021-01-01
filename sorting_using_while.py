l = [64, 34, 25, 12, 22, 11, 90]

# iterating over given list and popping up the min element and storing in result varibale


def sort_using_while(list):
    res = []
    while l:
        res.append(l.pop(l.index(min(l))))
    return res


print('Sorting without built-in or existing algorithms: ', sort_using_while(l))
