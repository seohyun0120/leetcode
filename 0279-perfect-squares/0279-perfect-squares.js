/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    if (n < 4) return n;

    const dp = [0];

    // dp[12] = 최솟값 (dp[12], dp[11]+1(1^2), dp[8]+1(2^2), dp[3]+1(3^3))
    for (let i=1; i<=n; i++) {
        dp[i] = Number.MAX_VALUE;
        for (let j=1; j*j <= i; j++) {
            dp[i] = Math.min(dp[i], dp[i-j*j] + 1);
        }
    }
    return dp[n];
};