""" Find the Nearest Greater Element to the LEFT of each element from the given array """

## inputs
arr_1 = [1, 3, 2, 4]
arr_2 = [1, 3, 0, 0, 1, 2, 4]

def ngl(arr):
    res, s = [], []
    for i in range(0,len(arr)):
        if (len(s) == 0):
            res.append(-1)
        elif len(s) > 0 and s[-1] > arr[i]:
            res.append(s[-1])
        elif len(s) > 0 and s[-1] <= arr[i]:
            while len(s)>0 and s[-1] <= arr[i]:
                s.pop()
            if len(s) == 0:
                res.append(-1)
            else:
                res.append(s[-1])
        s.append(arr[i])

    return res # no reversing the res array

if __name__ == "__main__":
    print(ngl(arr_1)) ## outputs [-1, -1, 3, -1]
    print(ngl(arr_2)) ## outputs [-1, -1, 3, 3, 3, 3, -1]