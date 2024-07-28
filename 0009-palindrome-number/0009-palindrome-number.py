class Solution:
    def isPalindrome(self , num):
        string = str(num)
        rev_str = string[::-1]

        if string == rev_str:
            return True

        else:
            return False

num = 34 
sol = Solution()
result = sol.isPalindrome(num)
print(result)
        