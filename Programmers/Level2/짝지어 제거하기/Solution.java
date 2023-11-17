import java.util.*;

class Solution
{
    public int solution(String s)
    {
        int answer = 0;
        char[] arr = s.toCharArray();
        Deque<Character> q = new ArrayDeque<>();

        q.addLast(arr[0]);
        
        for (int i = 1; i < arr.length; i++) {
            if (!q.isEmpty() && arr[i] == q.peekLast()) {
                q.pollLast();
                continue;
            }
            q.addLast(arr[i]);
        }
        if (q.isEmpty()) {
            answer = 1;
        }
        
        return answer;
    }
}
