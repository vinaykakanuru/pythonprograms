""" Simple example of printing * in Left triangle pattern for given size """

## inputs
n = 5


def left_triangle(n):
    """
    Definition: Left sided triangle is nothing but 
                an Increasing triangle with "*" and decreasing with " "
                or (A simple Increasing triangle)

    Outer loop runs for n times for n rows
    we have two inner loops to handle decreasing triangle with " " and increasing triangle with "*"
    """
    for i in range(n):
        # increasing triangle of "*"
        for _ in range(i+1):
            print("*", end=" ")

        # decreasing triange for empty spaces
        for _ in range(i, n):
            print(" ", end=" ")

        print()

left_triangle(n)

# output
# *
# * *
# * * *
# * * * *
# * * * * *