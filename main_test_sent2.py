import main

def test_main():
    word = "Eleven animals I slam in a net"
    assert main.palindrome(word)== False