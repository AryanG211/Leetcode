class Solution:
    def twoSum(self, A, target):
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] == target:
                    return [i, j]
        return []

A = [6, 3, 2, 5, 7, 8]
target = 9
sol = Solution()
result = sol.twoSum(A, target)
print(result)
