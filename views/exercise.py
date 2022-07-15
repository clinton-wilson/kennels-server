from posixpath import split


def no_vowels(string):
    """this is a docstring"""
    split_list = []
    split_list.append(split(string))
    for char in split_list:
        if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u":
            split_list.pop(char)
    print("".join(split_list))


no_vowels("Please god let this work")

print("Hello")
