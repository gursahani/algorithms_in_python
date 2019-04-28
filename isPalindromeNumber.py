def isPalindrome(x):
       while x>1:
            
            remainder = x%10
            print("remainder is ",remainder)
            x = x//10
            print("x is ",x)
            new_remainder = x%10
            print("new_remainder is ",new_remainder)
            new_x = x//10
            print("new_x is ",new_x)
            if new_x != remainder:
                return False
            
            return True


print(isPalindrome(121))
