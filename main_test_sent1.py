import main

def test_main():
    word = "Ten animals I slam in a net"
    assert main.palindrome(word)== True