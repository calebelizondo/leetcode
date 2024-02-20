class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        min_jumps = [n for i in range(n)]
        min_jumps[0] = 0

        for i in range(n): 
            for j in range(i, min(n, i + nums[i] + 1)):
                min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)

        print(min_jumps)

        return min_jumps[n - 1]
