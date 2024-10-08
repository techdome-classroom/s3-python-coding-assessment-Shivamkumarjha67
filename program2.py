class Solution(object):
    """
    :type s: str
    :rtype: int
    """
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

        n = len(s)
        last = roman_map[s[n-1]]
        total = 0

        for i in range(n-1):
            if roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]

        total += last
        return total



