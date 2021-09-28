""" If given sentence contains all english alphabets then we can say it is pangram """

from string import ascii_lowercase

sentence = "We promptly judged antique ivory buckles for the next prize"


def pangrams(sentence):
    alphabets = [c for c in ascii_lowercase]
    b = sorted(set([i for i in sentence.lower() if i != ' ']))
    return True if alphabets == b else False


print(pangrams(sentence))


# Another approach
def pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabets:
        if char not in sentence.lower():
            return False
    return True
