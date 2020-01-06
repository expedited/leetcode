class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> mappings = new HashMap<>();
        mappings.put('(', ')');
        mappings.put('{', '}');
        mappings.put('[', ']');
        String starts = "({[";
        ArrayList<Character> stack = new ArrayList<>();
        for (Character currChar : s.toCharArray()) {
            if (starts.indexOf(currChar) != -1) {
                stack.add(mappings.get(currChar));
            } else {
                if (stack.size() == 0 || stack.remove(stack.size() - 1) != currChar) {
                    return false;
                }
            }
        }
        if (!stack.isEmpty()) {
            return false;
        } else {
            return true;
        }
    }
}
