class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dlength = len(digits)

        if dlength < 1:
            return []
        else:
            memo = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            }

            def getPossibleComb(index, path):

                # recursion base case,length path is eq to length of digits
                if len(path) == len(digits):
                    # remember, path is an array
                    answer.append("".join(path))
                    return

                # now, get the possible path

                ans = memo[digits[index]]

                # compute all possible answers

                for digit in ans:
                    path.append(digit)

                    # check possible solutions

                    getPossibleComb(index+1, path)

                    # backtrack
                    path.pop()

            answer = []

            getPossibleComb(0, [])  # initial path is empty

            # Time Complexity: O(4**n * n) (input is at most of length 4)
            # Space Complexity: O(n) (recursion stack)
            return answer
