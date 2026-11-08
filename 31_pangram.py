
"""Program 31: Check whether a sentence is a pangram."""


def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    sentence = sentence.lower()

    for letter in alphabet:
        if letter not in sentence:
            return False

    return True


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    if is_pangram(sentence):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")
