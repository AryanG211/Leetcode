class Solution():
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
    
nums = [1 ,1 ,2 ,3 , 4 ,5 ,4 ,6]
val = 4
sol = Solution()
result = sol.removeElement(nums , val)
print(result)
print(nums)

