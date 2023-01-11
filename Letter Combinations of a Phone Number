import sys
class Solution(object):
    def letterCombinations(self, digits):
       
        if not digits:
            return []
        letters = [
            None,
            None,
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        iterables = list(letters[int(n)] for n in digits)
        return [''.join(x) for x in product(*iterables)
