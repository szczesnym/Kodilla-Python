def palindron(text):
    for i in range(0, len(text) // 2 + 1):
        if text[i] == text[len(text) - i - 1]:
            continue
        else:
            return False
    return True
print(palindron('kajak'))
print(palindron('potok'))