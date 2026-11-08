
"""Program 33: Find the first non-repeating character."""


def first_non_repeating_char(text):
    for char in text:
        if text.count(char) == 1:
            return char

    return ""


if __name__ == "__main__":
    text = input("Enter a string: ")
    result = first_non_repeating_char(text)

    if result:
        print("First non-repeating character:", result)
    else:
        print("No non-repeating character found.")
