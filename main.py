#Your code goes here
def palindrome(word):
    pass

#Solution
'''def palindrome(word):
    #result = True
    last_index = -1
    
    for char in word:
        if char == word[last_index]:
            last_index -= 1
        else:
            return False

    return True  

if __name__ == '__main__':
    word = input("Enter a word:")

    word = word.lower()

    word = word.strip()

    word = word.replace(" ","")

    result = palindrome(word)

    if result:
        print("Palindrome")
    else:
        print("Not a Palindrome")'''