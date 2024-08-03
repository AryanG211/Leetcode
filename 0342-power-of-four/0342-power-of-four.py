class Solution(object):
    def isPowerOfFour(self, n):
       if n <= 0:
            return False

       while n % 4 == 0:
            n = n // 4

       return n == 1

n = 64
sol = Solution()
result = sol.isPowerOfFour(n)
print(result)
        