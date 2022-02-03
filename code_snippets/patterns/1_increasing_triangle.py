""" Simple example of printing * in increasing triangle pattern for given size """

## inputs
n = 5

def increasing_triangle(size):
    """
    Outer loop runs for n times for n rows
    inner loop runs for i times for n columns
    """
    for i in range(size):
        for _ in range(i+1):
            print("*", end=" ")
        print()

increasing_triangle(n)

# output
# *
# * *
# * * *
# * * * *
# * * * * *