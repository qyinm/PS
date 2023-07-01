import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> map = new HashMap<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        Stream<String> stream = getTokenStream(st);
        stream.forEach(token -> {
            int k = Integer.parseInt(token);
            if (map.containsKey(k)) {
                map.put(k, map.get(k) + 1);
            } else {
                map.put(k, 1);
            }
        });
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        stream = getTokenStream(st);
        String answer = stream.map(token -> Optional.ofNullable(map.get(Integer.parseInt(token)))
                                .orElse(0))
                                .map(Object::toString)
                                .collect(Collectors.joining(" "));
        System.out.println(answer);
    }
    private static Stream<String> getTokenStream(StringTokenizer tokenizer) {
        Iterable<String> iterable = () -> new StringTokenizerIterator(tokenizer);
        return StreamSupport.stream(iterable.spliterator(), false);
    }

    private static class StringTokenizerIterator implements java.util.Iterator<String> {
        private final StringTokenizer tokenizer;

        public StringTokenizerIterator(StringTokenizer tokenizer) {
            this.tokenizer = tokenizer;
        }

        @Override
        public boolean hasNext() {
            return tokenizer.hasMoreTokens();
        }

        @Override
        public String next() {
            return tokenizer.nextToken();
        }
    }
}