class Solution(object):
    def plusOne(self, digits):
        num = int(''.join(map(str , digits)))
        ans = num + 1
        rev = list(map(int , str(ans) ))
        return rev

digits = [1,2,3]
sol = Solution()
result = sol.plusOne(digits)
print(result)