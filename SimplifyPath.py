class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        res = []
        for i in range(len(path) - 1, -1 ,-1):
            if path[i] == '': del(path[i])
        for i in path:
            if i == '.': continue
            elif i == '..':
                if len(res) != 0: del(res[-1])
            else: res.append(i)
        return '/' + '/'.join(res)

t = Solution()
print(t.simplifyPath('/.'))