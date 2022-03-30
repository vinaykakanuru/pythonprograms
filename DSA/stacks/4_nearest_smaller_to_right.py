""" Find the Nearest Smaller Element to the RIGHT of each element from the given array """

## inputs
arr_1 = [1, 3, 2, 4]
arr_2 = [1, 3, 0, 0, 1, 2, 4]
arr_3 = [4, 5, 2, 10, 8]

def nsr(arr):
    res, s = [], []
    for i in range(len(arr)-1, -1, -1):
        if (len(s) == 0):
            res.append(-1)
        elif len(s) > 0 and s[-1] < arr[i]:
            res.append(s[-1])
        elif len(s) > 0 and s[-1] >= arr[i]:
            while len(s)>0 and s[-1] >= arr[i]:
                s.pop()
            if len(s) == 0:
                res.append(-1)
            else:
                res.append(s[-1])
        s.append(arr[i])

    return res[::-1] # reversing the res array

if __name__ == "__main__":
    print(nsr(arr_1)) ## outputs [-1, 1, 1, 2]
    print(nsr(arr_2)) ## outputs [-1, 1, -1, -1, 0, 1, 2]
    print(nsr(arr_3)) ## outputs [-1, 4, -1, 2, 2]