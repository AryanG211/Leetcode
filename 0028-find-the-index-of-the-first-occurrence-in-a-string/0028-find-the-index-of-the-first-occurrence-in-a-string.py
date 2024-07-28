class Solution:
    def strStr(self, haystack, needle ) :
        return haystack.find(needle)

haystack = "Airplane"
needle = "Air"
sol = Solution()
result = sol.strStr(haystack, needle)
print(result)  

        