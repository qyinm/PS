class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(" ")[::-1]
        print(s)
        for ss in s:
            if len(ss) == 0:
                continue
            return len(ss)