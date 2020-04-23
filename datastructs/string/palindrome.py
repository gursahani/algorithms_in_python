def is_palindrome(s):
    return all(s[i] == s[~i] for i in range(len(s)))


print(is_palindrome("madaM"))
