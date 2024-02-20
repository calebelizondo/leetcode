class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        current_jump_len = nums[0]

        if current_jump_len <= 0 and n != 1: #if first jump len is 0, we fail unless it is also the last index
            return False

        for i in range(1, n - 1):
            current_jump_len = max(current_jump_len - 1, nums[i])
            if current_jump_len <= 0: 
                return False

        return True        