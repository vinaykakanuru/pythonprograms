""" Simple example of printing * in Diamond pattern for given size """

## inputs
n = 5


def diamond_pattern(size):
    """
    Definition: Diamnond Pattern is nothing but a pattern below pattern of Hill type

    Edge Case: We don't get an edge points if we print Hill and Inverted Hill patterns as is with the given size
    We need to reduce the Hill size by "1" to get the pointed Edges
    
    1) So we are running Hill_Pattern with "n-1" rows
    2) Inverted Hill pattern with "n" rows
    """

    # hill_pattern 
    for i in range(n-1):
        # decreasing triangle with empty spaces
        for _ in range(i, n):
            print(" ", end=" ")

        # increasing triangle with "*" (right sided) by dropping one column
        # by looping till "i"
        for _ in range(i):
            print("*", end=" ")

        # increasing triangle with "*" (left sided)
        for _ in range(i+1):
            print("*", end=" ")
        print()

    
    # hill_pattern_inverted
    for i in range(n):
        # increasing triangle with empty spaces
        for _ in range(i+1):
            print(" ", end=" ")

        # decreasing triangle with "*" (right sided) by dropping one column
        # by looping from "i+1 to n"
        for _ in range(i+1, n):
            print("*", end=" ")

        # decreasing triangle with "*" (left sided)
        for _ in range(i, n):
            print("*", end=" ")
        print()


diamond_pattern(n)

# output with pointed edges
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *

# Edge case handled output
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *