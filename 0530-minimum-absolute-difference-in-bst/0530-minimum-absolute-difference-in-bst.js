/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var getMinimumDifference = function(root) {
    res = []
    function dfs(root) {
        if (!root) {
            return
        }
        dfs(root.left)
        res.push(root.val);
        dfs(root.right)
        return
    }
    
    dfs(root)
    res.sort(function(a, b){return a-b});
    let ans = res[1] - res[0];

    for (let i = 1; i < res.length-1; i++) {
        ans = Math.min(ans, res[i+1] - res[i]);
    }
    
    return ans
};