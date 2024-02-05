class Solution(object):

    def getHappyString(self, n, k):

        chars = ['a', 'b', 'c']

        current_string = [chars[0] for i in n]
        lexical_strings = []
        
        #generate lexical strings 
        #for each index
        for i in n:
            for  c in chars:
                gen_strings = []

        