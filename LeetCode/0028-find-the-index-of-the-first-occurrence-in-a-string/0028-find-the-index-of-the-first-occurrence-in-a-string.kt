class Solution {
    fun strStr(haystack: String, needle: String): Int {
        val needleLength = needle.length

        for (i in 0 .. haystack.length - needleLength) {
            if (needle == haystack.slice(i until i+needleLength)) {
                return i
            }
        }

        return -1
    }
}