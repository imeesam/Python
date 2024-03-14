wd = input("Enter any word to check if it's a palindrome or not: ")
def is_palindrome(word):
    rev_word = word[::1]
    if word == rev_word:
        return "The Word is a palindrome"
    else:
        return "The Word is not a palindrome"

print(is_palindrome(wd))
