class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """


        current_str = ""
        i = 0
        while len(current_str) < len(s) and len(words) > i:
            current_str += words[i]
            i += 1

        return s == current_str
