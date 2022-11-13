/**
 * @param {number[]} nums
 * @return {number}
 */
var minPairSum = function(nums) {
    nums.sort((a,b) => b-a);
    
    let n = nums.length;
    let ans = 0;
    for (let i = 0; i < n/2; i++) {
        ans = Math.max(ans, nums[i] + nums[n-i-1]);
    }
    
    return ans;
};