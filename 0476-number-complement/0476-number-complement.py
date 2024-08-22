class Solution(object):
    def findComplement(self, num):
        binary = bin(num)[2:]
        replace = binary.replace("0" , "3")
        replace = replace.replace("1" , "0")
        replace = replace.replace("3" , "1")

        number = int(replace , 2)
        return number 

num = 3 
sol = Solution()
result = sol.findComplement(num)
print(result)
        