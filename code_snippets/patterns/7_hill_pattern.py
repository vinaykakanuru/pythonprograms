""" Simple example of printing * in Hill pattern for given size """

## inputs
n = 5


def hill_pattern(n):
    """
    Definition: Hill Pattern is nothing but a combination of
                1) Decreasing triangle with empty spaces
                2) Increasing triangle of "*" (right sided)
                3) Increasing triangle of "*" (left sided)

    Outer loop runs for n times for n rows
    we have three inner loops to handle 
    1) Decreasing triangle with " " 
    2) Increasing triangle with "*" by looping till "i" {to drop a column} (right sided)
    3) Increasing triangle with "*" looping till "i+1" (left sided)

    Edge case:
    We don't have a peak "*" if we follow the definition we need to drop a column for second inner loop
    so we are looping 2nd inner loop till "i" 
    whereas 3rd inner loop continues till "i+1"
    """
    for i in range(n):
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


hill_pattern(n)

# output without a peak
#           * *
#         * * * *
#       * * * * * *
#     * * * * * * * *
#   * * * * * * * * * *

# Edge case handled output
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *