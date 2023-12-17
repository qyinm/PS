import kotlin.math.*

lateinit var graph: Array<IntArray>
lateinit var cache: Array<IntArray>
var n = 0

fun dp(row: Int, col: Int, start: Int): Int {
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
        cache[row][col] = min(dp(row + 1, i, start) + graph[row][col], cache[row][col])
    }
    
    return cache[row][col]
}

fun main() = with(System.`in`.bufferedReader()) {
    n = readLine().toInt()
    graph = Array(n) {
        readLine().split(" ").map { it.toInt() }.toIntArray()
    }
    
    var ans = 987654321
    for (i in 0..2) {
        cache = Array(n) {
            IntArray(n) {-1}
        }
        ans = min(ans, dp(0, i, i))
    }
    println(ans)
    
}
