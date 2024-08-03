class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        else:
            return 1 + (num - 1)% 9

num = 3652
sol = Solution()
result = sol.addDigits(num)
print(result)