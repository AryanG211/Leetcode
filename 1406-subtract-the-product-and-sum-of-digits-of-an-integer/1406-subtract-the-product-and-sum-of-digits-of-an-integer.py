class Solution():
    def subtractProductAndSum(self, n):
        product = 1
        sum = 0
        for num in str(n):
            num = int(num)
            product = product * num
            sum = sum + num
        return product - sum
        
n = 325
sol = Solution()
result = sol.subtractProductAndSum(n)
print(result)