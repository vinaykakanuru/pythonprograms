# We consider the given string is beautifu if it shouldn't consists "010" in it
# to make the given string of integers beautiful how many "minimial" conversions needed either 0-1 or 1-0 to avoid
# that there will be no "010" is present in the given string

# input
s = "0100101010"

# output should be 3 because "010" present 3 times.
# And we need 3 minimal conversions to eliminate "010" in the given string


def beautiful_string(s):
    # method 1
    # return s.count("010")

    # method 2
    return (len(s) - len(s.replace("010", ""))) // 3


print(beautiful_string(s))
