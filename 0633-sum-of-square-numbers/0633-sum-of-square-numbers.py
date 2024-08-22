class Solution(object):
    def judgeSquareSum(self, c):
      b = 0
      while b * b <= c:
        b = b + 1

      b = b - 1
      a = 0
      while a <= b:
        sum = a * a + b * b
        if sum == c:
            return True

        elif sum > c:
            b = b - 1

        else:
            a = a + 1

      return False

c = 5
sol = Solution()
result = sol.judgeSquareSum(c)
print(result)
