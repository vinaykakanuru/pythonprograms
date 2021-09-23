a = input('Enter word1: ')
b = input('Enter word2: ')


def anagrams(a, b):
    if sorted(a) == sorted(b):
        return "Given words are anagrams"
    else:
        return "Sorry..! Given words aren't Anagrams"


print(anagrams(a, b))
