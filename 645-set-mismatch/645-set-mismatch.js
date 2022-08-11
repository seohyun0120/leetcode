/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    const set = new Set(nums);
    let n = nums.length;
    let sum = 0;
    set.forEach((s) => sum += s);
    
    let real = 0;
    nums.forEach((s) => real += s);
    
    let totalSum = n * (n+1) / 2;
    
    return [real - sum, totalSum - sum]
};