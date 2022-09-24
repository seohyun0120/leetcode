class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]* (rowIndex + 1)
        dp = [1] * (rowIndex + 1)
        
        for r in range(1, rowIndex+1):
            for c in range(1, r):
                dp[c] = res[c-1] + res[c]
            
            dp, res = res, dp
        return res