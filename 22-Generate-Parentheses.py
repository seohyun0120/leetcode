class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dp
        # dp[0] = 1 # ()
        # dp[1] = 2 # (()), ()()
        # dp[2] = 5
        #   dp[1]의 값을 ()로 감쌈
        #   dp[1] + dp[0] 이어 붙이기
        # dp[n] = '('+ dp[n-1]+')' + dp[n-i]+dp[i]

        dp = { 1: set(['()']), 2: set(['(())', '()()'])}
        
        for i in range(3, n+1):
            dp[i] = set(['(' + x + ')' for x in dp[i-1]])

            for j in range(1, i):
                dp[i] = dp[i].union([x + y for x in dp[j] for y in dp[i-j]])

        return list(dp[n])
