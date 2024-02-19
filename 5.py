class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s) 

        #assume the longest possible palindrome is odd in length
        longest_palin_len = -1
        longest_palin_bounds = (-1, -1)

        for i in range(n):

            front_pointer = i 
            back_pointer = i
            local_max_len = 0
            local_max_bound = (-1, -1)

            while (front_pointer != -1 and back_pointer != n):
                if s[front_pointer] == s[back_pointer]:
                    local_max_len += 1
                    local_max_bound = (front_pointer, back_pointer)
                    front_pointer -= 1
                    back_pointer += 1
                else: 
                    break

            if local_max_len > longest_palin_len:
                longest_palin_len = local_max_len
                longest_palin_bounds = local_max_bound

        for i in range(1, n):
            front_pointer = i - 1 
            back_pointer = i
            local_max_len = 1
            local_max_bound = (-1, -1)

            while (front_pointer != -1 and back_pointer != n):
                if s[front_pointer] == s[back_pointer]:
                    local_max_len += 1
                    local_max_bound = (front_pointer, back_pointer)
                    front_pointer -= 1
                    back_pointer += 1
                else: 
                    break

            if local_max_len > longest_palin_len:
                longest_palin_len = local_max_len
                longest_palin_bounds = local_max_bound

        return s[longest_palin_bounds[0] : longest_palin_bounds[1] + 1]