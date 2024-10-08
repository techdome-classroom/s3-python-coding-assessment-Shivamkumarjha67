class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        itr = len(s)
        last = roman_map[s[itr-1]]
        count = 0

        for i in range(itr-1):
            if roman_map[s[i]] < roman_map[s[i+1]]:
                count -= roman_map[s[i]]
            else:
                count += roman_map[s[i]]

        count += last
        return count