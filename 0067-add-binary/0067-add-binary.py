class Solution(object):
    def addBinary(self, a, b):
       a = int(a , 2)
       b = int(b , 2)
       while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1

       return bin(a)[2:]

a = "11"
b = "1"
sol = Solution()
result = sol.addBinary(a , b)
print(result)
        