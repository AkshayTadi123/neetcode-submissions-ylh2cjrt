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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null & q == null){
            return true;
        }
        boolean result = helper(p, q);
        return result;
    }

    private boolean helper(TreeNode p, TreeNode q){
        if(p == null & q == null){
            return true;
        } else if(p == null || q == null) {
            return false;
        } 
        return  (p.val == q.val) && helper(p.left, q.left) && helper(p.right, q.right);

    }
}
