class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}  # use it

        def recursive_decode(s, index):
            # remember, usually recursive methods have indexes
            # base cases

            if index in memo:
                return memo[index]

            # order of base cases matters!

            if index == len(s):
                return 1

            if s[index] == '0':
                return 0  # no mapping for 0

            if index == len(s) - 1:
                return 1

            # here is where the tree diverges
            # We only count a solution if it reaches the end of a string!

            # decoding 1 char at a time
            decodings = recursive_decode(s, index+1)

            # check if  two characters are in a valid index
            next_two_chars = int(s[index: index + 2])
            if next_two_chars <= 26:
                # remember, we want all possible ways to decode a string
                decodings += recursive_decode(s, index+2)

            # update memo
            memo[index] = decodings
            # Example: 127
            # 7 ends the recursion stack
            # memo[1 (integer 2)] = 1
            # memo[0 (integer 1)] = 1

            return decodings

        # trigger code
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        return recursive_decode(s, 0)
