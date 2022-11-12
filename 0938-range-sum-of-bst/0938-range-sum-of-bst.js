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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
    arr = []
    function dfs(node) {
        if (!node) return;
        dfs(node.left);
        arr.push(node.val);
        dfs(node.right);
    }
    
    dfs(root);
    res = 0;
    for (let a of arr) {
        if (low <= a && a <= high) {
            res += a;
        }
    }
    
    return res;
};