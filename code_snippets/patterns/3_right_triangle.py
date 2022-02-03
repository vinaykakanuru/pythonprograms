""" Simple example of printing * in Right triangle pattern for given size """

## inputs
n = 5


def right_triangle(n):
    """
    Definition: Right sided triangle is nothing but a combination of 
                Decreasing triangle and Increasing triangle

    Outer loop runs for n times for n rows
    we have two inner loops to handle decreasing triangle with " " and increasing triangle with "*"
    """
    for i in range(n):
        # decreasing triange for empty spaces
        for _ in range(i, n):
            print(" ", end=" ")

        # increasing triangle of "*"
        for _ in range(i+1):
            print("*", end=" ")

        print()

right_triangle(n)

# output
#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
