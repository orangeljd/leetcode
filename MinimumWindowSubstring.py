class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        need, sLen, tLen = collections.Counter(t), len(s), len(t)
        left, right = 0, 0
        begin, end = None, 0
        while right < sLen:
            tLen -= need[s[right]] > 0
            need[s[right]] -= 1
            while tLen == 0:
                if begin is None or right - left < end - begin: begin, end = left, right
                need[s[left]] += 1
                if need[s[left]] > 0: tLen += 1
                left += 1
            right += 1
        return begin is not None and s[begin: end + 1] or ""

t = Solution()
print(t.minWindow("a", "aa"))