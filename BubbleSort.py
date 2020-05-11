l = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sorted(l)

# takes sorted list as input and keeps large number at last pos for each comparison

def BinarySort(list):
    for i in range(len(l)-1, 0, -1): # keep large number at last
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(BinarySort(sorted_list))