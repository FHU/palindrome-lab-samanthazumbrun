
def palindrome(user_word):
    word = user_word.strip().lower()
    if word == word[::-1]:
        print('True')
    else:
        print('False')


user_word = input()
palindrome(user_word)
