class Solution():
    def countSeniors(self, details):
        count = 0
        for i in details:
            age = int(i[11:13])
            if age > 60:
                count = count + 1

        return count 

details = ["5612624052M0130","5378802576M6424","5447619845F0171","2941701174O9078"]
sol = Solution()
result = sol.countSeniors(details)
print(result)
        