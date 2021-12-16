class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # approach: greedy algorithm
        # idea: search for the index that lands you in the leftmost index
        # if leftmost index == 0, then we can reach the end inde
        starting_index = len(nums) - 1
        for i in reversed(range(len(nums))):

            # if the current index + max number of steps surpasses our current
            # position,
            # choose it
            if(i + nums[i] >= starting_index):  # choose the index that goes the furthest
                starting_index = i

        # Time Complexity: O(N)
        # Space Complexity: O(1)
        return starting_index == 0  # meaning we can reach the index from the beginning
