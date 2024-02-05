def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return "not a palindrome"
    return "palindrome"

s = input()
print(is_palindrome(s))
