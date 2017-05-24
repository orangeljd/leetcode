class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sLen = len(s)
        res = []
        def restore(start, end, count, tmp):
            if start >= sLen: return
            if count == 4:
                if end + 1 == sLen and ((s[start] != '0' and 0 < int(s[start: end + 1]) <= 255) or (s[start] == '0' and start == end)):
                    tmp.append(s[start: end + 1])
                    res.append('.'.join(tmp))
                    tmp.pop()
                return
            for i in range(start, end + 1):
                if (s[start] != '0' and 0 <= int(s[start: i + 1]) <= 255) or (s[start] == '0' and start == i):
                    tmp.append(s[start: i + 1])
                    if i + 3 < sLen: restore(i + 1, i + 3, count + 1, tmp)
                    else: restore(i + 1, sLen - 1, count + 1, tmp)
                    tmp.pop()
        if sLen < 4: return res
        restore(0, 2, 1, [])
        return res

t = Solution()
print(t.restoreIpAddresses('010010'))