class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> results = new HashMap<>();
        for (String curr : strs) {
            // sort the current string
            char tempArray[] = curr.toCharArray();
            Arrays.sort(tempArray);
            String sortedCurr = new String(tempArray);

            if (results.containsKey(sortedCurr)) {
                List<String> currList = results.get(sortedCurr);
                currList.add(curr);
                results.put(sortedCurr, currList);
            } else {
                List<String> newList = new ArrayList<String>();
                newList.add(curr);
                results.put(sortedCurr, newList);
            }
        }
        return new ArrayList<>(results.values());
    }
}
