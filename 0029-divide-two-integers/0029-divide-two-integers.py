class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        ans = dividend // divisor

        if (dividend % divisor != 0 and (dividend < 0) != (divisor < 0)):
            ans = ans + 1 
        return max(min(ans, INT_MAX), INT_MIN)

dividend = 10 
divisor = 3
sol = Solution()
result = sol.divide(dividend , divisor)
print(result)
        
