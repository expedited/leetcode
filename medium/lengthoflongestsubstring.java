class Solution {
    public int lengthOfLongestSubstring(String s) {
        int start = 0;
        int end = 0;
        int currMax = 0;
        String currSubstr = "";
        while (end < s.length()) {
            // Consider the current substring
            end += 1;
            int contains = currSubstr.indexOf(s.charAt(end - 1));
            if (contains == -1) {
                if (end - start > currMax) {
                    currMax = end - start;
                }
            } else {
                start += contains + 1;
            }

            currSubstr = s.substring(start, end);
        }
        return currMax;
    }
}
