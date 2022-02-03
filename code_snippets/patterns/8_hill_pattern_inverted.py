""" Simple example of printing * in Inverted Hill pattern for given size """

## inputs
n = 5


def inverted_hill_pattern(n):
    """
    Definition: Inverted Hill Pattern is nothing but a combination of
                1) Increaing triangle with empty spaces
                2) Decreasing triangle of "*" (right sided)
                3) Decreasing triangle of "*" (left sided)

    Outer loop runs for n times for n rows
    we have three inner loops to handle 
    1) Increaing triangle with " " 
    2) Decreasing triangle with "*" by looping from "i+1 to n" {to drop a column} (right sided)
    3) Decreasing triangle with "*" looping from "i to n" (left sided)

    Edge case:
    We don't have a peak "*" if we follow the definition we need to drop a column for second inner loop
    so we are looping 2nd inner loop from "i+1 to n" 
    whereas 3rd inner loop from "i to n"
    """
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


inverted_hill_pattern(n)

# output without a peak
#   * * * * * * * * * *
#     * * * * * * * *
#       * * * * * *
#         * * * *
#           * *

# Edge case handled output
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *