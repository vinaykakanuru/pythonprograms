""" Simple example of printing * in a square pattern for a given size """

## inputs
n = 5

def print_square(size):
    """ 
    Outer loop is for rows
    Inner loop is for columns
    """
    for _ in range(size):
        for _ in range(size):
            print("*", end=" ")
        print()

print_square(n)
        