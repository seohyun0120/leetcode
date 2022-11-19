/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    const m = accounts.length;
    const n = accounts[0].length;
    
    let max = 0;
    for (let i=0; i<m; i++) {
        max = Math.max(max, getSum(accounts[i]));
    }
    
    return max;
};

var getSum = function(arr) {
    let res = 0;
    
    for (let i=0; i<arr.length; i++) {
        res += arr[i];
    }
    return res;
}