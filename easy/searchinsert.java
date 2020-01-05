class Solution {
    public int searchInsert(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;
        int mid = 0;
        while (high >= low) {
            mid = Math.floorDiv((high + low), 2);
            int currVal = nums[mid];
            if (currVal == target) {
                return mid;
            } else if (target > currVal) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        if (target > nums[mid]) {
            return mid + 1;
        } else {
            return mid;
        }
    }
