import java.util.*;

class Solution {
    boolean[][] graph;
    boolean[] visited;
    int n;
    Object[] word;
    String end;
    public int solution(String begin, String target, String[] words) {
        end = target;
        n = words.length+1;
        visited = new boolean[n];
        Deque<String> temp = new ArrayDeque<>(Arrays.asList(words));
        temp.addFirst(begin);
        word = temp.toArray();
        initGraph();
        
        
        int answer = dfs(0, 0);
        return answer;
    }
    
    public int dfs(int idx, int cnt) {
        int ret = 987654321;
        visited[idx] = true;
        
        if (word[idx].equals(end)) {
            return cnt;
        }
        for (int i = 0; i < n; i++) {
            if (!visited[i] && graph[idx][i]) {
                ret = Math.min(ret, dfs(i, cnt + 1));
            }
        }
        if (ret == 987654321) {
            return 0;
        }
        return ret;
        
    }
    
    
    public void initGraph() {
        graph = new boolean[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                if (oneDiff((String)word[i], (String)word[j])) {
                    graph[i][j] = true;
                    graph[j][i] = true;
                }
            }
        }
    }
    
    public boolean oneDiff(String a, String b) {
        int idx = 0;
        int diffCnt = 0;
        
        while(idx < a.length()) {
            if (diffCnt > 1)    break;
            if (a.charAt(idx) != b.charAt(idx)) {
                diffCnt++;
            }
            idx++;
        }
        
        if (diffCnt == 1)   return true;
        else    return false;
    }
}
