class Solution {
    public String reverseVowels(String s) {
        Set<Character> vo = new HashSet<>();
        vo.add('a');
        vo.add('e');
        vo.add('i');
        vo.add('o');
        vo.add('u');
        vo.add('A');
        vo.add('E');
        vo.add('I');
        vo.add('O');
        vo.add('U');
        StringBuilder sb = new StringBuilder();
        List<Integer> idxList = new ArrayList<>();
        for (int idx = 0; idx < s.length(); idx++) {
            if (vo.contains(s.charAt(idx))) {
                idxList.add(idx);
            }
        }

        int vowelIdx = idxList.size()-1;
        for (int idx = 0; idx < s.length(); idx++) {
            if (vo.contains(s.charAt(idx))) {
                sb.append(s.charAt(idxList.get(vowelIdx)));
                vowelIdx--;
            } else {
                sb.append(s.charAt(idx));
            }
        }
        return sb.toString();
    }
}