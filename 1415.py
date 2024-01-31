#This solution did not perform well in runtime, but well in memory
class Solution(object):

    def getHappyString(self, n, k):
        
        #given n and k, we can calculate if len(total solutions) < k
        if (k > 3 ** (n)): 
            return "" # early return
        

        chars = ['a', 'b', 'c']


        