/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        return helper(t1, t2);
    }

    public TreeNode helper(TreeNode curr1, TreeNode curr2) {
        int sum = 0;
        if (curr1 == null && curr2 == null) {
            return null;
        } else if (curr1 == null) {
            sum = curr2.val;
        } else if (curr2 == null) {
            sum = curr1.val;
        } else {
            sum = curr1.val + curr2.val;
        }
        TreeNode currResult = new TreeNode(sum);
        currResult.left = helper(curr1 == null ? null : curr1.left, curr2 == null ? null : curr2.left);
        currResult.right = helper(curr1 == null ? null : curr1.right, curr2 == null ? null : curr2.right);
        return currResult;
    }
}
