import java.util.*;

class Solution {
    public int solution(int[][] targets) {
        Deque<int[]> st = new ArrayDeque<>();
        Arrays.sort(targets, (o1, o2) -> {
            if(o1[0] == o2[0]) {
                return Integer.compare(o1[1],o2[1]);
            }
            else {
                return Integer.compare(o1[0],o2[0]);
            }
        });
        
        st.add(targets[0]);
        
        int[] peek = st.peek();
        int n = targets.length;
        for (int i = 1; i < n; i++) {
            if (targets[i][0] < st.peekLast()[1]) {
                st.peekLast()[0] = Math.min(st.peekLast()[0], targets[i][0]);
                st.peekLast()[1] = Math.min(st.peekLast()[1], targets[i][1]);
            } else {
                st.add(targets[i]);
            }
        }
        List<int[]> test = new ArrayList<>(st);
        test.stream().forEach(el -> System.out.println(el[0] + " " + el[1]));
        int answer = st.size();
        return answer;
    }
}
