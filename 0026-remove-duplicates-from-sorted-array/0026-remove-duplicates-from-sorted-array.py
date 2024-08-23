class Solution():
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1 , len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]

            

        return i + 1

nums = [1,1,2]
sol = Solution()
result = sol.removeDuplicates(nums)
for k in range(result, len(nums)):
    nums[k] = '_'
print(result)
       