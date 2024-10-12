class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (str2.length() == 0) {
            return str1;
        }
        if (str1.length() < str2.length()) {
            return gcdOfStrings(str2, str1);
        }
        int index = 0;
        for (; index < str2.length(); index++) {
            if (str1.charAt(index) != str2.charAt(index)) {
                return "";
            }
        }

        str1 = str1.length() > index ? str1.substring(index) : "";
        
        return gcdOfStrings(str2, str1);
    }
}