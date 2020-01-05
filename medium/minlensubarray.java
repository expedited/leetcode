class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        // have a window, expand right bound if we're under the minimum
        // advance the left bound, shrink window if we are greater than or equal to the target
        int start = 0;
        int end = 0;
        int currMin = nums.length + 1;
        while (end <= nums.length) {
            int currSum = 0;
            for (int i = start; i < end; i++) {
                currSum += nums[i];
            }
            if (currSum < s) {
                end += 1;
            } else {
                if (end - start < currMin) {
                    currMin = end - start;
                }
                start += 1;
            }
        }
        if (currMin == nums.length + 1) {
            return 0;
        } else {
            return currMin;
        }
    }
}
