
"""Program 32: Count words in a sentence."""


def count_words(sentence):
    words = sentence.split()
    return len(words)


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Number of words:", count_words(sentence))
