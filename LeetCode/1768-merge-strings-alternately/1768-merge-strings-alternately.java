class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int maxLength = Math.max(word1.length(), word2.length());

        int index = 0;
        for (; index < maxLength; index++) {
            if (index < word1.length()) {
                sb.append(word1.charAt(index));
            }
            if (index < word2.length()) {
                sb.append(word2.charAt(index));
            }
        }


        return sb.toString();
    }
}