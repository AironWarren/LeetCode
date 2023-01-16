class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # n = 0
        # s1 = 0
        # s2 = 0
        # str = ['(', ')', '{', '}', '[', ']']
        #
        # for i in s:
        #     if s.index(i, n) % 2 != 0:
        #         s2 = i
        #         n += 1
        #         if (s1 == str[0] and s2 == str[1]) or (s1 == str[2] and s2 == str[3])
        #         or (s1 == str[4] and s2 == str[5]):
        #              m = 1
        #         else:
        #             return False
        #     else:
        #         s1 = i
        # return True


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = 0
        m = 0

        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')

        return False if len(s) != 0 else True

s = "(){]"

print(Solution().isValid(s))
