""" Simple example of printing * in Inverted Left triangle pattern for given size """

## inputs
n = 5


def inverted_left_triangle(n):
    """
    Definition: Left sided triangle is nothing but a combination of 
                Decreasing triangle and Increasing triangle 

    Outer loop runs for n times for n rows
    we have two inner loops to handle decreasing triangle with "*" and increasing triangle with " "
    """
    for i in range(n):
        # decreasing triange of "*"
        for _ in range(i, n):
            print("*", end=" ")

        # increasing triangle with empty spaces
        for _ in range(i+1):
            print(" ", end=" ")

        print()

inverted_left_triangle(n)

# output
# * * * * *
# * * * *
# * * *
# * *
# *