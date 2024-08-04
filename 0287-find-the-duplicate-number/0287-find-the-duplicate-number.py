class Solution(object):
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

nums = [3,1,3,4,2]
sol = Solution()
result = sol.findDuplicate(nums)
print(result)
        