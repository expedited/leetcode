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
    public int minDepth(TreeNode root) {
        return helper(root, 1);
    }

    public int helper(TreeNode curr, int depth) {
        if (curr == null) {
            return 0;
        }
        int leftresult = helper(curr.left, depth + 1);
        int rightresult = helper(curr.right, depth + 1);
        if (leftresult == 0 && rightresult == 0) {
            return depth;
        } else if (leftresult == 0) {
            return rightresult;
        } else if (rightresult == 0) {
            return leftresult;
        } else {
            return leftresult < rightresult ? leftresult : rightresult;
        }
    }
}
