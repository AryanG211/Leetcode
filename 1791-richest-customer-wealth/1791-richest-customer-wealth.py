class Solution():
    def maximumWealth(self, accounts):
        max_wealth = 0  
        for client in accounts:
            wealth = sum(client)
            if(wealth > max_wealth):
                max_wealth = wealth

        return max_wealth


accounts = [[1,3,4] , [3,5,1] , [5,9,1]]
sol = Solution()
result = sol.maximumWealth(accounts)
print(result)


        