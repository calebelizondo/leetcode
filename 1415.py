class Solution(object):

    def genLexString(self, n, cur_str):

        chars = ['a', 'b', 'c']
        if (n == 0):
            return [cur_str]
        else:
            concat_strings = []
            for i in chars: 
                if (cur_str == "" or i != cur_str[len(cur_str) - 1]):
                    concat_strings += Solution.genLexString(self, n - 1, cur_str + i)

            return concat_strings

    def getHappyString(self, n, k):
        #generate lexical strings 
        lex_string = Solution.genLexString(self, n, "")

        #get the k index
        if (len(lex_string) < k):
            return ""
        else: 
            return lex_string[k  - 1]
