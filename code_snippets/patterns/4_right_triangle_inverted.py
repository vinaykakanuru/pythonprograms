""" Simple example of printing * in Inverted Right triangle pattern for given size """

## inputs
n = 5


def inverted_right_triangle(n):
    """
    Definition: Right sided triangle is nothing but a combination of 
                Decreasing triangle and Increasing triangle 

    Outer loop runs for n times for n rows
    we have two inner loops to handle increasing triangle with " " and decreasing triangle with "*"
    """
    for i in range(n):
        # increasing triangle with empty spaces
        for _ in range(i+1):
            print(" ", end=" ")

        # decreasing triange of "*"
        for _ in range(i, n):
            print("*", end=" ")
        
        print()

inverted_right_triangle(n)

# output
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
