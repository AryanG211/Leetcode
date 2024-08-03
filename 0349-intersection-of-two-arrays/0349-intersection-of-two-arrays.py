class Solution(object):
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        intersection = s1.intersection(s2)

        return list(intersection)

nums1 = [1 , 3 , 4 , 6 , 3 , 9]
nums2 = [3 , 8 , 9 , 0 , 1, 5]

sol = Solution()
result = sol.intersection(nums1 , nums2)
print(result)