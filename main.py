
def palindrome(user_word):
    if user_word == user_word[::-1]:
        print('True')
    else:
        print('False')


user_word = input().strip().lower()
palindrome(user_word)
