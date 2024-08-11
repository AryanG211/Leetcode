class Solution(object):
    def thirdMax(self, nums):
        new = set(nums)
        sorted_new = sorted(new , reverse = True)
        
        if len(sorted_new) >= 3:
            return sorted_new[2]



        else:
            return sorted_new[0]

        
nums = [3 , 4, 5]
sol = Solution()
result = sol.thirdMax(nums)
print(result)



