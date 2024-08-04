class Solution(object):
    def findDuplicates(self, nums):
        seen = set()
        duplicate = set()
        for num in nums:
            if num in seen:
                duplicate.add(num)
            seen.add(num)
        return list(duplicate)

nums = [3, 1, 3, 4, 2]
sol = Solution()
result = sol.findDuplicates(nums) 
print(result)  

        
        