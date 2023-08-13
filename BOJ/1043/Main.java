import java.io.*;
import java.util.StringTokenizer;

class Main {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new Stringtokenizer(br.readLine());

    int n = st.nextToken();
    int m = st.nextToken();

    st = new StringTokenizer(br.readLine());
    int kn = st.nextToken();
    if (kn == 0) {
        System.out.println(m);
        return;
    }
    int[] check = new int[n];
    for (int i = 0; i < kn; i++) {
        check[Integer.parseInt(st.nextToken())] = 1;
    }
}