/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    
    public TreeNode invertTree(TreeNode root) {
        if(root == null){
            return null;
        }
        TreeNode newNode = new TreeNode(root.val, null, null);
        helper(root, newNode);
        return newNode;
    }

    public void helper(TreeNode root, TreeNode newNode){
        if (root.right!=null){
            newNode.left = new TreeNode(root.right.val);
            helper(root.right, newNode.left);
        }

        if(root.left!=null){
            newNode.right = new TreeNode(root.left.val);
            helper(root.left, newNode.right);
        }
    }
}
