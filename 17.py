class Solution(object):

    map = {
        '2': ['a', 'b', 'c'], 
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'], 
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'], 
        '9': ['w', 'x', 'y', 'z']
    }

    def recurs(self, digits, cur_string):
        ret = []
        if digits == '':
            return cur_string
        else:
            [ret.append(self.recurs( digits[1:len(digits)], cur_string + i)) for i in self.map[digits[0]]]
            return ret 
        

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.recurs(digits, '')



a = Solution()

print(a.letterCombinations('29'))