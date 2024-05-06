# Module 8 Lab - Palindrome Tester
# Zane Reif
# 12 April 2024
# Tests words for palindromes

string = input('Enter a word or phrase: ')

def is_palindrome(string):
    string = string.lower()
    stack = []
    for character in string:
        if 'a' <= character <= 'z':
            stack.append(character)
    
    for character in string:
        if 'a' <= character <= 'z':
            if character != stack.pop():
                return False
    
    return True

print(is_palindrome(string))
