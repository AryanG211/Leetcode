class Solution():
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result ^=i
        return result

    
nums = [1,3,2,3,1]
sol = Solution()
result = sol.singleNumber(nums)
print(result) 