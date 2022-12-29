/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
var longestCommonSubsequence = function(text1, text2) {
    const n = text1.length;
    const m = text2.length;

    let dp = [...Array(n+1)].map(() => Array(m+1).fill(0));

    for (let i=0; i<n; i++) {
        for (let j=0; j<m; j++) {
            if (text1[i] === text2[j]) {
                dp[i+1][j+1] = dp[i][j] + 1;
            } else {
                dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }

    return dp[n][m];
};
