class Solution:
    def maximumWealth(self, accounts):
        m=len(accounts)
        n=len(accounts[0])
        maxWealth=0
        for i in range(m):
            currentWealth=0
            for j in range(n):
                currentWealth+=accounts[i][j]
            if currentWealth>maxWealth:
                maxWealth=currentWealth
        return maxWealth       

              

        