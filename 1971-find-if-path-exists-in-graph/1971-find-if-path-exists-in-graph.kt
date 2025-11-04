class Solution {
    fun validPath(n: Int, edges: Array<IntArray>, source: Int, destination: Int): Boolean {
        val visited = HashSet<Int>()
        val queue = ArrayDeque<Int>()
        val graph = buildMap<Int, MutableList<Int>> {
            (0 until n).forEach { put(it, mutableListOf()) }
            edges.forEach { (u, v) ->
                getOrPut(u) { mutableListOf() }.add(v)
                getOrPut(v) { mutableListOf() }.add(u)
            }
        }

        queue.addLast(source)
        visited.add(source)

        while (queue.isNotEmpty()) {
            val curr = queue.removeFirst()

            if (curr == destination) {
                return true
            }
            for (nxt in graph[curr]!!) {
                if (nxt in visited) {
                    continue
                }
                visited.add(nxt)
                queue.addLast(nxt)
            }
        }

        return false
    }
}