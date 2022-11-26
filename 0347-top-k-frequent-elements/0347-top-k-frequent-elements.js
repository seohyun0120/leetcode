/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let m = new Map();
    for (let v of nums) {
        m.has(v) ? m.set(v, m.get(v) + 1) : m.set(v,1);
    };

    let arr = [];    
    // k: 숫자, v: 횟수
    for (let [k,v] of m) {
        arr.push([k,v]);
    }
    
    // desc sort
    arr.sort((a,b) => b[1]-a[1]);
    
    let ans = [];
    for (let i=0; i<k; i++) {
        ans.push(arr[i][0])
    }
    return ans;    
};