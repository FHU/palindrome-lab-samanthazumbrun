def palindrome(word):
    word = word.lower().replace(" ","")
    if word.isspace():
        return False
    if word == word[::-1]:
        return True
    else:
        return False


