def Reverse(s):
    words = s.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

s = input()
print(Reverse(s))
