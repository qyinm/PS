import kotlin.math.*

fun dp(graph: Array<IntArray>, cache: Array<IntArray>, n: Int, row: Int, col: Int, start: Int): Int {
    if (row == n - 1) {
        if (col == start) {
            return 987654321
        }
        cache[row][col] = graph[row][col]
        return cache[row][col]
    }

    if (cache[row][col] != -1) {
        return cache[row][col]
    }
    cache[row][col] = 987654321
    
    for (i in 0..2) {
        if (i == col) {
            continue
        }
        cache[row][col] = min(dp(graph, cache, n, row + 1, i, start) + graph[row][col], cache[row][col])
    }
    
    return cache[row][col]
}

fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val graph = Array(n) {
        readLine().split(" ").map { it.toInt() }.toIntArray()
    }
    
    var ans = 987654321
    for (i in 0..2) {
        var cache = Array(n) {
            IntArray(n) {-1}
        }
        ans = min(ans, dp(graph, cache, n, 0, i, i))
    }
    println(ans)
    
}
