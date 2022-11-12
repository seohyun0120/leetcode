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
 * @return {TreeNode}
 */
var increasingBST = function(root) {
    const nodeValue = [];
    function dfs(node) {
        if (!node) return;
        dfs(node.left);
        nodeValue.push(node.val);
        dfs(node.right);
    }
    
    dfs(root);
    
    const treeNode = new TreeNode(0);
    let curNode = treeNode;
    
    for (let x of nodeValue) {
        curNode.right = new TreeNode(x, null, null);
        curNode = curNode.right;
    }
    
    return treeNode.right;
};