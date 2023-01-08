class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = 0
        answer = 0

        d = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

        for i in s:
            if (i == 'V' and x == 1) or (i == 'X' and x == 1):
                x = d[i] - 2
            elif (i == 'L' and x == 10) or (i == 'C' and x == 10):
                x = d[i] - 20
            elif (i == 'D' and x == 100) or (i == 'M' and x == 100):
                x = d[i] - 200
            else:
                x = d[i]
            answer += x

        return answer


print(Solution().romanToInt("LVIII"))
