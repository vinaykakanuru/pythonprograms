""" Search in row-wise and colum-wise 2D sorted array """

## inputs
arr =   [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]]

target = 29


def sorted_arr_2d_bs(arr, target):
    """
    1. Start looking from first row, last column (i=0, j=m-1)
    2. Compare if arr[i][j] == target, then return the position of indexes
    3. If arr[i][j] > target, then we can ignore the current col and move towards prev col by j-=1
    4. If arr[i][j] < target, then we can ignore the current row and move towards next row by i+=1
    5. If there is no target present in the given 2D sorted array we return -1 after completion of while loop.
    """
    rows = len(arr)
    columns = len(arr[0])
    print(f"Rows: {rows}, Columns: {columns}")

    row, col = 0, columns-1
    while(row>=0 and row < rows and col>=0 and col < columns):
        if arr[row][col] == target:
            return row, col
        elif arr[row][col] > target:
            col -= 1
        elif arr[row][col] < target:
            row += 1

    return -1


if __name__ == "__main__":
    print(sorted_arr_2d_bs(arr, target)) # outputs (2, 1)