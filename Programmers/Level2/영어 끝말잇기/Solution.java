import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        
        Map<String, String> store = new HashMap<>();
        
        store.put(words[0], words[0]);
        char [] firstArr = words[0].toCharArray();
        char endChar = firstArr[firstArr.length - 1];
        
        for (int i = 1; i < words.length; i++) {
            
            char[] word = words[i].toCharArray();
            char startChar = word[0];
            Object flag = store.getOrDefault(words[i], null);
            if (flag != null || endChar != startChar) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            }
            endChar = word[word.length - 1];
            store.put(words[i], words[i]);
        }
        
        
        return answer;
    }
}
