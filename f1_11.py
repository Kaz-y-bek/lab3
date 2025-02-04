def pal(word):
    word1 = "".join(reversed(word))
    return word == word1
name = input()
print(pal(name))