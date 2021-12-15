class Solution:
    def rob(self, nums: List[int]) -> int:

        # trivial cases
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

       # m = [nums[0] , max(nums[0], nums[1]) ] #initial solutions
       # using m[] implied O(n) memory

        max_robbed = 0
        # using these two variables reduces space complexity to O(1)
        previous = max(nums[0], nums[1])
        previous_two = nums[0]  # index - 2

        for house in range(2, len(nums)):

            #m.append(max(nums[house] + m[house-2] ,  m[house-1] ))
            max_robbed = max(nums[house] + previous_two, previous)
            previous_two = previous
            previous = max_robbed

        # Time Complexity: 0(n)
        # Space Complexity: O(1)
        return max_robbed
