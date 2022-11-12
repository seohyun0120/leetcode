/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
    res = [];
    function dfs(root, res) {
        if (!root) {
            return
        }
        
        if (root.left === null && root.right === null){
            res.push(root.val);
            return
        }
        dfs(root.left, res)
        dfs(root.right, res)
        
        return
    }
    
    leaf1 = []
    dfs(root1, leaf1)
    leaf2 = []
    dfs(root2, leaf2)

    return leaf1.join(',') === leaf2.join(',')
};