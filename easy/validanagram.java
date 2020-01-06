class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] tmp1 = s.toCharArray();
        Arrays.sort(tmp1);
        char[] tmp2 = t.toCharArray();
        Arrays.sort(tmp2);
        s = new String(tmp1);
        t = new String(tmp2);
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != t.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
