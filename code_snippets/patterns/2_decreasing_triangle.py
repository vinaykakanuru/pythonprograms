""" Simple example of printing * in decreasing triangle pattern for given size """

## inputs
n = 5


def decreasing_triangle(n):
    """
    Outer loop runs for n times for n rows
    inner loop runs from i to n times for n columns
    """
    for i in range(n):
        for _ in range(i, n):
            print("*", end=" ")
        print()

decreasing_triangle(n)

# output
# * * * * *
# * * * *
# * * *
# * *
# *