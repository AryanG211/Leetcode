class Solution(object):
    def reverse(self, x):
        string = str(x)
        if string[0] == "-":
            new_str = "-" + string[:0:-1]   

        else:
            new_str = string[::-1]
        reverse_str = int(new_str)

        if reverse_str < -2**31 or reverse_str > 2**31 - 1:
            return 0

        return reverse_str
    

x = 342
sol = Solution()
result = sol.reverse(x)
print(result)      