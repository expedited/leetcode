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
    public boolean isValidBST(TreeNode root) {
        // Given a certain node, you can have up to two constraints, a lower and upper bound
        // The upper bound is defined by the
        // You have to make recursive calls at each node, and then set the appropriate bounds for the children, if any of them don't obey the BST property then short circuit
        // recursive call, left child has to be less than min(low, keyval), right child has to be greater than max(high, keyval)
        if (root == null) {
            return true;
        }
        return helper(root, Integer.MIN_VALUE, Integer.MAX_VALUE, false, false);
    }

    public boolean helper(TreeNode curr, int low, int high, boolean leftInit, boolean rightInit) {
        if (curr == null) {
            return true;
        }
        if (curr.val <= low && leftInit == true) {
            return false;
        }

        if (curr.val >= high && rightInit == true) {
            return false;
        }

        return helper(curr.left, low, high < curr.val ? high : curr.val, leftInit, true) && helper(curr.right, low > curr.val ? low : curr.val, high, true, rightInit);
    }
}
