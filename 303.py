class NumArray(object):

    arr = []

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.arr = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        return sum([self.arr[i] for i in range(left, right + 1, 1)])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)