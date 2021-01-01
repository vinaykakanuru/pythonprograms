l = [64, 34, 25, 12, 22, 11, 90]

# takes list as input and keeps large number at last pos for each comparison


def bubble_sort(list):
    for i in range(len(l)-1, 0, -1):  # keep large number at last
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


print('Bubble Sort: ', bubble_sort(l))
