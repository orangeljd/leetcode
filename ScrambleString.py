class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        import collections
        if s1 == s2: return True
        count = collections.Counter(s1)
        for c in s2:
            count[c] -= 1
            if count[c] < 0: return False
        for i in range(len(s1) - 1):
            if self.isScramble(s1[0: i + 1], s2[0: i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:]): return True
            if self.isScramble(s1[0: i + 1], s2[len(s1) - i - 1:]) and self.isScramble(s1[i + 1:], s2[0: len(s1) - i - 1]): return True
        return False

t = Solution()
print(t.isScramble('abcd', 'bdac'))