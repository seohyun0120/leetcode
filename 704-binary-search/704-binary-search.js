/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let start = 0;
    let end = nums.length;
    
    while (start <= end) {
        let mid = parseInt((start + end)/2);
        let midValue = nums[mid];
        
        if (midValue === target) {
            return mid;
        } else if (midValue > target) {
            end = mid -1;
        } else {
            start = mid + 1;
        }
    }
    return -1;
};