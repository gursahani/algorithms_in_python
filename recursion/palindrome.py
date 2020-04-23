def isPalindrome(s):
    # if len(word) == 1:
    #     return True
    # elif word[0] != word[len(word) - 1]:
    #     return False
    # mid = word[1:-1]
    # # print(mid)
    # return isPalindrome(mid)
    str1 = ""
    for i in range(len(s)):
        if s[i].isalnum():
            str1 += s[i].lower()

    if len(str1) == 1:
        return True
    elif str1[0] != str1[len(str1) - 1]:
        return False
    mid = str1[1:-1]
    return isPalindrome(mid)


print(isPalindrome("A man, a plan, a canal: Panama"))
