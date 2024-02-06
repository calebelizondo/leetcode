class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        

        front_pointer = 0
        back_pointer = len(height) - 1

        current_front = front_pointer
        current_back = back_pointer
        current_area = min(height[front_pointer], height[back_pointer]) * (back_pointer - front_pointer)

        while front_pointer < back_pointer: 

            print(f'Front pointer: {front_pointer} back pointer: {back_pointer}')
            print(f"current front: {current_front} back {current_back}")

            move_front_area = min(height[front_pointer], height[current_back]) * (current_back - front_pointer)
            move_back_area = min(height[current_front], height[back_pointer]) * (back_pointer - current_front)
            move_both = min(height[front_pointer], height[back_pointer]) * (back_pointer - front_pointer)
            
            if move_both > current_area and move_both > move_front_area and move_both > move_back_area:
                current_front = front_pointer
                current_back = back_pointer
                current_area = move_both

            elif move_front_area > current_area and  move_front_area > move_back_area:
                current_area = move_front_area
                current_front = front_pointer


            elif move_back_area > current_area:
                current_area = move_back_area
                current_back = back_pointer


            if (height[front_pointer] > height[back_pointer]):
                back_pointer -= 1
            else:
                front_pointer += 1
                

        return current_area


a = Solution()
print(a.maxArea([1,8,100,2,100,4,8,3,7]))

            
