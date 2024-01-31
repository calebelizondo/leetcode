class Solution(object):

    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        

        hashmap = {}
        

        #initializing each substring to 0
        for i in range(len(s) - minSize + 1):
            hashmap[s[i: i+minSize]] = 0


        #count the substr totals
        for i in range(len(s) - minSize + 1):
            hashmap[s[i : i + minSize]] += 1

        ans = 0
        #for each key value pair ...
        for key, value in hashmap.items():
            if (len(set(key)) <= maxLetters): #if the max letters is respected
                ans = max(ans, value) #set answer to either max or value

        return ans

