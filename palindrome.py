def palindrome(my_str):
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
        print("Palindrome")
    else:
        print("Not palindrome")

palindrome("aibohphobia")