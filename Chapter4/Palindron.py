def palindron(text):
    """

    :param text: Text to check if it's palindrome
    :return: True if the text IS palindrome, False in other cases
    """
    for i in range(0, len(text) // 2 + 1):
        if text[i] == text[len(text) - i - 1]:
            continue
        else:
            return False
    return True
print(palindron('kajak'))
print(palindron('potok'))