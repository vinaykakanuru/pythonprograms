""" Find maximum element from Bitonic array """

from _17_peak_element_BS import peak_element
## inputs
arr = [1, 3, 8, 12, 4, 2]

def bitonic_arr_bs(arr):
    """ Apply peak element to find the max from given Bitonic array """
    return peak_element(arr)

if __name__ == "__main__":
    print(bitonic_arr_bs(arr)) # outputs (3)

