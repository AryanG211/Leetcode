class Solution(object):
    def lemonadeChange(self, bills):
        five , ten = 0 , 0
        for i in bills:
            if i == 5:
                five = five + 1
            elif i == 10:
                if five == 0:
                    return 0
                five = five - 1
                ten = ten + 1

            elif i == 20:
                if five > 0 and ten > 0:
                    ten = ten - 1
                    five = five -1
                elif five >= 3:
                    five = five - 3
                else:
                    return 0

        return 1

bills = [5,5,5,10,20]
sol = Solution()
result = sol.lemonadeChange(bills)
print(result)