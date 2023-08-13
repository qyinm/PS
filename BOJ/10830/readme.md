#[[골드 4] 행렬 제곱](https://www.acmicpc.net/problem/10830)

해당 문제는 분할 정복으로 하면 풀린다. 

n이 짝수일 때,
A^n = A^(n / 2) * A^(n / 2)

n이 홀수일 때,
A^n = A^(n / 2 + 1) * A^(n / 2)

분할 정복 하면 된다. 최적화를 위해 map 자료 구조를 사용해서 cache변수를 생성해서 dynamic programming하게 만들었다.

[[실버 3] A](https://www.acmicpc.net/problem/13171) 문제는 예전에 시간복잡도 때문에 못 풀었는 데 지금 풀이법 같이 코딩하면 풀릴 것 같다.