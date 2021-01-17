l = [64, 34, 25, 12, 22, 11, 90]

# iterating over given list and popping up the min element and storing in result varibale


def sort_using_while(given_list):
    res = []
    while given_list:
        res.append(given_list.pop(given_list.index(min(given_list))))
    return res


print('Sorting without built-in or existing algorithms: ', sort_using_while(l))
